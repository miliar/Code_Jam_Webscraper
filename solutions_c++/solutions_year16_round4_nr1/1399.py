#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
using namespace std;
int dp[13][3];
char t[13][4100];
map<char,char>mp;
void solve(char* a,int n)
{
    int i,j,k;
    for(k=2;k<=n;k<<=1)
    {
        for(i=0;i<n;i+=k)
        {
            if(strncmp(a+i,a+i+(k>>1),k>>1)>0)
                for(j=i;j<i+(k>>1);++j)
                    swap(a[j],a[j+(k>>1)]);
        }
    }
}
void output(int n,char a)
{
    t[0][0]=a;
    int i,j,k;
    char c1,c2;
    for(k=1;k<=n;++k)
    {
        for(i=0,j=0;t[k-1][i];++i)
        {
            c1=t[k-1][i];
            c2=mp[c1];
            t[k][j++]=c1;
            t[k][j++]=c2;
        }
    }
    solve(t[n],1<<n);
    puts(t[n]);
}
int main()
{
    mp['S']='P';
    mp['P']='R';
    mp['R']='S';
    dp[0][0]=1;
    for(int  i=1;i<=12;++i)
    {
        dp[i][0]=dp[i-1][0]+dp[i-1][2];
        dp[i][1]=dp[i-1][1]+dp[i-1][0];
        dp[i][2]=dp[i-1][1]+dp[i-1][2];
    }
    int T,t,n,c,b,a;
    scanf("%d",&T);
    for(t=1;t<=T;++t)
    {
        scanf("%d%d%d%d",&n,&c,&b,&a);
        printf("Case #%d: ",t);
        if(a==dp[n][0]&&b==dp[n][1]&&c==dp[n][2])
            output(n,'S');
        else if(a==dp[n][1]&&b==dp[n][2]&&c==dp[n][0])
            output(n,'R');
        else if(a==dp[n][2]&&b==dp[n][0]&&c==dp[n][1])
            output(n,'P');
        else puts("IMPOSSIBLE");
    }
    return 0;
}
