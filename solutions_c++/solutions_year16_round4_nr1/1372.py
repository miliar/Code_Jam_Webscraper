# include <bits/stdc++.h>
using namespace std;

string build(string s)
{
	string ans;
	for(int i=0; i<s.size(); ++i) {
		if (i % 2 == 0) {
			if (s[i] == 'R' && s[i+1] == 'S') {
				swap(s[i], s[i+1]);
			}
		}
		
		if (s[i] == 'P') {
			ans += "PR";
		}
		else if (s[i] == 'R') {
			ans += "RS";
		}
		else {
			ans += "PS";
		}
	}
	
	return ans;
}

typedef struct _G {
	int p, r, s;
} G;

int main()
{	
	vector<vector<string>> ans(13);
	ans[1] = {"PR", "RS", "PS"};
	
	map<string, string> dp;
	dp["P"] = "PR";
	dp["R"] = "RS";
	dp["S"] = "PS";
	
	queue<string> que; 
	que.push("PR"), que.push("RS"), que.push("PS");
	
	while(!que.empty()) {
		string s = que.front(); que.pop();
		string s1 = s.substr(0, s.size()/2);
		string s2 = s.substr(s.size()/2, s.size()/2);
		string ns = min(dp[s1] + dp[s2], dp[s2] + dp[s1]);
		dp[s] = ns;
		
		int p = log2(ns.size());
		ans[p].push_back(ns);
		
		if (p < 12) que.push(ns);
	}

	vector<vector<G>> nans(13);
	for(int i=1; i<=12; ++i) {
		for(int k=0; k<3; ++k) {
			G t = {0, 0, 0};
			for(int p=0; p<ans[i][k].size(); ++p) {
				if (ans[i][k][p] == 'R') t.r += 1;
				else if (ans[i][k][p] == 'P') t.p += 1;
				else t.s += 1;
			}
			nans[i].push_back(t);
		}
	}
	
	int T; cin >> T;
	for(int T_=1; T_<=T; ++T_) {
		int n, r, p, s; cin >> n >> r >> p >> s;
		
		printf("Case #%d: ", T_);
		
		vector<string> v;
		for(int i=0; i<3; ++i) {
			if (nans[n][i].r == r && nans[n][i].p == p && nans[n][i].s == s) {
				v.push_back(ans[n][i]);
			}
		}
		if (v.empty()) printf("IMPOSSIBLE\n");
		else {
			for(int i=1; i<v.size(); ++i) {
				if (v[i] < v[0]) swap(v[0], v[i]);
			}
			printf("%s\n", v[0].c_str());
		}
	}
	return 0;
}