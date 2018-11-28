#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int l, x;
string s;

int m[4][4] = { {1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1} };

int pre[10010];

int h(char c) {
    if (c == 'i') return 2;
    if (c == 'j') return 3;
    if (c == 'k') return 4;
}

int f(int p) {
    for (int i=1; i<=4; i++) if (abs(p) == i) return i-1;
}

int sgn(int p) {
    if (p==0) return 0;
    return p / abs(p);
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>l>>x;
        cin>>s;

        string str;

        for (int i=0; i<x; i++) str += s;

        pre[0] = h(str[0]);

        for (int i=1; i<l*x; i++) {

            pre[i] = m[f(pre[i-1])][f(h(str[i]))]*sgn(pre[i-1]);

        }

        bool good = 0;

        if (l*x > 2) {
            int r = h(str[l*x-1]);

            int y = h(str[l*x-2]);

            if (pre[l*x-3] == 2 && y==3 && r==4) good = 1;

            for (int i=l*x-3; i>0; i--) {

                y = m[f(h(str[i]))][f(y)]*sgn(y);

                if (pre[i-1] == 2 && y==3 && r==4) good = 1;

            }

            for (int j=l*x-2; j>1; j--) {

                r = m[f(h(str[j]))][f(r)]*sgn(r);

                y = h(str[j-1]);

                if (pre[j-2] == 2 && y==3 && r==4) good = 1;

                for (int i=j-2; i>0; i--) {

                    y = m[f(h(str[i]))][f(y)]*sgn(y);

                    if (pre[i-1] == 2 && y==3 && r==4) good = 1;

                }

            }
        }

        if (good) printf("Case #%d: YES\n", cas);
        else printf("Case #%d: NO\n", cas);
    }

    return 0;

}
