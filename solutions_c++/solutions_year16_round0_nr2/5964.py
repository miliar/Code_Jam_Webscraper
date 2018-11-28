#include <bits/stdc++.h>
#include<algorithm>
using namespace std;
int main() {
    
	freopen("B-large.in","r",stdin);
	freopen("outputB.out","w",stdout);
    
	int t,i,j,k;
    char arr[200];
    int dp[200];
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cout<<"Case #"<<k<<": ";
        cin>>arr;
        if(arr[0]=='+')
        dp[0]=0;
        else
        dp[0]=1;
        
        for(i=1;arr[i]!='\0';i++)
        {
            if(arr[i]=='+')
            {
                dp[i]=dp[i-1];
            }
            else
            {
                if(arr[i-1]=='+')
                {
                    dp[i]=dp[i-1]+2;
                }
                else
                {
                    dp[i]=dp[i-1];
                }
            }
        }
        cout<<dp[i-1]<<endl;
    }
	return 0;
}

