#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int a[4][3] = 
{
	{1, 2, 3},
	{4, 3, 6},
	{7, 4, 1},
	{2, 5, 4}
};

short int dp[10001][10001];

int calc(const string& s, int i, int j)
{
	//cout << i << ' ' << j << endl;

	int res = 0;

	for(int k = i; k <= j; ++k) {
		int tmp = a[res & 3][s[k] - 'i'];
		res = tmp ^ (res & 4);
	}

	return res;
}

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {
		int L, X;
		cin >> L >> X;
		string s;
		cin >> s;

		string lx;
		for(int i = 0; i < X; ++i) {
			lx += s;
		}
		
		for(int i = 0; i < (int)lx.size() ; ++i) {
			dp[i][i] = a[0][lx[i] - 'i'];
			for(int j = i + 1; j < (int)lx.size();  ++j) {
				int tmp = a[dp[i][j - 1]&3][lx[j] - 'i'];
				dp[i][j] = tmp ^ (dp[i][j - 1] & 4);
			}
		}
		
		if(lx.size() < 3) {
			cout << "Case #" << t << ": NO" << endl;
			continue;
		}
		
		bool f = false;
		int prev = 1;
		for(int i = 0; i < (int)lx.size() - 2; ++i) {
			for(int j = i + 1; j < (int)lx.size() - 1; ++j) {
				//cout << calc(lx, 0, i) << ' ' << calc(lx, i + 1, j) << ' ' << calc(lx, j + 1, lx.size() - 1) << endl;
				if(dp[0][i] == 1 && dp[i+1][j] == 2 && dp[j + 1][lx.size() - 1] == 3) {
					f = true;
				}
			}
		}

		cout << "Case #" << t << ": " << (f ? "YES" : "NO") << endl;
	}
}
