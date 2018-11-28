#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes 
	long long int t,k,add,i,n;
	char x;
	cin>>t;
	k=1;
	while(t--){
		add=0;
		cin>>n;
		int a[n+1];
		long long int dp[n+1];
		getchar();
		for(i=0;i<=n;i++){
			cin>>x;
		//	cout<<x;
			a[i]=x-48;
		}
		dp[0]=a[0];
	//	cout<<dp[0]<<" ";
		for(i=1;i<=n;i++){
			if(dp[i-1]>=i || a[i]==0){
				dp[i]=dp[i-1]+a[i];
			}
			else{
				add=add+(i-dp[i-1]);
				dp[i]=dp[i-1]+a[i]+add;
			}
		//	cout<<dp[i]<<" ";
		}
		cout<<"Case #"<<k<<": "<<add<<endl;
		k++;
	}
	return 0;
}
