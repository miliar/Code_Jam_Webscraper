#include <iostream>
#include <string>
using namespace std;
int T,n; string shy;
int main() {
	cin>>T;
	for(int t=0;t<T;t++){
		cin>>n>>shy; int sum=0, ans=0;
		for(int i=0;i<shy.size();i++){
			if(sum<i) { ans+=(i-sum); sum=i; }
			sum+=shy[i]-'0';
		} cout<<"Case #"<<t+1<<": "<<ans<<'\n';
	}
	return 0;
}