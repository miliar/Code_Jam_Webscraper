#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <iostream>

#define ENP     printf("**Entry Point**\n")
#define A       first
#define B       second
#define MP      make_pair

using namespace std;

typedef long long ll;

const int INF = 0x60000000;
const int MINF = -1000000000;
const ll mod = 1000000007;
const int cons = 50000001;
const double pi = 3.141592653589793;

void flip(int pos, string & str)
{
	string tmp = str.substr(0, pos + 1);
	reverse(tmp.begin(), tmp.end());

	for (int i = 0; i < tmp.length(); i++)
	{
		if (tmp[i] == '+')tmp[i] = '-';
		else tmp[i] = '+';
	}
	str = str.substr(pos + 1);
	str = tmp + str;
}

int main()
{
//	freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int testCases;
	scanf("%d", &testCases);

	for (int testNum = 1; testNum <= testCases; testNum++)
	{
		printf("Case #%d: ", testNum);
		string str;
		cin >> str;

		int cnt = 0;
		for (int i = str.length() - 1; i >= 0; i--)
		{
			if (str[i] == '-')
			{
				int pos = i;
				bool flag = false;

				for (int j = 0; j < str.length(); j++)
				{
					if (str[j] == '+')
					{
						flag = true;
						continue;
					}
					else
					{
						if (flag)
						{
							pos = j - 1;
						}
						break;
					}
				}

				if (flag)
				{
					flip(pos, str);
					cnt++;
				}

				flip(i, str);
				cnt++;
			}
			else continue;
		}

		printf("%d\n", cnt);
	}

	return 0;
}