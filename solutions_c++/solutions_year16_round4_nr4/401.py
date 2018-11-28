/*
ID: ashish1610
PROG:
LANG: C++
*/
#include<bits/stdc++.h>
using namespace std;
#define ll				long long int
#define MOD				1000000007
#define si(a)			scanf("%d", &a)
#define sl(a)			scanf("%lld", &a)
#define pi(a)			printf("%d", a)
#define pl(a)			printf("%lld", a)
#define pn 				printf("\n")
ll pow_mod(ll a, ll b) {
	ll res = 1;
	while(b) {
		if(b & 1) {
			res = (res * a) % MOD;
		}
		a = (a * a) % MOD;
		b >>= 1;
	}
	return res;
}
bool can_op[5][5];
int func(int worker_mask, int machine_mask, int n) {
	int res = INT_MAX;
	for(int i = 0; i < n; ++i) {
		if(!(worker_mask & (1 << i))) {
			for(int j = 0; j < n; ++j) {
				if(!(machine_mask & (1 << j))) {
					if(can_op[i][j]) {
						res = min(res, 1 + func(worker_mask | (1 << i), machine_mask | (1 << j), n));
					}
				}
			}
		}
	}
	if(res == INT_MAX) {
		return 0;
	} else {
		return res;	
	}
}
int solve(vector < pair < int, int > > v, int n) {
	int n1 = (int)(v.size());
	int res = n1;
	for(int i = 0; i < (1 << n1); ++i) {
		for(int j = 0; j < n1; ++j) {
			if(i & (1 << j)) {
				can_op[v[j].first][v[j].second] = true;
			}
		}
		if(func(0, 0, n) == n) {
			res = min(res, __builtin_popcount(i));
		}
		for(int j = 0; j < n1; ++j) {
			if(i & (1 << j)) {
				can_op[v[j].first][v[j].second] = false;
			}
		}
	}
	return res;
}
int main() {
	int t;
	cin >> t;
	for(int tcase = 1; tcase <= t; ++tcase) {
		int n;
		cin >> n;
		char ch;
		memset(can_op, false, sizeof(can_op));
		vector < pair < int, int > > v;
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j) {
				cin >> ch;
				if(ch == '1') {
					can_op[i][j] = true;
				} else {
					v.push_back(make_pair(i, j));
				}
			}
		}
		cout << "Case #" << tcase << ": ";
		cout << solve(v, n) << endl;
	}
	return 0;
}