#include<bits/stdc++.h>
#define LL long long int
using namespace std;
int dp[105][3];
int Right[3][105];
char str[110];
int n;
int call(int i,int t)
{
    if(i==n) return t;
    if(dp[i][t]!=-1) return dp[i][t];
    return dp[i][t]=min(call(Right[t][i],1-t)+1,call(Right[1-t][i],t)+2);
}
int main()
{
   // freopen("B-large.in","r",stdin);
    //freopen("codejam.txt","w",stdout);
    int T,I=1;
    scanf("%d",&T);
    while(T--)
    {
    printf("Case #%d: ",I++);
   // scanf("%d",&n);
    scanf("%s",str);
    n=strlen(str);
    memset(dp,-1,sizeof(dp));
    int R=n;
    for(int i=n-1;i>=0;i--)
    {
       Right[0][i]=R;
        if(str[i]=='+')
            R=i;
    }
    R=n;
    for(int i=n-1;i>=0;i--)
    {
        Right[1][i]=R;
        if(str[i]=='-')
            R=i;
    }
    int t=(str[0]=='-')?1:0;
    printf("%d\n",min(call(Right[1-t][0],t),1+call(Right[1-t][0],1-t)));
    }
    return 0;
}
