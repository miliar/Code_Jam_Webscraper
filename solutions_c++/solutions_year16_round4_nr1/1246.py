#include <bits/stdc++.h>
using namespace std;
#define M_PI        3.14159265358979323846

typedef long long ll;
typedef long double ld;
const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 1e9 + 7;
const ld EPS = 1e-9;

string expand(string &s){
	string res;
	res.resize(s.size() * 2);
	for(int i = 0; i < (int)s.size(); i++){
		switch(s[i]){
		case 'R':
			res[i*2] = 'R';
			res[i*2+1] = 'S';
			break;
		case 'P':
			res[i*2] = 'P';
			res[i*2+1] = 'R';
			break;
		case 'S':
			res[i*2] = 'P';
			res[i*2+1] = 'S';
		}
	}
	cerr << s << " " << res << "\n";
	return res;
}

array<int, 3> expand(array<int, 3> first){
	array<int, 3> rs = {0, 0, 0}; // P, R, S
	for(int i = 0; i < 3; i++){
		rs[i] += first[i];
		rs[i + 1 == 3 ? 0 : i + 1] += first[i];
	}
	return rs;
}

int main() {
	ios_base::sync_with_stdio(false);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
//	freopen("isomorphism.in", "r", stdin);
//	freopen("isomorphism.out", "w", stdout);
#endif
	// PR->P
	// PS->S
	// RS->R
	string rs[15][150];
	rs[0]['R'] = "R";
	rs[0]['S'] = "S";
	rs[0]['P'] = "P";
	vector<pair<char, string> > vc = {{'R', "RS"}, {'S', "PS"}, {'P', "PR"}};
	for(int i = 1; i <= 12; i++){
		for(int j = 0; j < 3; j++){
			string s1 = rs[i-1][(int)vc[j].second[0]] + rs[i-1][(int)vc[j].second[1]];
			string s2 = rs[i-1][(int)vc[j].second[1]] + rs[i-1][(int)vc[j].second[0]];
			rs[i][(int)vc[j].first] = min(s1, s2);
		}
	}
	int caseall;
	cin >> caseall;
	array<int, 3> rk;
	for(int casenum = 1; casenum <= caseall; casenum++){
		cout << "Case #" << casenum << ": ";
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		rk = {1, 0, 0};// P, R, S
		for(int i = 0; i < n; i++){
			rk = expand(rk);
		}
		if(rk[0] == p && rk[1] == r && rk[2] == s){
			string ss = rs[n]['P'];
			cout << ss << "\n";
			continue;
		}
		rk = {0, 1, 0};// P, R, S
		for(int i = 0; i < n; i++){
			rk = expand(rk);
		}
		if(rk[0] == p && rk[1] == r && rk[2] == s){
			string ss = rs[n]['R'];
			cout << ss << "\n";
			continue;
		}
		rk = {0, 0, 1};// P, R, S
		for(int i = 0; i < n; i++){
			rk = expand(rk);
		}
		if(rk[0] == p && rk[1] == r && rk[2] == s){
			string ss = rs[n]['S'];
			cout << ss << "\n";
			continue;
		}
		cout << "IMPOSSIBLE\n";
	}
	return 0;
}
