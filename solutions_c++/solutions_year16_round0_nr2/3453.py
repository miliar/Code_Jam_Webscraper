#include <cstdio>
#include <cstring>


char s[1000000];

int solve()
{
	int r = 0;
	const int n = (int)strlen(s);	

	s[n] = '+';
	for(int i = 0; i < n; i++)
		if(s[i] != s[i + 1])
			r++;

	return r;
}

int main()
{
	int tests;
	scanf("%i\n", &tests);
	for(int t = 1; t <= tests; t++)
	{
		scanf("%s\n", s);
		int res = solve();
		printf("Case #%i: %i\n", t, res);
	}

	return 0;
}

