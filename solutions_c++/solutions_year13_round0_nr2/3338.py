#define _CRT_SECURE_NO_DEPRECATE

#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <ctime>
using namespace std;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define eps 1e-9
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;


int T;
int h, w;
int a[110][110];
int mn, mx, mi, mj;
bool ans;


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("b_output.txt", "w", stdout);

    scanf("%d", &T);
    FOR(test, 1, T)
    {
        scanf("%d %d", &h, &w);
        rep(j, h)
            rep(i, w)
                scanf("%d", &a[i][j]);

        ans = true;

        rep(i, w)
        {
            rep(j, h)
            {
                // checking a row
                mx = -1;
                rep(k, w)
                    mx = max(mx, a[k][j]);

                if (mx <= a[i][j])
                    continue;

                // checking a column
                mx = -1;
                rep(k, h)
                    mx = max(mx, a[i][k]);

                if (mx > a[i][j])
                {
                    ans = false;
                    break;
                }
            }

            if (ans == false)
                break;
        }

        printf("Case #%d: ", test);
        if (ans)
            printf("YES\n");
        else
            printf("NO\n");
    }

    return 0;
}
