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
#define inf 1000000000ll
#define MAX 200
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
    //memset(used,0,sizeof(used));
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int a[5][5],T,r,x,y,b[5][5],n;
    cin >> T;
    rep (u,T)
    {
        r = 0;
        cin >> x;
        x--;
        rep (i,4)
            rep (j,4)
                cin >> a[i][j];
        cin >> y;
        y--;
        rep (i,4)
            rep (j,4)
                cin >> b[i][j];
        rep (i,4)
            rep (j,4)
                if (a[x][i] == b[y][j])
                   {
                            r++;
                            n = a[x][i];
                   }
        if (r == 1)
           cout << "Case #" << u + 1 << ": " << n << endl;
        else if (r == 0)
                cout << "Case #" << u + 1 << ": Volunteer cheated!\n";
        else cout << "Case #" << u + 1 << ": Bad magician!\n";
    }
    //system("pause");
    return 0;
}
