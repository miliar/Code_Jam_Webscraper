#include<bits/stdc++.h>
using namespace std;

string solve(string s) {
	
	vector<int> alpha(300, 0);
	for(int i=0; i<s.size(); i++) {
		alpha[s[i]]++;
	}
	
	vector<int> cnt(10, 0);
	cnt[0] = alpha['Z'];
	cnt[2] = alpha['W'];
	cnt[8] = alpha['G'];
	cnt[6] = alpha['X'];
	cnt[7] = alpha['S'] - cnt[6];
	cnt[5] = alpha['V'] - cnt[7];
	cnt[3] = alpha['H'] - cnt[8];
	cnt[4] = alpha['F'] - cnt[5];
	cnt[9] = alpha['I'] - cnt[6] - cnt[5] - cnt[8];
	cnt[1] = alpha['O'] - cnt[0] - cnt[2] - cnt[4];
	
	
	string t;
	for(int i=0; i<10; i++) {
		string tmp = ".";
		tmp[0] = '0' + i;
		for(int j=0; j<cnt[i]; j++)
			t += tmp;
	}
	
	return t;
}

int main() {
	int N;
	cin >> N;
	for(int i=0; i<N;i ++) {
		
		string s;
		cin >> s;
		string ans = solve(s);
		cout << "Case #" << i+1 << ": " << ans << endl;
		
	}
	
	return 0;
	
}

