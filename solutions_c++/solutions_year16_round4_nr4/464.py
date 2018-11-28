#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <complex>
#include <queue>
#include <cstdlib>
#include <ctime>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()

string str[222];

bool check(int p, vector<int> &perm, int mask, int wtf) {
	if(p == sz(perm)) return true;
	bool ok = false;
	for(int i = 0; i < sz(perm); i++) {
		bool omg = false;
		int idx = perm[p] * sz(perm) + i;
		if(wtf & (1 << idx)) omg = true;
		if((str[perm[p]][i] == '1' || omg) && (mask & (1 << i))) {
			ok = true;
			if(!check(p+1,perm,mask^(1<<i), wtf)) return false;
		}
	}
	return ok;
}

bool solve(int N, int mask) {
	vector<int> perm;
	for(int i = 0; i < N; i++) perm.pb(i);
	do {
		if(!check(0, perm, (1 << N) - 1, mask)) {
			return false;
		}
	} while(next_permutation(perm.begin(), perm.end()));
	return true;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int T;
	scanf("%d", &T);
	for(int test = 1; test <= T; test++) {
		printf("Case #%d: ", test);
		int N;
		scanf("%d", &N);
		for(int i = 0; i < N; i++) cin >> str[i];
		int res = N * N;
		for(int mask = 0; mask < (1 << (N*N)); mask++) {
			int cnt = 0;
			for(int i = 0; i < N * N; i++) {
				int r = i / N;
				int c = i % N;
				if(str[r][c] == '1') {
					if(mask & (1 << i)) {
						// ok
					}
					else {
						// bad 
						cnt = 1e9;
					}
				}
				else {
					if(mask & (1 << i)) {
						cnt++;
					}
					else {
						// ok
					}
				}
			}
			if(cnt < res && solve(N, mask)) res = cnt;
		}
		cout << res << endl;
	}

	return 0;
}