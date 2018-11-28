#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>
#include <stack>
#include <cassert>
#include <unordered_map>

using namespace std;

vector<string> In = {"PR", "PS", "RS"};
unordered_map<char, string> M;

string solve(const string & t, int N, int R, int P, int S) {
	if (N == 1) {
		for (int i = 0 ; i < t.size() ; ++i) {
			if (t[i] == 'P') P--;
			if (t[i] == 'R') R--;
			if (t[i] == 'S') S--;
 		}
		if (P < 0 || R < 0 || S < 0) return "";
		return t;
	}
	
	string next = "";
	for (int i = 0 ; i < t.size() ; ++i) {
		next += M[t[i]];
	}
	return solve(next, N-1, R, P, S);
}

string fix(const string & x, int L) {
	assert(x.size() == 2 * L);
	string a = x.substr(0, L);
	string b = x.substr(L, L);
	if (a < b) return a + b;
	return b + a;
}

string fix(string x) {
	for (int l = 2 ; l * 2 <= x.size() ; l *= 2) {
		for (int i = 0 ; i < x.size() ; i += l * 2) {
			string sx = x.substr(i, l * 2);
			string fx = fix(sx, l);
			x.replace(i, l*2, fx);
		}
	}
	return x;
}

string solve(int N, int R, int P, int S) {
	vector<string> sol;
	for (int i = 0 ; i < In.size() ; ++i) {
		auto x = solve(In[i], N, R, P, S);
		if (x.size() > 0) {
			x = fix(x);
			sol.push_back(x);
		}
	}
	if (sol.empty()) return "IMPOSSIBLE";
	sort(sol.begin(), sol.end());
	return sol.front();
}

int main(){
	int tcase;
	cin >> tcase;
	M.emplace('P', "PR");
	M.emplace('S', "PS");
	M.emplace('R', "RS");
	int N, R, P, S;
	
	for(size_t casen = 0; casen < tcase; ++casen)
	{
		cin >> N >> R >> P >> S;
		cout << "Case #" << casen + 1 << ": ";
		cout << solve(N, R, P, S) << endl;
	}
	

	return 0;
}
