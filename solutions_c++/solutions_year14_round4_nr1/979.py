#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int n, cap, s[11000], used[11000];

void solve()
{
	scanf ("%d%d", &n, &cap);
	int i, j;
	for(i = 0; i < n; i ++)
		scanf ("%d", &s[i]);

	sort(s, s+n, std::greater<int>());
	
	memset(used, 0, sizeof(used));

	int res = 0;
	for(i = 0; i<n; i++)
	{
		if(used[i]) continue;

		for(j = i+1; j < n; j ++)
		{
			if(!used[j] && cap >= s[i] + s[j])
				break;
		}

		used[j] = 1;
		res ++;
	}

	printf ("%d\n", res);
}

int main ()
{

	int tt;
	scanf ("%d", &tt);

	int i;
	for(i = 0; i < tt; i ++)
	{
		printf ("Case #%d: ", i+1);
		solve();
	}

	return 0;
}