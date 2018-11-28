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

int n, l;
string s[110];
string bad;

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {
        cin>>n>>l;
        for (int i=0; i<n; i++) {
            cin>>s[i];
        }
        cin>>bad;

        bool good = 1;
        for (int i=0; i<n; i++) {
            if (bad == s[i]) {
                good = 0;
            }
        }

        if (!good) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }

        int z = 0, o = 0, a = 0;
        for (int i=0; i<n; i++) {
            bool found = 0;
            int tz = 0, to = 0, ta = 0;
            for (int j=0; j<s[i].length(); j++) {
                if (s[i][j] == '0') {
                    if (found) ta++;
                    else tz++;
                }
                else {
                    to++;
                    found = 1;
                }
            }
            z = max(z, tz);
            o = max(o, to);
            a = max(a, ta);
        }

        if (a == 0) {
            z--; a++;
        }

        string x, y;
        for (int i=0; i<l; i++) {
            x += "0?";
        }
        for (int i=0; i<l-1; i++) {
            y += "1";
        }
        if (l == 1) {
            y += "0";
        }

        printf("Case #%d: %s %s\n", cas, x.c_str(), y.c_str());

    }

    return 0;

}
