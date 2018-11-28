#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

#define pb push_back
#define mp make_pair

vector<char> symb;
vector< vector<int> > strs;

int solve(int n) {
	int ans = 0;
	bool ok = true;
	symb.resize(0);
	strs.assign(n, vector<int>());
	string s;
	cin >>s;
	s += '%';

	int ilst = 0;
	for(int i = 0; i < s.size(); i++) {
		if(i != 0 && s[i - 1] != s[i]) {
			symb.pb(s[i - 1]);
			strs[0].pb(i - ilst);
			ilst = i;
		}
	}

	for(int j = 1; j < n; j++) {
		cin >>s;
		s += '%';
		ilst = 0;
		int p = 0;
		for(int i = 0; i < s.size() && ok; i++) {
			if(i != 0 && s[i - 1] != s[i]) {
				if(p >= symb.size() || s[i - 1] != symb[p++]) {
					ok = false;
					break;
				}
				strs[j].pb(i - ilst);
				ilst = i;
			}
		}

		if(p != symb.size())
			ok = false;
	}

	if(!ok) return -1;

	for(int j = 0; j < symb.size(); j++) {
		int cs = 0;
		for(int i = 0; i < n; i++) {
			cs += strs[i][j];
		}
		int m = floor((double)cs / n + 0.5);

		for(int i = 0; i < n; i++) {
			ans += abs(strs[i][j] - m);
		}
	}

	return ans;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >>T;

	for(int t = 0; t < T; t++) {
		int A, B, K;
		int ans = 0;
		cin >>A >>B >>K;

		for(int a = 0; a < A; a++) {
			for(int b = 0; b < B; b++) {
				if((int)(a & b) < K) ans++;
			}
		}

		cout <<"Case #" <<t + 1 <<": " <<ans <<endl;
	}

	return 0;
}