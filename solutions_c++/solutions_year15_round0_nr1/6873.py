#include <iostream>
#include <string>
using namespace std;
int main(){
	int t;
	cin.tie(0);
	cin.sync_with_stdio(0);
	cin>>t;
	for(int k=1;k<=t;k++){
		int x;
		string s;
		cin>>x>>s;
		int parados = 0;
		int amigos = 0;
		for(int i=0;i<=x;i++){
			if(parados<i and s[i]!='0'){
				int necesarios = i - parados;
				amigos += necesarios;
				parados += necesarios;
			}
			parados+=s[i]-'0';
		}
		cout<<"Case #"<<k<<": "<<amigos<<'\n';
	}
	return 0;
}