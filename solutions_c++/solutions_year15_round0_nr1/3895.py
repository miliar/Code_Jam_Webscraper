#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main()
{
	int T;
	int ca = 0;
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		int n;
		scanf("%d", &n);
		string input;
		cin>>input;
		int cur = input[0] - '0';
		int res = 0;
		for (int i = 1; i < n + 1; ++i)
		{
			if(cur < i)
			{
				cur++;
				res++;
			}
			cur += input[i] - '0';
		}
		printf("Case #%d: ", ++ca);
		printf("%d\n", res);
	}
	return 0;
}