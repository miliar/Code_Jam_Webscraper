#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;


int k, n;
int keys[201];
int chests[21][201];
int needed[21];

void Load()
{
	cin >> k >> n;
	memset(keys, 0, sizeof(keys));
	int i, j, l;
	for (i = 0; i < k; i++) {
		cin >> j;
		keys[j]++;
	}
	memset(chests, 0, sizeof(chests));
	for (i = 0; i < n; i++) {
		cin >> j >> l;
		needed[i] = j;
		for (int z = 0; z < l; z++) {
			cin >> j;
			chests[i][j]++;
		}
	}
}


int dp[1<<20];



bool Can(int m) {
	if(dp[m] != 0) return dp[m] != -1;
	if (m == 0) return true;
	int i, j;
	int s = 201;
	vector<int> cur;
	cur.resize(s);
	for (i = 0; i < s; i++) cur[i] = keys[i];
	for (j = 0; j < n; j++) {
		if (((1 << j) & m) != 0) continue;
		cur[needed[j]]--;
		for (i = 0; i < s; i++)
			cur[i] += chests[j][i];
	}
	for (j = 0; j < n; j++) {
		if (((1 << j) & m) != 0) {
			if (cur[needed[j]] > 0) {
				int nm = m ^ (1 << j);
				if (Can(nm)) {
					dp[m] = j+1;
					return true;
				}
			}
		}
	}
	dp[m] = -1;
	return false;
}

void Solve()
{
	int i;
	memset(dp, 0, sizeof(dp));
	if (!Can((1<<n) -1 )) cout << " IMPOSSIBLE\n";
	else {
		vector<int> ans;
		i = (1 << n) - 1;
		while (i > 0) {
			ans.push_back(dp[i]);
			i ^= (1 << (dp[i]-1));
		}
		for (i = 0; i < n; i++)
			cout << ' ' << ans[i];
		cout << "\n";
	}
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ":";
		Load();
		Solve(); 
	}
	return 0;
}
