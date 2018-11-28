#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <locale>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <climits>
#include <cfloat>
#include <map>
using namespace std;
const double PI = acos(0.0) * 2.0;

int rowIdxFirst, rowIdxSecond, arr1[16][16], arr2[16][16];
FILE *ipt, *opt;

int main() // Google Code Jam 2014 Problem A. Magic Trick
{
	ipt = fopen("A-small-attempt1.in", "r");
	opt = fopen("output.out", "w");

	int tc_N;
	fscanf(ipt, "%d", &tc_N);

	for (int tc = 0; tc < tc_N; tc++)
	{
		fscanf(ipt, "%d", &rowIdxFirst);

		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) fscanf(ipt, "%d", &arr1[i][j]);

		fscanf(ipt, "%d", &rowIdxSecond);

		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) fscanf(ipt, "%d", &arr2[i][j]);

		int canAns_N = 0, ans; // 답이 될 수 있는 카드 개수, 답인 카드

		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		if (arr1[rowIdxFirst - 1][i] == arr2[rowIdxSecond - 1][j])
		{
			canAns_N++;
			ans = arr1[rowIdxFirst - 1][i];
			break;
		}

		fprintf(opt, "Case #%d: ", tc + 1);

		switch (canAns_N)
		{
		case 0: fprintf(opt, "Volunteer cheated!\n");
			break;
		case 1: fprintf(opt, "%d\n", ans);
			break;
		default: fprintf(opt, "Bad magician!\n");
			break;
		}
	}

	fclose(ipt);
	fclose(opt);

	return 0;
}



