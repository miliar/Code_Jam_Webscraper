#include <iostream>
#include <fstream>
#include <algorithm>

int t;
int d;
int p[7];

int upper(int val, int g) {
	if (val % g)
		return val / g + 1;
	return val / g;
}

int res;

void dfs(int k, int max, int add) {
	if (k == d + 1) {
		if (res == -1 || max + add < res)
			res = max + add;
		return;
	}
	for (int g = 1; g <= p[k]; g++)
		dfs(k + 1, std::max(max, upper(p[k], g)), add + g - 1);
}

int main() {
	std::ifstream fin("B-small-attempt0.in");
	std::ofstream fout("output.out");
	fin >> t;
	for (int i = 1; i <= t; i++) {
		fin >> d;
		for (int j = 1; j <= d; j++)
			fin >> p[j];
		res = -1;
		dfs(1, 0, 0);
		fout << "Case #" << i << ": " << res << std::endl;
	}
	return 0;
}