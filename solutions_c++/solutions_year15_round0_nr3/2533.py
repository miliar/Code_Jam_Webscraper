#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <assert.h>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <functional>

#include <Windows.h>

using namespace std;

const int MX = 10010;
int dp[MX][MX];

int mp[5][5];
map<char, int> toi; 

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	mp[1][1] = 1; mp[1][2] = 2; mp[1][3] = 3; mp[1][4] = 4;
	mp[2][1] = 2; mp[2][2] = -1; mp[2][3] = 4; mp[2][4] = -3;
	mp[3][1] = 3; mp[3][2] = -4; mp[3][3] = -1; mp[3][4] = 2;
	mp[4][1] = 4; mp[4][2] = 3; mp[4][3] = -2; mp[4][4] = -1;

	toi['1'] = 1; toi['i'] = 2; toi['j'] = 3; toi['k'] = 4; 

	int TC = 0;
	inf >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		int k, l; string s;
		inf >> k >> l >>s;
		
		string str;
		for (int i = 0; i < l; i++) str += s;
		l *= k; 
		memset(dp, 0, sizeof(dp));

		for (int i = 1; i <= l; i++) dp[i][i] = toi[str[i - 1]]; 
		for (int step = 2; step <= l; step++) {
			for (int i = 1; i <= (l - step + 1); i++) {
				int sign1 = 1, sign2 = 1;
				int val1 = dp[i][i + step - 2], val2 = dp[i + step - 1][i + step - 1];
				if (val1 < 0) {
					sign1 = -1; val1 *= -1;
				}
				if (val2 < 0) {
					sign2 = -1; val2 *= -1;
				}

				dp[i][i + step - 1] = mp[val1][val2] * sign1 * sign2;
			}
		}

		bool possible = false;
		for (int i = 1; i < l; i++) {
			if (dp[1][i] != 2) continue;
			for (int j = i + 1; j < l; j++) {
				if (dp[i + 1][j] != 3 || dp[j+1][l] != 4) continue;
				possible = true;
			}
		}

		if (possible)
			cout << "Case #" << tc << ": " << "YES" << endl;
		else
			cout << "Case #" << tc << ": " << "NO" << endl;
	}

	return 0; 
}