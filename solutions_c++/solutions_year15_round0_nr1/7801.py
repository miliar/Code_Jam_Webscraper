#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	
	int t,j=1;
	cin>>t;
	
	while(t--){
	
	long long int dp[1004]={0};
	int n,i;
	long long int a[1004],count=0;
	cin>>n;
	string s;
	cin>>s;
	for(i=0;i<=n;i++)
		a[i]=s[i]-48;
    dp[0]=a[0];
	for(i=1;i<=n;i++){
		if(i>dp[i-1]&&a[i]>0){
			count+=(i-dp[i-1]);
			dp[i]=a[i]+dp[i-1]+(i-dp[i-1]);
		}
		else
		dp[i]=a[i]+dp[i-1];
		
	}
	   cout<<"Case #"<<(j++)<<": "<<count<<endl;
	}
	return 0;
}
