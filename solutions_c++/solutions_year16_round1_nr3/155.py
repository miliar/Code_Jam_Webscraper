#include <bits/stdc++.h>
using namespace std;

int bff[2000];
vector<int> zzz[2000];
int c[2000];
int n;

int iii;
int cycle(int v, int d) {
	if(v == iii && d > 0) return d;
	int res = 0;
	for(int i = 0; i < (int)zzz[v].size(); i++) {
		int w = zzz[v][i];
		res = max(res, cycle(w, d+1));
	}
	return res;
}

int chain(int v, int d) {
	int res = 0;
	for(int i = 0; i < (int)zzz[v].size(); i++) {
		int w = zzz[v][i];
		if(w != bff[v]) res = max(res, chain(w, d+1));
	}
	return res + 1;
}

int main() {
	ios_base::sync_with_stdio(0);
	int _;
	cin >> _;
	for(int __ = 0; __ < _;) {
		cout << "Case #" << ++__ << ": ";
		cin >> n;
		for(int i = 1; i <= n; i++) zzz[i].clear();
		int ans = 0;
		for(int i = 1; i <= n; i++) {
			cin >> bff[i];
			zzz[bff[i]].push_back(i);
		}
		for(int i = 1; i <= n; i++) {
			int k = 0;
			iii = i;
			k = cycle(i, 0);
//			cerr << i << " " << k << "\n";
			ans = max(ans, k);
			c[i] = k;
		}	
		int ans2 = 0;
		for(int i = 1; i <= n; i++) {
			if(c[i] == 2) {
//				cerr << i << " " << chain(i, 0) << "\n";
				ans2 += chain(i, 0);	
			}
		}		
		cout << max(ans, ans2) << "\n";
	}	
	return 0;
}
