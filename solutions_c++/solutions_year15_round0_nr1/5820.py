#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>

#define INF 1000000000
#define Inf 1000000000000000000
#define mp make_pair
#define pb push_back
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int main() {
    //freopen("inLargeA","r",stdin);
    //freopen("outLargeA","w",stdout);
    int t, s, x, v;
    string str;
    cin >> t;
    for(int cas = 1; cas <= t; ++cas)
    {
        int resp = 0;
        cin >> s;
        cin >> str;
        v = 0;
        for(int i = 1; i < str.size(); ++i)
        {
            v += (int)(str[i - 1] - '0');
            if (v < i) {
                int aux = i - v;
                resp += aux;
                v += aux;
            }
        }
        cout << "Case #" << cas << ": " << resp << endl;

    }
    return 0;
}
