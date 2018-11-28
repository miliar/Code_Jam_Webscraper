//kopyh
#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define N 11234
using namespace std;
int n,m,sum,res,flag;
char s[N],ans[N];
int main()
{
    int i,j,k,cas,T,t,x,y,z;
//    #ifndef ONLINE_JUDGE
//        freopen("in.in","r",stdin);
//        freopen("out.out","w",stdout);
//    #endif
    scanf("%d",&T);
    cas=0;
    while(T--)
//    while(scanf("%d",&n)!=EOF)
    {
        scanf("%s",s);
        memset(ans,'#',sizeof(ans));
        ans[2000]=s[0];
        i=2000;j=2001;
        n=strlen(s);
        for(k=1;k<n;k++)
        {
            if(s[k]>=ans[i])
            {
                i--;
                ans[i]=s[k];
            }
            else
            {
                ans[j]=s[k];
                j++;
            }
        }
        printf("Case #%d: ",++cas);
        for(;i<=j;i++)
            if(ans[i]!='#')
                printf("%c",ans[i]);
        printf("\n");
    }
    return 0;
}
