#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d\n",&t);
	for(int gh=1;gh<=t;gh++)
	{
       string str;
       cin>>str;
       int dp[str.length()];
       dp[0]=(str[0]=='-');
       for(int i=1;i<str.length();i++)
       {
    	   if(str[i]=='+')
    		   dp[i]=dp[i-1];
    	   else
    	   {
    		   if(str[i-1]=='-')
    			   dp[i]=dp[i-1];
    		   else
    			   dp[i]=dp[i-1]+2;
    	   }
       }
       printf("Case #%d: %d\n",gh,dp[str.length()-1]);
	}
	return 0;
}
