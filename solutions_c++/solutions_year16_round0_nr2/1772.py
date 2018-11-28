#include <bits/stdc++.h>
using namespace std;

int solve(string s){
	int ed = s.size();
	for(int i=s.size()-1;i>=0;i--){
		if( s[i] == '+' )ed = i;
		else break;
	}
	if(ed == 0)return 0;
	int cnt = 1;
	char c = s[0];
	for(int i=0;i<ed;i++){
		if(c != s[i]){
			c = s[i];
			cnt++;
		}
	}
	return cnt;
}

int main(void){
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		string s;cin >> s;
		cout << "Case #" << i+1 << ": ";
		cout << solve(s) << endl;
	}

	return 0;
}