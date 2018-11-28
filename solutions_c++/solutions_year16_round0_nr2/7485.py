#include<iostream>
#include<string>
using namespace std;

int main(){
	
	int t;
	cin>>t;
	
	for(int ii=1;ii<=t;ii++){
		string s = "";
		std::cin>>s;
		int l = s.length();
		char sw = '-';
		int ans=0;
		for(int i=l-1;i>=0;i--){
			//cout<<s[i];
			if(s[i]==sw){
				ans++;
				if(sw=='-'){
					sw = '+';
				}else{
					sw = '-';
				}
			}
		}
		cout<<"Case #"<<ii<<": "<<ans<<"\n";
	}
}
