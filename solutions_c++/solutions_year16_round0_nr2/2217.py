#include <bits/stdc++.h>
using namespace std;
int main(){
	int cases;cin>>cases;
	for(int n=0;n<cases;n++){
		string s;cin>>s;
		int changes = 0;
		char curr = s[0];
		for(int i=1;i<s.size();i++){
			if(s[i] != curr) changes += 1;
			curr = s[i];
		}
		if(s[s.size()-1] == '-') changes += 1;
		cout<<"Case #"<<n+1<<": "<<changes<<endl;
	}
	return 0;
}
