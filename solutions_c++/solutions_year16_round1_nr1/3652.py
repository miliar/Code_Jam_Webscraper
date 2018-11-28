#include <bits/stdc++.h>
using namespace std;

string solve(string in){
	string res;
	for(char &c: in){
		if(res.empty()) res+=c;
		else if(res[0]<=c) res=string(1,c)+res;
		else res+=c;
	}
	return res;
}

int main(){

	int t;
	cin>>t;
	for(int tc=1; tc<=t; tc++){
		string in;
		cin>>in;
		cout<<"Case #"<<tc<<": "<<solve(in)<<endl;
	}

	return 0;
}
