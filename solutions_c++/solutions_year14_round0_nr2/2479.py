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

//C�� �������, F�� �߰� ��Ű, X�� ��ǥ��
double C, F, X;
//i���� factory�� ����µ� �ɸ��� �ð�
double cache[200010];
//i��°�� ��Ű ���귮
double cookie[200010];
void process()
{
	//i�� ������ ����
	double ret = INF;
	cookie[0] = 2;
	for (int i = 0; i <= 200000; ++i)
	{
		cookie[i + 1] = cookie[i] + F;
		//��Ű ����
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