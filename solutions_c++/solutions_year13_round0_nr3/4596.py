#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define LL long long

using namespace std;

const int maxn = 1005;

vector <int> list;
bool a[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		int start, finish;
		scanf("%d%d", &start, &finish);
		for (int i = 1; i <= finish; i++)
		{
			list.clear();
			int now = i;
			while(now != 0)
			{
				list.push_back(now % 10);
				now /= 10;
			}
			a[i] = true;
			for (int j = 0; j < list.size(); j++)
				if (list[j] != list[list.size() - j - 1])
				{
					a[i] = false;
					break;
				}
		}
		int answer = 0;
		for (int choice = 1; choice <= finish; choice++) if (a[choice])
		{
			int x = choice * choice;
			if (x >= start && x <= finish && a[x])
				answer++;
		}
		printf("Case #%d: %d\n", test, answer);
	}
}