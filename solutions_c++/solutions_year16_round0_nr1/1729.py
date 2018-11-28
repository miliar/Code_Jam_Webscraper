#include <bits/stdc++.h>
using namespace std;

int solve(int n){
	set<char> st;
	for(int i=1;i<=100;i++){
		int m = n * i;
		string s = to_string(m);
		for(int j=0;j<s.size();j++){
			st.insert(s[j]);
		}
		if(st.size() == 10){
			return m;
		}
	}
	return -1;
}

int main(void){
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		int n;cin >> n;
		cout << "Case #" << i+1 << ": ";
		int ret = solve(n);
		if(ret == -1)cout << "INSOMNIA" << endl;
		else cout << ret << endl;
	}
	return 0;
}