#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <stack>
#include <cmath>
#include <queue>
using namespace std;

int n;
string s;

bool evaluate(int k)
{
	int cum = k;
	for (int i = 0; i < s.length(); ++i)
	{
		if (cum < i) return false;
		cum += s[i] - '0';
	}
	return true;
}

void input()
{
	cin >> n >> s;
	for (int i = 0; ; ++i)
	{
		if (evaluate(i)) 
		{
			printf("%d\n", i);
			return;
		}
	}

}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int T;
	scanf("%d", &T);

	for (int test = 1; test <= T; ++test)
	{
		printf("Case #%d: ", test);
		input();
	}

	return 0;
}