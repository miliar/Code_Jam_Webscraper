#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <bitset>
using namespace std;

#define INF 987654321
#define LL long long
#define ULL unsigned long long
#define For(i, n) for(int i = 0; i < n; ++i)

//C가 공장생성, F가 추가 쿠키, X가 목표량
double C, F, X;
//i개의 factory를 만드는데 걸리는 시간
double cache[200010];
//i번째의 쿠키 생산량
double cookie[200010];
void process()
{
	//i는 생성한 갯수
	double ret = INF;
	cookie[0] = 2;
	for (int i = 0; i <= 200000; ++i)
	{
		cookie[i + 1] = cookie[i] + F;
		//쿠키 증가
		cache[i + 1] = cache[i] + C / cookie[i];
		
		ret = min(ret, cache[i] + X / cookie[i]);
	}
	printf("%.7lf\n", ret);
}

int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%lf %lf %lf", &C, &F, &X);
		memset(cache, 0, sizeof(cache));
		printf("Case #%d: ", i);
		process();
	}
	return 0;
} 