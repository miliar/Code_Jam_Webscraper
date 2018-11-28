#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int k=0;k<t;k++){
		int n;
		string s;
		cin>>n>>s;
		long long sum=0;
		long long ans=0;
		for(int i=0;i<=n;i++){
			//cout<<ans<<" "<<sum<<" "<<i<<endl;
			long long shy=s[i]-'0';
			if(sum<i){
				ans+=i-sum;
				sum+=(i-sum);
			}
			sum+=shy;
		}
		cout<<"Case #"<<k+1<<": "<<ans<<endl;
	}
}
