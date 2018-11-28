#include <bits/stdc++.h>
#define rf freopen("ioi.in", "r", stdin)
#define wf freopen("ioi.out", "w", stdout)
using namespace std;
int t, f[26], g[26];
string s;
bool find(string &s, string ch){
	memset(f, 0, sizeof f);
	memset(g, 0, sizeof g);
	for(char x : s)  f[x - 'A']++;
	for(char x : ch) g[x - 'A']++;
	bool ok = true;
	for(int i = 0; i < 26; i++) ok &= (g[i] <= f[i]);
	if(ok){
		string temp = "";
		for(int i = 0; i < 26; i++){
			int r = f[i] - g[i];
			for(int j = 1; j <= r; j++)
				temp += (char)(i + 65);
		}
		s = temp;
		return true;
	}
	return false;
}
int main(){
	ios :: sync_with_stdio(false);
	rf;
	wf;
	cin >> t;
	for(int qq = 1; qq <= t; qq++){
		cout << "Case #" << qq << ": ";
		cin >> s;
		string ans = "";
		while(find(s, "ZERO")){
			ans += "0";
		}
		while(find(s, "EIGHT")){
			ans += "8";
		}
		while(find(s, "SIX")){
			ans += "6";
		}
		while(find(s, "FOUR")){
			ans += "4";
		}
		while(find(s, "FIVE")){
			ans += "5";
		}
		while(find(s, "SEVEN")){
			ans += "7";
		}
		while(find(s, "TWO")){
			ans += "2";
		}
		while(find(s, "NINE")){
			ans += "9";
		}
		while(find(s, "ONE")){
			ans += "1";
		}
		while(find(s, "THREE")){
			ans += "3";
		}
		sort(ans.begin(), ans.end());
		cout << ans;
		cout << "\n";
	}
}