#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <set>
#define FOR0(n) for(int i = 0; i < (int)n; ++i)
#define FOR1(n) for(int i = 1; i <= (int)n; ++i)

using namespace std;

int mas[20];
int grid[20][20];
int minim = 1000000, r, c;

void grid_clear(){
	for (int i = 0; i < 20; ++i)
	for (int j = 0; j < 20; ++j)
		grid[i][j] = 0;
}

void calc_min(){
	int k = 0, ans = 0;
	for (int i = 1; i <= r; ++i)
		for (int j = 1; j <= c; ++j)
			grid[i][j] = mas[k++];
	for (int i = 1; i <= r; ++i)
		for (int j = 1; j <= c; ++j)
		if (grid[i][j]){
			if (grid[i + 1][j]) ++ans;
			if (grid[i - 1][j]) ++ans;
			if (grid[i][j + 1]) ++ans;
			if (grid[i][j - 1]) ++ans;
		}
	minim = min(ans, minim);
}

void brf(int tot, int n, int s){
	if (s + n > tot) return;
	if (n == 0){
		calc_min();
		return;
	}
	for (int i = s; i < tot; ++i){
		mas[i] = 1;
		brf(tot, n - 1, i + 1);
		mas[i] = 0;
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	ifstream inf("B-small-attempt0.in");
	ofstream outf("output.txt");
	int t;
	inf >> t;
	for (int i = 0; i < t; ++i){
		int n;
		inf >> r >> c >> n;
		minim = 1000000;
		grid_clear();
		brf(r*c, n, 0);
		outf << "Case #" << i + 1 << ": " << minim/2 << '\n';
	}
	inf.close();
	outf.close();
}