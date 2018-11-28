#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <bitset>
using namespace std;
//////////////////////////////////////////////////////////////////////////
///宏定义
const int  INF = 1000000000;
const int MAXN = 30000 + 10;
const int maxn = MAXN;
///全局变量 和 函数


int T;
double C, F, X; 
double ans;
int main()
{
//	freopen("D:\\input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout); 
	//////////////////////////////////////////////////////////////////////////
	scanf("%d", &T);
	int cases = 1;
	while (T--)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		int turns = (X / C - 2 / F);
		if (turns < 0)
			turns = 0;
		ans = 0;
		for (int i = 1; i <= turns; i++)
		{
			ans += C / (((double) i - 1) * F + 2);
		}
		ans += X / ((turns) * F + 2);
		printf("Case #%d: %.7f\n", cases++, ans);
	}

	///结束
	return 0;
}