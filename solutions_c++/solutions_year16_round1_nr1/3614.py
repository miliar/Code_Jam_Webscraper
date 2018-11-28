#include <iostream>
#include <string>
using namespace std;
int main(){
	int T,i,count;
	string s;
	cin>>T;
	i=T;
	while(T>0){
		count = 0;
		cin>>s;
		if(s.size()==0) {
			T--;
			cout<<"Case #"<<i-T<<": \n";
		}
		string ans;
		char first, last;
		first=s[0];
		last=s[0];
		ans=ans+first;

		for(int j=1;j<s.size();j++){
			if(s[j]>=first) {
				ans=s[j]+ans;
				first=s[j];
			}else{
				ans=ans+s[j];
				last=s[j];
			}
		}
		T--;
		cout<<"Case #"<<i-T<<": "<<ans<<"\n";
	}
	return 0;
}