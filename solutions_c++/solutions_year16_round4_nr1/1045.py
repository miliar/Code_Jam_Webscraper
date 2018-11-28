#include <bits/stdc++.h>
using namespace std;

string dp[13][128];
char ss[4]="RPS";
void init()
{
    for(int i=0;i<3;i++)
        dp[0][ss[i]]=ss[i];
    for(int i=1;i<13;i++)
    {
        dp[i]['R']=min(dp[i-1]['R']+dp[i-1]['P'],dp[i-1]['P']+dp[i-1]['R']);
        dp[i]['P']=min(dp[i-1]['P']+dp[i-1]['S'],dp[i-1]['S']+dp[i-1]['P']);
        dp[i]['S']=min(dp[i-1]['S']+dp[i-1]['R'],dp[i-1]['R']+dp[i-1]['S']);
    }
}
void solve()
{
    int n,r,p,s;
    scanf("%d%d%d%d",&n,&r,&p,&s);
    string ans;
    for(int i=0;i<3;i++)
    {
        int tr=0,tp=0,ts=0;
        //cout<<dp[n][ss[i]]<<endl;
        for(int j=0;j<dp[n][ss[i]].size();j++)
        {
            if(dp[n][ss[i]][j]=='R')   ++tr;
            else if(dp[n][ss[i]][j]=='P')  ++tp;
            else   ++ts;
        }
        //printf("%d %d %d\n",tr,tp,ts);
        if(r==tr&&p==tp&&s==ts)
        {
            if(ans=="")   ans=dp[n][ss[i]];
            else if(ans>dp[n][ss[i]])
                ans=dp[n][ss[i]];
        }
    }
    if(ans=="")   printf("IMPOSSIBLE\n");
    else   cout<<ans<<endl;
}
int main()
{
    int T;
    scanf("%d",&T);
    init();
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
