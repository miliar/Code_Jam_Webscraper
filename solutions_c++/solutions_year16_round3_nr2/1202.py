#include <fstream>
#include <iostream>
#include <string>
#include <vector> 
using namespace std;

vector<vector<int> > g;


int count(int B) {
	vector<int> dp(B, 0);	
	dp[0] = 1;
	for (int v = 1; v < B; ++v) {
		for (int i = 0; i < v; ++i) {
			if (g[i][v]) {
				dp[v] += dp[i];
			}
		}
	}
	return dp[B - 1];
}

string show(int B) {
	string res = "";
	for (int i = 0; i < B; ++i) {
		for (int j = 0; j < B; ++j) {
			if (g[i][j]) res += "1";
			else res += "0";
		}
		res += "\n";
	}
	return res;
}

void getPos(int B, int mask, int &k, int&l) {
	int index = 0;
	for (int k1 = 0; k1 < B; ++k1) {
		for (int l1 = k1 + 1; l1 < B; ++l1) {
			if (index == mask) {
				k = k1; 
				l = l1;
			}
			index ++;
		}
	}
}

string solve(int B, int M) {
	for (int mask = 0; mask < (1 << ((B - 1) * B / 2)); ++mask) {
		g.clear();

		g.resize(B);
		for (int i = 0; i < g.size(); ++i) {
			g[i].resize(B);
		}

		
		for (int j = 0; j < (B * (B - 1) / 2); ++j) {
			if (((1 << j) & mask) > 0) {
				int k, l;
				getPos(B, j, k, l);
				g[k][l] = 1;
			}	
		}
		int res = count(B);
		//cout << show(B);
		if (res == M) {
			return "POSSIBLE\n" + show(B);
		}
	}
	return "IMPOSSIBLE\n";
}

int main() {
	ifstream fin("input.txt");
	ofstream fout ("result.txt");
	int T;
	fin >> T;
	for (int t = 1; t <= T; ++t) {
		int B, M;
		fin >> B >> M;
		fout << "Case #" << t << ": " << solve(B, M);
	}
	return 0;
}