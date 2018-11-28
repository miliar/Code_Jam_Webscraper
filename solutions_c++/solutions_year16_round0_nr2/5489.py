#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,k;
	cin>>t;
	string s;
	k=1;
	while(t--)
	{   
		cin>>s;
		int l=s.length();
		int dp[l];
		if(s[0]=='+')
			dp[0]=0;
		else
			dp[0]=1;
        int i=0;
        while(s[i]=='-' && i<l)i++;
        dp[i-1]=1;
        for(int j=i;j<l;)
        {
         
             if(s[j]=='+')
	        	{dp[j]=dp[j-1];
	        		//cout<<dp[j];
	        		j++;
	        	}
	        else
	        {  int f=j;
	        	while(s[f]=='-')
	        	{
	   	              f++; 
	   	        }
	   	         dp[f-1]=dp[j-1]+2;
	   	         j=f;
	   	         //cout<<dp[f-1];
	        }
	        
        }
        cout<<"Case #"<<k++<<": "<<dp[l-1]<<endl;

	}
}