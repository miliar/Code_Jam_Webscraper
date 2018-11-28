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
#define MAX 3000
#define MOD 1000000007ll
#define MAXX 1000100

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define fch(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define sz(x) (int((x).size()))
using namespace std;
int main()
{
    //ios_base::sync_with_stdio(0);
    //memset(memo,-1,sizeof(memo));
    //memset(d,-1,sizeof(d));
    //memset(C,0,sizeof(C));
    //memset(vis,0,sizeof(vis));
    freopen("D-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,n,r2,r1;
    double a[MAX],b[MAX];
    cin >> T;
    rep (u,T)
    {
        cin >> n;
        rep (i,n)
            cin >> a[i];
        rep (i,n)
            cin >> b[i];
        sort (a,a + n);
        sort (b,b + n);
        r2 = n;
        r1 = 0;
        int l = n - 1,r = n - 1;
        while (l >= 0 && r >= 0)
        {
              if (a[l] < b[r])
                 {
                       r2--;
                       l--;
                       r--;
                 }
              else l--;
        }
        l = n - 1,r = n - 1;
        while (l >= 0 && r >= 0)
        {
              if (a[l] > b[r])
                 {
                       r1++;
                       l--;
                       r--;
                 }
              else r--;
        }
        printf ("Case #%d: %d %d\n",u + 1,r1,r2);
    }
    //system("pause");
    return 0;
}

