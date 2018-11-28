#include <bits/stdc++.h>

using namespace std;

int cnt[10][26], cur[26];

string ans;

void rec(string s, int last){
	bool ok = true;
	for (int i = 0; i < 26; i++){
		if (cur[i] != 0){
			ok = false;
			break;
		}
	}
	
	if (ok){
		ans = s;
		return;
	}
	
	for (int i = last; i < 10; i++){
		bool ok = true;
		for (int j = 0; j < 26; j++){
			if (cnt[i][j] > cur[j]){
				ok = false;
			}
		}
		
		if (ok){
			for (int j = 0; j < 26; j++) cur[j] -= cnt[i][j];
			rec(s + (char)(i + '0'), i);
			for (int j = 0; j < 26; j++) cur[j] += cnt[i][j];
		}
	}
	
	return;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	string words[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	
	for (int i = 0; i < 10; i++){
		for (int j = 0; j < (int)words[i].length(); j++){
			cnt[i][words[i][j] - 'A']++;
		}
	}
	
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		string s;
		cin >> s;
		
		int n = s.length();
		for (int i = 0; i < 26; i++) cur[i] = 0;
		for (int i = 0; i < n; i++) cur[s[i] - 'A']++;
		
		ans = "";
		rec("", 0);
		
		cout << "Case #" << t + 1 << ": " << ans << endl;	
	}
	
	return 0;
}
