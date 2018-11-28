#include<bits/stdc++.h>
using namespace std;
int main(){
	int i,sum,smax,t,ans,count;
	char s[10000];
	
	#ifndef ONLINE_JUDGE
		freopen("inp","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	cin>>t;
	count=1;
	while(t--){
		cout<<"Case #"<<count<<": ";
		cin>>smax;
		cin>>s;
		sum=ans=0;
		for(i=0;i<=smax;i++){
			if(sum<i){
				ans+=(i-sum);
				sum+=(i-sum);
			}
			sum+=(s[i]-'0');
		}
		count++;
		cout<<ans<<endl;
	}
	
return 0;
}
