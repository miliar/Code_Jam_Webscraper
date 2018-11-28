#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include <fstream>
using namespace std;
const int mod = 1e9+7;
#define LL long long
#define mem(a,b) memset(a,b,sizeof(a))
int a[105][105],n,m;
int aa[105],bb[105];
int main()
{
    int i,j,t;

    int cas=0;

    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        mem(aa,0);
        mem(bb,0);
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                scanf("%d",&a[i][j]);
                aa[i]=max(aa[i],a[i][j]);
                bb[j]=max(bb[j],a[i][j]);
            }
        }
        int flag=0;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if(aa[i]==a[i][j]||bb[j]==a[i][j])continue;
                flag=1;break;
            }
        }
        printf("Case #%d: ",++cas);
        if(flag)
          puts("NO");
        else puts("YES");
    }
}
