#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<map>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int,int> PII;
#define PB push_back
#define MP make_pair
#define fi first
#define se second
#define inf 1e9
#define eps 1e-9
int g[105][105];
int vstr[105],vstc[105],rv,cv;
int main()
{
    int n,m,t;
    int i,j,k;
    freopen("bl.in","r",stdin);
    freopen("bl.out","w",stdout);
    scanf("%d",&t);
    for(int cnt = 1;cnt<=t;cnt++)
    {
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++)for(j=0;j<m;j++)
            scanf("%d",&g[i][j]);
        memset(vstr,0,sizeof(vstr));
        memset(vstc,0,sizeof(vstc));
        rv=cv=0;
        int yes = 1;
        while(rv!=n&&cv!=m)
        {
            int mi=100,mr,mc;
            for(i=0;i<n;i++)if(!vstr[i])for(j=0;j<m;j++)if(!vstc[j])
            {
                if(g[i][j]<mi)
                {
                    mi = g[i][j];
                    mr = i;
                    mc = j;
                }
            }
            for(i=0;i<n;i++)if(g[i][mc]!=mi&&!vstr[i])
                break;
            if(i==n)
            {
                cv++;
                vstc[mc] = 1;
                continue;
            }
            for(i=0;i<m;i++)if(g[mr][i]!=mi&&!vstc[i])
                break;
            if(i==m)
            {
                rv++;
                vstr[mr] = 1;
                continue;
            }
            yes = 0;
            break;
        }
        printf("Case #%d: ",cnt);
        if(yes)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
