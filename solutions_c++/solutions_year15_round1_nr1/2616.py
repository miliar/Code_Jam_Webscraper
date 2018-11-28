#include <bits/stdc++.h>

using namespace std;
int main(){
	int t,ca=0;cin>>t;
	while(t-->0){
		ca++;
		int n;cin>>n;
		int arr[n];
		for(int i=0;i<n;i++)cin>>arr[i];
		int ans1=0,ans2=0,ma=0;
		for(int i=1;i<n;i++){
			if(arr[i]<arr[i-1])ans1+=arr[i-1]-arr[i];
		}
		for(int i=1;i<n;i++){
			if(arr[i]<=arr[i-1])ma=max(ma,arr[i-1]-arr[i]);
		}
		for(int i=1;i<n;i++){
			if(arr[i-1]>=ma)ans2+=ma;
			else ans2+=arr[i-1];
		}
		cout<<"Case #"<<ca<<": "<<ans1<<' '<<ans2<<endl;
	}
	return 0;
} 
