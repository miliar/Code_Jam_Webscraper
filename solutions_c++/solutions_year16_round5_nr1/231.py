#include <bits/stdc++.h>
using namespace std;
const int MAXN = 20005;
char A[MAXN];
int main()
{
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc)
	{
		scanf("%s", A);
		int n = strlen(A), c1 = 0;
		stack <char> S;
		for (int i = 0; i < n; ++i)
		{
			if(!S.empty())
			{
				if(A[i] == S.top())
				{
					S.pop();
					c1++;
				}
				else
					S.push(A[i]);
			}
			else
				S.push(A[i]);
		}
		int c2 = n/2 - c1;
		printf("Case #%d: %d\n", tc, 10*c1 + 5*c2);
	}
	return 0;
}