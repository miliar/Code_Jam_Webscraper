
#include<iostream>
using namespace std;

long long dp[1000005];

long long turn(long long x){
	long long f=0;
	while(x){
		f=f*10+(x%10);
		x/=10;
	}
	return f;
}

int main(){
	int nn,r=1;
	long long n, m;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	dp[0] = 0;
	for( n = 1; n <= 1000000; n++ ) {
		m = turn(n);
		if( m < n && n%10 )	dp[n] = min(dp[n-1]+1,dp[m]+1);
		else dp[n] = dp[n-1]+1;
	}
	cin>>nn;
	while(nn--){
		cin>>n;
		cout<<"Case #"<<r<<": "<<dp[n]<<endl;
		r++;
	}
	return 0;
}
