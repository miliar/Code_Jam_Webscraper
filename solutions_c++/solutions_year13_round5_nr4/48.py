#include <iostream>
#include <cstring>
using namespace std;


char s[105];


int getLexMin(int x, int len)
{
	int ans = x;
	for (int i = 0; i < len; i++)
	{
		x |= ( (1 & x) << len );
		x >>= 1;
		ans = min(ans, x);
	}
	return ans;
}

 double ans[1200500];
//double ans[25];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%s", s);
		int n = strlen(s);

		int start = 0;
		for (int i = 0; i < n; i++)
		{
			if (s[i] == 'X')
			{
				start |= (1<<i);
			}
		}
		start = getLexMin(start, n);
		
		for (int i = (1 << n) - 1; i >= start; i--)
			ans[i] = 0;

		for (int i = (1 << n) - 2; i >= start; i--)
		{
			if (i != getLexMin(i, n) )
				continue;
			double cur = 0;
			for (int j = 0; j < n; j++)
			{
				int k = n;
				for (int h = j; ; h = (h + 1) % n, k--)
				{
					if ( ( (1 << h) & i) != 0)
						continue;
					cur += k + ans[getLexMin(i | (1 << h), n) ];
					break;
				}
			}
			cur /= (double) n;
			ans[i] = cur; 
		}
		printf("Case #%d: %.10lf\n", t + 1, ans[start] );
	}


	return 0;
}