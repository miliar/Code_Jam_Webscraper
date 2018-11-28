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


int p, r, s;
int n;

void Load()
{
	cin >> n >> r >> p >> s;
}

int cnt[20][3][3];
string ans[20][3];

void Solve()
{
	string ss = "Z";
	int j;
	for (j = 0; j < 3; j++) {
		if (cnt[n][j][0] == p && cnt[n][j][1] == r && cnt[n][j][2] == s) {
			if (ss > ans[n][j])
				ss = ans[n][j];
		}
	}
	if (ss == "Z") cout << "IMPOSSIBLE\n";
	else cout << ss << "\n";
}

void Fill()
{
	int i, w, j;
	ans[0][0] = "P"; ans[0][1] = "R"; ans[0][2] = "S";
	cnt[0][0][0] = cnt[0][1][1] = cnt[0][2][2] = 1;
	for (i = 1; i <= 13; i++) {
		for (w = 0; w < 3; w++) {
			if (ans[i-1][w] < ans[i-1][(w+1) % 3])
				ans[i][w] = ans[i-1][w] + ans[i-1][(w+1)%3];
			else
				ans[i][w] = ans[i-1][(w+1)%3] + ans[i-1][w];
			for (j = 0; j < 3; j++) {
				cnt[i][w][j] = cnt[i-1][w][j] + cnt[i-1][(w+1)%3][j];
			}
		}
	}
}

int main()
{
	Fill();
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
