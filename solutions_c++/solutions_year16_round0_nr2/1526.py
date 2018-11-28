#include <iostream>
#include <cstdio>
#include <cstring>
#include <deque>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#define FOR(i, a, b) for(int i=a; i<b; i++)
#define RFOR(i, a, b) for(int i=a-1; i>=b; i--)
inline int MIN(int a, int b) { return (a<b)?a:b; }
inline int MAX(int a, int b) { return (a<b)?b:a; }
inline int ABS(int a) { if (a<0) a=-a; return a; }

typedef long long Int;
using namespace std;

int main()
{
	int t, c = 0;
	scanf("%d", &t);
	while (t--)
	{
		char str[1000];
		scanf(" %s", str);
		int l = strlen(str);
		int flips = 0;
		RFOR(i, l, 0)
		{
			if (str[i]=='-' && flips%2==1)
				continue;
			else if (str[i]=='-' && flips%2==0)
				flips+=1;
			else if (str[i]=='+' && flips%2==1)
				flips+=1;
		}
		printf("Case #%d: %d\n", ++c, flips);
	}
	return 0;
}
