#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

int N;
int map[25][25];

void input()
{
	char line[32];
	cin >> N;
	for (int i=0;i<N;++i) {
		cin >> line;
		for (int j=0;j<N;++j) map[i][j] = (line[j]=='1'?1:0);
	}
}

int validx(int x) {
	int cnt = 0;
	for (int i=0;i<N;++i) {
		bool match = 1;
		for (int j=0;j<N;++j) {
			if (map[i][j] != map[x][j]) match = 0;
		}
		if (match == 1) ++cnt;
	}
	return cnt;
}

int validy(int y) {
	int cnt = 0;
	for (int i=0;i<N;++i) {
		bool match = 1;
		for (int j=0;j<N;++j) {
			if (map[j][i] != map[j][y]) match = 0;
		}
		if (match == 1) ++cnt;
	}
	return cnt;
}

bool valid()
{
	for (int i=0;i<N;++i) {
		int cnt = 0;
		for(int j=0;j<N;++j) {
			if (map[i][j]) ++ cnt;
		}
		if (cnt == 0) return false;
		if (cnt != validx(i)) return false;
	}
	
	for (int i=0;i<N;++i) {
		int cnt = 0;
		for(int j=0;j<N;++j) {
			if (map[j][i]) ++ cnt;
		}
		if (cnt == 0) return false;
		if (cnt != validy(i)) return false;
	}
	
	return true;
}

int count(int x) {
	int cnt = 0;
	for (int i=0;i<(N*N);++i) {
		if (x & (1<<i)) ++cnt;
	}
	return cnt;
}

bool set_it(int X) {
	for (int i=0;i<N*N;++i) {
		if (X & (1 << i)) {
			int x = i / N;
			int y = i % N;
			if (map[x][y]) return false;
		}
	}
	for (int i=0;i<N*N;++i) {
		if (X & (1 << i)) {
			int x = i / N;
			int y = i % N;
			map[x][y] = 1;
		}
	}
	return true;
}

void unset_it(int X) {
	for (int i=0;i<N*N;++i) {
		if (X & (1 << i)) {
			int x = i / N;
			int y = i % N;
			map[x][y] = 0;
		}
	}
}

void dump()
{
	for (int i=0;i<N;++i) {
		for (int j=0;j<N;++j) {
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}
	printf("===\n");
}

int solv()
{
	int ans = N*N;
	for (int i=0;i<(1<<(N*N)); ++i) {
		if (!set_it(i)) {
			continue;
		}
//		printf("i = %d\n", i);
//		dump();
		if (valid()) {
			int cost = count(i);
			if (cost < ans) ans = cost;
//			printf("===%d\n", i);
		}
		unset_it(i);
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int nCase = 1; nCase <= T; ++nCase) {
		input();
		printf("Case #%d: %d\n", nCase, solv());
	}
	return 0;
}
