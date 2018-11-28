#include <iostream>
#include <string>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long long sm;
		string s;
		cin>>sm>>s;
		int tot=0;
		int ans=0;
		for(int j=0;j<=sm;j++){
			//cout<<"tot "<<tot<<" j="<<j<<"\n";
			if(tot<j){
				ans+=(j-tot);
				tot=j;
			}
			tot+=(s[j]-'0');
		}
		cout<<"Case #"<<i<<": ";
		cout<<ans<<"\n";
	}
}
