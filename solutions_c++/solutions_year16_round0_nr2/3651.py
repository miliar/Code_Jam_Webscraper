#include<bits/stdc++.h>
#include<fstream>

using namespace std;

int main(){
	ofstream archivo;
	archivo.open("codejamBlarge.out");
	int t;cin>>t;
	for(int i=1;i<=t;i++){
		archivo<<"Case #"<<i<<": ";
		string s;cin>>s;
		int cont=0;
		if(s[s.size()-1]=='-') cont++;
		for(int i=1;i<s.size();i++){
			if(s[i]==s[i-1]) continue;
			else cont++;
		}
		archivo<<cont<<endl;
	}
	archivo.close();
}
