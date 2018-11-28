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
int cards[20][20];
int cntNum[20];
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout); //输出重定向，输出数据将保存在out.txt文件中
	//////////////////////////////////////////////////////////////////////////
	scanf("%d", &T);
	int cases = 1;
	while (T--)
	{
		memset(cntNum, 0, sizeof(cntNum));
		int ans1, ans2;
		scanf("%d", &ans1);
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				scanf("%d", &cards[i][j]);
			}
		}
		for (int i = 1; i <= 4; i++)
		{
			int temp = cards[ans1][i];
			cntNum[temp]++;
		}
		
		scanf("%d", &ans2);
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				scanf("%d", &cards[i][j]);
			}
		}
		for (int i = 1; i <= 4; i++)
		{
			int temp = cards[ans2][i];
			cntNum[temp]++;
		}

		//检查
		int found = 0, outNum;
		for (int i = 1; i <= 16; i++)
		{
			if (cntNum[i] == 2)
			{
				found++;
				outNum = i;
			}
		}

		if (found == 1)
		{
			printf("Case #%d: %d\n", cases++, outNum);
		}
		else if (found >= 2)
		{
			printf("Case #%d: Bad magician!\n", cases++);
		}
		else if (found == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", cases++);
		}
	}

	///结束
	return 0;
}