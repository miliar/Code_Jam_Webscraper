// PRS
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>


using namespace std;

int cnt[255];
bool ok = true;
string dfs(char win, int n) {
	if (n == 0)
		if (cnt[win] > 0) {
			cnt[win]--;
			return string(1, win);
		} else {ok = false; return "$";};
	if (win == 'P') {
		string s1 = dfs('P', n - 1);
		string s2 = dfs('R', n - 1);
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	}
	if (win == 'R') {
		string s1 = dfs('R', n - 1);
		string s2 = dfs('S', n - 1);
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	}
	if (win == 'S') {
		string s1 = dfs('S', n - 1);
		string s2 = dfs('P', n - 1);
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	}

}

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++){
		printf("Case #%d: ", cas);
		int n,r,p,s;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		
		vector<string> ss;
		string s1;

		cnt['R'] = r; cnt['P'] = p; cnt['S'] = s; ok  = true;
		s1 = dfs('P', n);
		if (ok) 
			ss.push_back(s1);
		cnt['R'] = r; cnt['P'] = p; cnt['S'] = s;ok  = true;
		s1 = dfs('R', n);
		if (ok) 
			ss.push_back(s1);
		cnt['R'] = r; cnt['P'] = p; cnt['S'] = s;ok  = true;
		s1 = dfs('S', n);
		if (ok) 
			ss.push_back(s1);
		if (ss.size() == 0)
			puts("IMPOSSIBLE");
		else {
			sort(ss.begin(), ss.end());
			cout << ss[0] << endl;
		}
	}
}