#include<bits/stdc++.h>

using namespace std;
int dp[1111];
int n;
int a[1111];
int maxi;
int ceil(int l,int r,int x){
	while(r-l>1){
		int m=(r+l)>>1;
		if(a[m]<=x)
			l=m;
		else
			r=m;
	}
	return r;
}

int find(int min){
	int i;
	bool ans=0;
	for(i=1;i<=maxi;i++){
		int eat_idx=ceil(0,n-1,i);
		//cout<<eat_idx<<endl;
		if(eat_idx!=0){
			int wait_time=(dp[n-1]-dp[eat_idx-1]);
			if(wait_time%i==0)
				wait_time=(wait_time/i)-1;
			else
				wait_time/=i;
			ans|=(i+wait_time<=min);
		}
		else{
			int wait_time=dp[n-1];
			if(wait_time%i==0)
				wait_time=(wait_time/i)-1;
			else
				wait_time/=i;
			ans|=(i+wait_time<=min);
		}
			
	}
	return ans;
}

int main(){
	int t;
	cin>>t;
	for(int kk=1;kk<=t;kk++){
		cin>>n;
		int i,j;
		maxi=0;
		for(i=0;i<n;i++){
			cin>>a[i];
			maxi=max(maxi,a[i]);
		}
		dp[0]=a[0];
		for(i=1;i<n;i++)
			dp[i]=dp[i-1]+a[i];
		int l=1;
		int r=maxi;
		while(r-l>1){
			int m=(r+l)>>1;
			if(find(m)){
				r=m;
			} 
			else
				l=m;
			//cout<<l<<" "<<r<<endl;
		} 
		cout<<"Case #"<<kk<<": "<<r<<endl;
		memset(dp,0,sizeof(dp));
	}
}

