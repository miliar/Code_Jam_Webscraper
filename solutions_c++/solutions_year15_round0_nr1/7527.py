#include <iostream>
#include <string>
using namespace std;

bool vis[1010];
int main() {
	int t,s;
	string str;
	cin>>t;
	for(int c=1;c<=t;c++){
		cin>>s>>str;
		
		int cont =0,rpta=0;
		for(int i=0;i<str.length();i++){
			if(str[i]=='0') continue;
			if(cont>=i){
				cont += (str[i]-'0');
			}else{
				rpta += (i-cont);
				cont=i+(str[i]-'0');
			}
		}
		cout<<"Case #"<<c<<": "<<rpta<<endl;
	}
	return 0;
}