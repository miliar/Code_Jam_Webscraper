#include<iostream>
#include<string>
using namespace std;
int main(){
	int t,cas,ans,count,n;
	cin>>t;
	cas=0;
	while(t--){
		cas++;
		string st;
		cin>>n>>st;
		count=ans=0;
		count+=(st[0]-'0');
		for(int i=1;i<=n;i++){
			if(count<i){
				ans+=(i-count);
				count+=(i-count);
			}
			count+=(st[i]-'0');
		}
		cout<<"Case #"<<cas<<": "<<ans<<"\n";
	}
}
