#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
#define N 1002
void a()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	vector<int> list;
	int cnt = 0;
	while (T--)
	{
		char input[N];
		list.clear();
		int S_max;
		scanf("%d %s\n", &S_max, input);
		for (int i = 0; i <= S_max; i++)
		{
			list.push_back(input[i] - '0');
		}
		int result = 0;
		int standup = 0;
		for (int i = 0; i <= S_max; i++)
		{
			while (standup < i)
			{
				result++;
				standup++;
			}
			standup += list[i];
		}
		printf("Case #%d: %d\n", ++cnt, result);
	}

}
bool cmp(const int a1, const int a2)
{
	return a1 > a2;
}
bool check(int number, int *v, int size)
{
	for (int moveday = 0; moveday < number; moveday++)
	{
		int leftday = number - moveday;
		bool fail = false;

		int current_move = 0;
		for (int i = 0; i < size; i++)
		{
			if (v[i] < leftday) break;
			current_move += v[i] / leftday;
			if (v[i] % leftday == 0) current_move--;
			if (current_move > moveday)
			{
				fail = true;
				break;
			}
		}

		if (!fail)
		{
			return true;
		}
	}
	return false;
}
void b()
{
#define B_N 1002
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T,n;
	int v[N];
	scanf("%d", &T);
	int cnt = 0;
	while (T--)
	{
		scanf("%d", &n);
		int maxone = -1;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &v[i]);
			if (v[i]>maxone) maxone = v[i];
		}
		sort(v, v + n, cmp);
		if (v[0] == 0)
		{
			printf("Case #%d: %d\n", ++cnt, 0);
			continue;
		}
		int left = 0, right = maxone;
		while (left < right - 1)
		{
			int mid = (left + right) >> 1;
			if (check(mid, v, n))
			{
				right = mid;
			}
			else
			{
				left = mid;
			}
		}
		printf("Case #%d: %d\n", ++cnt, right);
	}
}
int main()
{
	//a();
	b();
	//system("pause");
	return 0;
}