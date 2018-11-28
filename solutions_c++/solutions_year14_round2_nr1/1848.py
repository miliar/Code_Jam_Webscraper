#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <map>
#include <math.h>
#include <vector>
#include <limits.h>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>
#include <string.h>
#include <time.h>
#define ll long long
#define mp make_pair
#define pii pair<int,int>
#define vi vector<int>
#define vl vector<ll>
#define pll pair<ll,ll>
#define s second
#define f first
#define pb push_back
#define inf 2000000000ll
#define MAX 110
#define MOD 1000007ll
#define MAXX 1000100

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define fch(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define sz(x) (int((x).size()))
using namespace std;
string s;
int n,k,b[MAX][2],a[MAX][MAX],m,T;
char q[MAX][MAX];
int main()
{
    ios_base::sync_with_stdio(0);
    //memset(memo,-1,sizeof(memo));
    //memset(d,-1,sizeof(d));
    //memset(a,0,sizeof(a));
    //memset(vis,0,sizeof(vis));
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> T;
    rep (u,T)
    {
        cin >> n;
        k = 0;
        int p = 1;
        memset(a,0,sizeof(a));
        rep (i,MAX)
            rep (j,MAX)
                q[i][j] = '-';
        rep (i,MAX)
        {
            b[i][0] = MAX;
            b[i][1] = 0;
        }
        rep (i,n)
        {
            cin >> s;
            m = 0;
            a[i][0] = 1;
            q[i][0] = s[0];
            fer (j,1,s.size())
                if (s[j] == s[j - 1])
                   a[i][m]++;
                else {
                      m++;
                      a[i][m] = 1;
                      q[i][m] = s[j];
                }
            if (k == 0)
               k = m + 1;
            else if (m + 1 != k)
                    p = 0;
            rep (j,m + 1)
            {
                b[j][0] = min(b[j][0],a[i][j]);
                b[j][1] = max(b[j][1],a[i][j]);
            }
        }
        rep (j,k)
            fer (i,1,n)
                if (q[i][j] != q[i - 1][j])
                   p = 0;
        int res = 0;
        rep (j,k)
            res += b[j][1] - b[j][0];
        cout << "Case #" << u + 1 << ": ";
        if (p)
           cout << res << endl;
        else cout << "Fegla Won\n";
    }
    //system("pause");
    return 0;
}
