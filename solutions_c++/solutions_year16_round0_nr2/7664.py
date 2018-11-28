#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cstring>
#define INF 987654321

using namespace std;

int t;
string str;
char temp;
int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
#endif
	freopen("output2.txt", "w+", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		int cnt = 0;
		cin >> str;
		temp = str[0];
		for (int i = 1; i < str.length(); i++)
		{
			if (temp != str[i])
			{
				cnt++;
				temp = str[i];
			}
		}
		if (temp == '+')
		{
			printf("Case #%d: %d\n", i+1, cnt);
		}
		else
		{
			printf("Case #%d: %d\n", i + 1, cnt+1);
		}
	}
}
