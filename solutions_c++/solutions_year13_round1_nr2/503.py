#include <iostream>
using namespace std;

int tn, tt;
int e,r,n;
int v[10010];
int f[10010][20];

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("pB_small.out","w",stdout);
    cin >> tn;
    for (tt=1;tt<=tn;tt++)
    {
        int i,j,k;
        cin >> e >> r >> n;
        for (i=1;i<=n;i++)
            cin >> v[i];
        
        memset(f,0,sizeof f);
        for (j=0;j<=e;j++)
            f[1][j] = (e-j)*v[1];
        for (i=2;i<=n;i++)
            for (j=0;j<=e;j++)
            {
                for (k=max(j-r,0);k<=e;k++)
                {
                    int tmp = f[i-1][k] + (min(k+r,e)-j)*v[i];
                    f[i][j] = max(f[i][j],tmp);
                }
            }
        int ans = 0;
        for (j=0;j<=e;j++)
            ans = max(ans,f[n][j]);
        cout << "Case #" << tt << ": " << ans << endl;
    }
}
