#include <bits/stdc++.h>

using namespace std;

#define INF 1<<30
#define MOD 1000000007
typedef long long ll;
#define fori(i, ini, lim) for(int i= int(ini); i<(int)lim; ++i)
#define ford(i, ini, lim) for(int i= int(ini); i>=(int)lim; --i)

map<int, string> m;
int hist[30];

int take(char id, int idx){
	int cur = hist[id - 'A'];
	while(hist[id - 'A'] > 0){
		fori(i, 0, m[idx].size()){
			hist[m[idx][i] - 'A']--;
		}
	}
	return cur;
}

int main(){
	m[0] = "ZERO";
	m[1] = "ONE";
	m[2] = "TWO";
	m[3] = "THREE";
	m[4] = "FOUR";
	m[5] = "FIVE";
	m[6] = "SIX";
	m[7] = "SEVEN";
	m[8] = "EIGHT";
	m[9] = "NINE";

	int t; cin >> t;
	int cases = 1;
	while(t--){
		memset(hist, 0, sizeof(hist));
		string s; cin >> s;
		fori(i, 0, s.size()){
			hist[s[i] - 'A']++;
		}
		string ans = "";
		int cur = take('Z', 0);
		fori(i, 0, cur) ans += '0';
		cur = take('W', 2);
		fori(i, 0, cur) ans += '2';
		cur = take('U', 4);
		fori(i, 0, cur) ans += '4';
		cur = take('X', 6);
		fori(i, 0, cur) ans += '6';
		cur = take('G', 8);
		fori(i, 0, cur) ans += '8';
		cur = take('R', 3);
		fori(i, 0, cur) ans += '3';
		cur = take('O', 1);
		fori(i, 0, cur) ans += '1';
		cur = take('F', 5);
		fori(i, 0, cur) ans += '5';
		cur = take('S', 7);
		fori(i, 0, cur) ans += '7';
		cur = take('E', 9);
		fori(i, 0, cur) ans += '9';
		sort(ans.begin(), ans.end());
		cout << "Case #" << cases++ << ": ";
		cout << ans << endl;
	}

	return 0;
}
