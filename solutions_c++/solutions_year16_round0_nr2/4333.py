#include <iostream>
#include <cstdio>
#include <string>
#include <hash_map>

using namespace std;

int T, ans;
string s;
hash_map<string, int> uniq;

bool check (string & s){
	for (int i = 0; i < s.length(); ++i){
		if (s[i] != '+'){
			return false;
		}
	}
	return true;
}

string ret(string s, int i){
	string w = s.substr(0, i + 1);
	for (int j = 0; j <= i; ++j){
		if (w[j] == '+'){
			s[j] = '-';
		} else {
			s[j] = '+';
		}
	}
	return s;
}

void iter(string s, int p){
	if (check(s)){
		ans = min(ans, p);
		return;
	}
	for (int i = 0; i < s.length(); ++i){
		string ns = ret(s, i);
		if (uniq.find(ns) == uniq.end() || p < uniq[ns]){
			uniq[ns] = p;
			iter(ns, p + 1);
		}
	}
}

void input(){
	cin >> s;
	ans = 1e9;
	uniq.clear();
	uniq[s] = 0;
}

void solve(){
	iter(s, 0);
}

void output(int t){
	printf ("Case #%d: ", t);
	printf ("%d\n", ans);
}

int main(){
	freopen("b.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i){
		input();
		solve();
		output(i);
	}
	return 0;
}