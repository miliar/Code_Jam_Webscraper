#define _CRT_SECURE_NO_WARNINGS
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
#include<array>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	char *d[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	array<int, 26> cnt[26];
	rep(i,10) {
		fill(all(cnt[i]), 0);
		for (int j = 0; d[i][j];j++) {
			cnt[i][d[i][j] - 'A']++;
		}
	}

	int T;
	cin >> T;
	rep(icase, T) {
		string str ,ans;
		cin >> str;
		array<int, 26> goal;
		fill(all(goal), 0);
		for (char c : str)goal[c - 'A']++;

		while (goal['Z'-'A']>0) {
			ans += '0';
			rep(i,26) {
				goal[i] -= cnt[0][i];
			}
		}
		while (goal['W' - 'A']>0) {
			ans += '2';
			rep(i, 26) {
				goal[i] -= cnt[2][i];
			}
		}
		while (goal['X' - 'A']>0) {
			ans += '6';
			rep(i, 26) {
				goal[i] -= cnt[6][i];
			}
		}
		while (goal['G' - 'A']>0) {
			ans += '8';
			rep(i, 26) {
				goal[i] -= cnt[8][i];
			}
		}
		while (goal['S' - 'A']>0) {
			ans += '7';
			rep(i, 26) {
				goal[i] -= cnt[7][i];
			}
		}
		while (goal['T' - 'A']>0) {
			ans += '3';
			rep(i, 26) {
				goal[i] -= cnt[3][i];
			}
		}
		while (goal['U' - 'A']>0) {
			ans += '4';
			rep(i, 26) {
				goal[i] -= cnt[4][i];
			}
		}
		while (goal['V' - 'A']>0) {
			ans += '5';
			rep(i, 26) {
				goal[i] -= cnt[5][i];
			}
		}
		while (goal['O' - 'A']>0) {
			ans += '1';
			rep(i, 26) {
				goal[i] -= cnt[1][i];
			}
		}
		while (goal['I' - 'A']>0) {
			ans += '9';
			rep(i, 26) {
				goal[i] -= cnt[9][i];
			}
		}


		sort(all(ans));
		cout << "Case #" << icase + 1 << ": "<< ans <<endl;
	}

	return 0;
}