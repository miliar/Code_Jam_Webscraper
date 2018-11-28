		//	   - -- --- ---- -----be name khoda----- ---- --- -- -		\\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

char c[N];

int main()
{
	int _ = in();
	for(int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		int n = in();
		scanf("%s", c);
		string s(c);
		int sum = 0, mn = 0;
		for(int i = 0; i <= n; i++)
		{
			if(s[i] > '0' && sum < i)
			{
				mn += i - sum;
				sum = i;
			}
			sum += s[i] - '0';
		}
		printf("%d\n", mn);
	}
}
