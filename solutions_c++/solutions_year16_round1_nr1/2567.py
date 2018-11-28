#include <bits/stdc++.h>
using namespace std;

string solve(string s){
	string ret;
	for(int i=0;i<s.size();i++){
		if(ret+s[i] > s[i]+ret){
			ret += s[i];
		}else{
			ret = s[i] + ret;
		}
	}
	return ret;
}

int main(void){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		cout << "Case #" << i+1 << ": ";
		string s;cin >> s;
		cout << solve(s) << endl;

	}

	return 0;
}