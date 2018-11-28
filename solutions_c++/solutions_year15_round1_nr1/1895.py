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

int m[1010];

int main() {
    //freopen("in","r",stdin);
    //freopen("out","w",stdout);
    int t, r1, r2, maiorDif;
    cin >> t;
    for(int cas = 1; cas <= t; ++cas)
    {
        int n;
        cin >> n;
        for(int i = 0; i < n; ++i)
            cin >> m[i];
        r1 = r2 = 0;
        maiorDif = 0;
        for(int i = 1; i < n; ++i) {
            if (m[i] < m[i - 1]) {
                r1 += m[i - 1] - m[i];
                maiorDif = max(maiorDif,m[i - 1] - m[i]);
            }
        }
        for(int i = 0; i < n - 1; ++i)
            r2 += min(m[i],maiorDif);
        printf("Case #%d: %d %d\n",cas,r1,r2);
    }
    return 0;
}
