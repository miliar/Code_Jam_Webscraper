#include<bits/stdc++.h>
using namespace std;


int cal(const string& s) {
	const int n = s.length();
/*	static int f[20000][20001];
	for(int i = 0; i < n; ++i)
		f[i][i] = 0;
	for(int d = 2; d <= n; d += 2) {
#		pragma omp parallel for
		for(int l = 0, r = d; l + d <=n ; ++l, ++r) {
			f[l][r] = f[l+1][r-1] + (s[l]==s[r-1] ? 10: 5);
			for(int k = l+2; k < r; k+=2)
				f[l][r] = max(f[l][r], f[l][k] + f[k][r]);
		}
	} */
	int res = 0;
	string tmp;
	for(int r = n, i = 0; r >= 1; --r, ++i) {
		if(tmp.length() == r || tmp.length() && tmp.back() == s[i]) {
			res += tmp.back() == s[i] ? 10 : 5;
			tmp.pop_back();
		} else tmp += s[i];
	}
	//assert(res == f[0][n]);
	return res;
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << i << ": "<< cal(s) << endl;
	}
}
