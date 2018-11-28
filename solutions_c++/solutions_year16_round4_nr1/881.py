										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int cnt[15][5][3];
string ans[15][5];

int main(){
	freopen("A-Rather Perplexing Showdown.in", "r", stdin);
	freopen("A-Rather Perplexing Showdown.out", "w", stdout);

	ans[0][0] = "P";
	ans[0][1] = "R";
	ans[0][2] = "S";
	cnt[0][0][0] = 1;
	cnt[0][1][1] = 1;
	cnt[0][2][2] = 1;
	for(int i = 1; i <= 14; i++){
		for(int j = 0; j < 3; j++){
			int k = (j + 1) % 3;
			for(int x = 0; x < 3; x++)
				cnt[i][j][x] = cnt[i - 1][j][x] + cnt[i - 1][k][x];
			if(ans[i - 1][j] < ans[i - 1][k])
				ans[i][j] = ans[i - 1][j] + ans[i - 1][k];
			else ans[i][j] = ans[i - 1][k] + ans[i - 1][j];
		}
	}
	int T, test = 0;
	int n, p[3];
	for(cin >> T; T--; ){
		cout << "Case #" << ++test << ": ";
		cin >> n >> p[1] >> p[0] >> p[2];
		bool can = false;
		for(int i = 0; i < 3 && !can; i++){
			bool ok = true;
			for(int j = 0; j < 3; j++)
				if(cnt[n][i][j] != p[j])
					ok = false;
			if(ok){
				can = true;
				cout << ans[n][i] << endl;
			}
		}
		if(!can) cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
