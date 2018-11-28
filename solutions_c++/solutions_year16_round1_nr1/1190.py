#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long ll;
string solve(){
	string s;
	cin >> s;
	char fl = s[0], sl = '?';
	string ans(1,s[0]);
	for(int i = 1; i < s.size(); ++i){
		if(s[i] > fl){
			ans = string(1,s[i]) + ans;
			sl = fl;
			fl = s[i];
		}
		else if(s[i] == fl && (sl == '?' || sl < s[i])){
			ans = string(1,s[i]) + ans;
		}
		else{
			ans = ans + string(1,s[i]);
			if(sl == '?' && s[i]!=fl)
				sl = s[i];
		}
	}
	return ans;
}
int main(){
	int T;
	cin >> T;
	for(int tc = 1; tc <= T; ++tc){
		cout << "Case #" << tc << ": " << solve() << '\n';
	}
}

