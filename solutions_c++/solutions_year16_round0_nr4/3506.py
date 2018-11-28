//kopyh
#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define N 1123456
using namespace std;
long long n,m,sum,res,flag;
long long a[200],b[200];
int main()
{
    long long i,j,k,cas,T,t,x,y,z,c,s;
    #ifndef ONLINE_JUDGE
        freopen("in.in","r",stdin);
        freopen("out.out","w",stdout);
    #endif
    scanf("%I64d",&T);
    cas=0;
    while(T--)
//    while(scanf("%I64d",&n)!=EOF)
    {
        printf("Case #%I64d:",++cas);
        scanf("%I64d%I64d%I64d",&k,&c,&s);
        n=(k+c-1)/c;
        if(s<n)printf(" IMPOSSIBLE\n");
        else
        {
            for(i=1;i<=min(s,k);i++)
                printf(" %I64d",i);
            printf("\n");
        }
    }
    return 0;
}
