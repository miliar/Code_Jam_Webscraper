#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int N, ret;
char S[20][20];
vector<int> A, B;
bool X[20], Y[20];

void dfs(int i)
{
	A.push_back(i);
	X[i] = true;
	for (int j = 0; j < N; j ++)
	if (S[i][j] == '1' && !Y[j]) {
		Y[j] = true;
		B.push_back(j);
		for (int k = 0; k < N; k ++)
		if (S[k][j] == '1' && !X[k]) {
			dfs(k);
		}
	}
}

bool check()
{
	memset(X, 0, sizeof(X));
	memset(Y, 0, sizeof(Y));
	for (int i = 0; i < N; i ++)
	if (!X[i]) {
		A.clear();
		B.clear();
		dfs(i);
		if (A.size() != B.size()) return false;
		for (int j = 0; j < A.size(); j ++) {
			for (int k = 0; k < B.size(); k ++)
			if (S[A[j]][B[k]] == '0') return false;
		}
	}
	return true;
}

void search(int x, int y, int z)
{
	if (z >= ret) return;
	if (x == N) {
		if (check()) ret = z;
	} else {
		if (y == N) {
			search(x + 1, 0, z);
		} else {
			if (S[x][y] == '0') {
				S[x][y] = '1';
				search(x, y + 1, z + 1);
				S[x][y] = '0';
			}
			search(x, y + 1, z);
		}
	}
}

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int test, nCase = 0;
	scanf("%d", &test);
	while (test --) {
		scanf("%d", &N);
		for (int i = 0; i < N; i ++) {
			scanf("%s", S[i]);
		}
		ret = 10000;
		search(0, 0, 0);
		printf("Case #%d: %d\n", ++ nCase, ret);
	}
	return 0;
}
