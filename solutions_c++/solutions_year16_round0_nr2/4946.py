//kopyh
#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define N 1123
using namespace std;
int n,m,sum,res,flag,a,b,c,d;
char s[N];
int main()
{
    int i,j,k,cas,T,t,x,y,z;
    #ifndef ONLINE_JUDGE
        freopen("in.in","r",stdin);
        freopen("out.out","w",stdout);
    #endif
    scanf("%d",&T);
    cas=0;
    while(T--)
//    while(scanf("%d",&n)!=EOF)
    {
        scanf("%s",s);
        sum=0;
        n=strlen(s);
        for(i=1;i<n;i++)
            if(s[i]!=s[i-1])
                sum++;
        if(s[n-1]=='-')sum++;
        printf("Case #%d: %d\n",++cas,sum);
    }
    return 0;
}
