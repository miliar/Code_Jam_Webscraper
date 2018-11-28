#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
#define sz(a) (int)a.size()
#define pb push_back
const int MAXN = 35 * 1000;
const double EPS = 1e-9;
typedef long long LL;

bool validate(vector<vector<char> > &a, vector<int> &order, int mask = 0, int pos = 0){
	if (pos == a.size()){
		return true;
	}

	int emp = order[pos];
	bool result = true;

	bool any = false;

	for (int i = 0; i < a[emp].size(); ++i){
		if (a[emp][i] == 0) continue;
		int machine = i;
		if (mask&(1 << machine))continue;
		any = true;
		result &= validate(a, order, mask | (1 << machine), pos + 1);
		if (!result) return false;
	}

	if (!any) return false;
	return true;
}

bool possible(vector<vector<char> > &a){
	vector<int> order(a.size());
	for (int i = 0; i < order.size(); ++i)order[i] = i;

	bool result = true;

	for (int i = 0; i < 30; ++i){
		result &= validate(a, order);
		if (!result) return false;
		next_permutation(all(order));
	}

	return result;
}

int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("numbers.in", "r", stdin); freopen("numbers.out", "w", stdout);
#endif
	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt){
		int ans = 1000;

		int n; cin >> n;
		vector<vector<int> > a(n, vector<int>(n));
		forn(i, 0, n){
			forn(j, 0, n){
				char t;
				cin >> t;
				a[i][j] = t - '0';
			}
		}

		for (int i = 0; i < (1 << (n*n)); ++i){
			vector<vector<char> > tmp(n,vector<char>(n));

			for (int j = 0; j < (n*n); ++j){
				if (i&(1 << j)){
					tmp[j / n][j%n] = 1;
				}
			}


			int need = 0;
			for (int i1 = 0; i1 < a.size(); ++i1){
				if (need == -1) break;
				for (int j1 = 0; j1 < a.size(); ++j1){
					if (a[i1][j1] == 1 && tmp[i1][j1] == 0){
						need = -1;
						break;
					}

					if (a[i1][j1] == 0 && tmp[i1][j1] == 1){
						need++;
					}
				}
			}

			if (need == -1) continue;
			if (possible(tmp)){
				ans = min(ans, need);
			}
		}

		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}
