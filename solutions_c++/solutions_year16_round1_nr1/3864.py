#include <bits/stdc++.h>
using namespace std;

string res(string s){
	if(s=="") return "";
	int m = s.size();
	ostringstream os;
	int idx = 0, cnt = 0;
	for(int j=0; j<m; j++) if(s[j]>s[idx]){
		idx = j; cnt = 1;
	} else if(s[j]==s[idx]) cnt++;		
	for(int j=0; j<cnt; j++) cout << s[idx];
	os << res(s.substr(0,idx));
	for(int j=idx+1; j<m; j++) if(s[j]!=s[idx]) os << s[j];
	return os.str();
}

int main(){	
	int t; cin >> t;
	for(int i=0; i<t; i++){
		string s; cin >> s;		
		cout << "Case #" << (i+1) << ": ";
		cout << res(s) << '\n';
	}
	return 0;
}
