#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;
#define N 1002
int main()
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
	//system("pause");
	return 0;
}