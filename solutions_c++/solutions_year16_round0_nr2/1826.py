#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  //freopen("input1.txt","r",stdin);
  //freopen("output1l.txt","w",stdout);
   int t; cin >> t;
   for(int k=1;k<=t;k++)
   {
      string s;
       cin >> s;
       long long dp[1001];
       memset(dp,0,sizeof(dp));
       dp[0]=0;
       int l = s.length();
       if(s[0] =='-') dp[1]=1;
       for(int i=2;i<=l;i++)
       {
         if(s[i-1] == '+') dp[i] = dp[i-1];
         if(s[i-1] == '-' && s[i-2]=='-') dp[i] = dp[i-1];
         if(s[i-1] == '-' && s[i-2] == '+') dp[i] = dp[i-1] + 2; 
        }
        printf("Case #%d: %lld\n",k,dp[l]);
   }
   return 0;
}
