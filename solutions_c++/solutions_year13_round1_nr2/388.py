#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#define rep(i,j,k) for (int i=j;i<=k;++i)
#define rrep(i,j,k) for (int i=j;i>=k;--i)

using namespace std;

const int MAXN = 11111111;
const int INF = 0x7FFFFFFF/2;
int e,r,n;
int v[20];
int f[20][20];

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    cin >> T;
    rep(test,1,T)
	{
	    memset(f,0,sizeof(f));
	    cin >> e >> r >> n;
	    rep(i,1,n) cin >> v[i];
	    rep(i,0,e-1) f[0][i] = -INF;
	    rep(i,1,n) rep(j,0,e)
		{
		    rep(k,0,e) rep(l,0,k)
			if (min((k - l) + r,e) == j)
			    f[i][j] = max(f[i-1][k] + l * v[i],f[i][j]);
		}
	    int ans = 0;
	    rep(i,0,e) ans = max(f[n][i],ans);
	    cout << "Case #" << test << ": ";
	    cout << ans << endl;
	}
    return 0;
}
