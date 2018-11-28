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

void printChar(char c, int a)
{
	FOR(i, 0, a)
		printf("%c", c);
}

int main()
{
	int t, c = 0;
	cin >> t;
	while (t--)
	{
		c+=1;
		printf("Case #%d: ", c);
		char str[3000];
		scanf(" %s", str);
		int arr[26] = {0};
		int l = strlen(str);
		FOR(i, 0, l)
		{
			arr[str[i]-'A']++;
		}
		int result[10] = {0};
		if (arr['Z'-'A']>0)
		{
			result[0] = arr['Z'-'A'];
			arr['E'-'A'] -= arr['Z'-'A'];
			arr['R'-'A'] -= arr['Z'-'A'];
			arr['O'-'A'] -= arr['Z'-'A'];
			arr['Z'-'A'] = 0;
		}
		if (arr['X'-'A']>0)
		{
			result[6] = arr['X'-'A'];
			arr['I'-'A'] -= arr['X'-'A'];
			arr['S'-'A'] -= arr['X'-'A'];
		}
		if (arr['S'-'A']>0)
		{
			result[7] = arr['S'-'A'];
			arr['V'-'A'] -= arr['S'-'A'];
			arr['N'-'A'] -= arr['S'-'A'];
			arr['E'-'A'] -= 2*arr['S'-'A'];
		}
		if (arr['V'-'A']>0)
		{
			result[5] = arr['V'-'A'];
			arr['F'-'A'] -= arr['V'-'A'];
			arr['E'-'A'] -= arr['V'-'A'];
			arr['I'-'A'] -= arr['V'-'A'];
		}
		if (arr['W'-'A']>0)
		{
			result[2] = arr['W'-'A'];
			arr['T'-'A'] -= arr['W'-'A'];
			arr['O'-'A'] -= arr['W'-'A'];
		}
		if (arr['G'-'A']>0)
		{
			result[8] = arr['G'-'A'];
			arr['E'-'A'] -= arr['G'-'A'];
			arr['I'-'A'] -= arr['G'-'A'];
			arr['H'-'A'] -= arr['G'-'A'];
			arr['T'-'A'] -= arr['G'-'A'];
		}
		if (arr['F'-'A']>0)
		{
			result[4] = arr['F'-'A'];
			arr['O'-'A'] -= arr['F'-'A'];
			arr['U'-'A'] -= arr['F'-'A'];
			arr['R'-'A'] -= arr['F'-'A'];
		}
		if (arr['R'-'A']>0)
		{
			result[3] = arr['R'-'A'];
			arr['T'-'A'] -= arr['R'-'A'];
			arr['E'-'A'] -= 2*arr['R'-'A'];
			arr['H'-'A'] -= arr['R'-'A'];
			arr['R'-'A'] = 0;
		}
		if (arr['O'-'A']>0)
		{
			result[1] = arr['O'-'A'];
			arr['E'-'A'] -= arr['O'-'A'];
			arr['N'-'A'] -= arr['O'-'A'];
		}
		result[9] = arr['E'-'A'];
		FOR(i, 0, 10)
		{
			printChar('0'+i, result[i]);
		}
		printf("\n");
	}
	return 0;
}
