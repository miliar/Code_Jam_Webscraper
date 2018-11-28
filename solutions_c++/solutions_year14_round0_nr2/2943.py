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
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    double C,F,X,Cur,CurSp,t;
    rep (i,T)
    {
        t = 0.0;
        CurSp = 2.0;
        Cur = 0.0;
        cin >> C >> F >> X;
        while (fabs (Cur - X) > 1e-8)
        {
              if (Cur < C)
                 {
                      t += (min (X,C) - Cur)/CurSp;
                      Cur = min (X,C);
                 }
              if ((X - Cur + C)/(CurSp + F) < (X - Cur)/CurSp)
                 {
                     Cur = 0.0;
                     CurSp += F;
                 }
              else if (fabs(Cur - X) > 1e-9)
                      {
                                t += (X - Cur)/CurSp;
                                Cur = X;
                      }
        }
        cout << "Case #" << i + 1 << ": ";
        cout.precision(7);
        cout << fixed << t << endl;
    }
    //system("pause");
    return 0;
}
