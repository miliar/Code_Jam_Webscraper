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

FILE *ipt, *opt;
double cost, extraCk_N, goal;

int main() // Google Code Jam 2014 Problem B. Cookie Clicker Alpha
{
	ipt = fopen("B-large.in", "r");
	opt = fopen("output.out", "w");

	int tc_N;
	fscanf(ipt, "%d", &tc_N);

	for (int tc = 0; tc < tc_N; tc++)
	{
		fscanf(ipt, "%lf %lf %lf", &cost, &extraCk_N, &goal);
		
		double nowCkEarningRate = 2.0, ans = goal / nowCkEarningRate; // 쿠키를 초당 몇개 얻는지와 farm 안짓고 그냥 초당 2개의 쿠키만 받아서 goal 까지 채우는 경우로 답 초기화
		double timeUntilSetFarm = 0.0;

		while (cost / nowCkEarningRate < ans)
		{
			timeUntilSetFarm += cost / nowCkEarningRate; // farm 짓기까지 걸리는 시간 추가
			nowCkEarningRate += extraCk_N; // 초당 쿠키 얻는 개수 증가

			if (ans > timeUntilSetFarm + goal / nowCkEarningRate) ans = timeUntilSetFarm + goal / nowCkEarningRate;
			else break;
		}

		fprintf(opt, "Case #%d: %.7lf\n", tc + 1, ans);
	}

	fclose(ipt);
	fclose(opt);

	return 0;
}



