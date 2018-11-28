#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int Test, N, M, R, C, ans[10][10];

int main(int argc, char **argv)
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	ans[2][3] = 2;
	ans[2][4] = 1;
	ans[2][5] = 1;
	ans[2][6] = 3;
	ans[3][3] = 2;
	ans[3][4] = 3;
	ans[3][5] = 2;
	ans[3][6] = 2;
	ans[4][3] = 3;
	ans[4][4] = 1;
	ans[4][5] = 1;
	ans[4][6] = 5;
	ans[5][3] = 3;
	ans[5][4] = 3;
	ans[5][5] = 1;
	ans[5][6] = 5;
	ans[6][3] = 6;
	ans[6][4] = 4;
	ans[6][5] = 2;
	ans[6][6] = 19;
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%d%d", &R, &C);
		printf("Case #%d: %d\n", Case, ans[R][C]);
	}
	return 0;
}
