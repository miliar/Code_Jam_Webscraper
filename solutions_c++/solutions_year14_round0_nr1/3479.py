#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

const int MAXN = 10;
int a[MAXN];
int b[MAXN];

int main()
{
	int csnum;
	int k;
	int n1, n2;
	freopen ("A-small-attempt0.in", "r", stdin);
	freopen ("1.out", "w", stdout);
	
	scanf ("%d", &csnum);
	for (int cs = 1; cs <= csnum; cs++)
	{
		scanf ("%d", &n1);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				scanf ("%d", &k);
				if (i == n1 - 1)
					a[j] = k;
			}

		scanf ("%d", &n2);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				scanf ("%d", &k);
				if (i == n2 - 1)
					b[j] = k;
			}

		int ans = 0;
		int cnt = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				if (a[i] == b[j])
				{
					cnt++;
					ans = a[i];
				}
			}

		if (cnt > 1)
			printf ("Case #%d: Bad magician!\n", cs);
		else if (cnt == 1)
			printf ("Case #%d: %d\n", cs, ans);
		else
			printf ("Case #%d: Volunteer cheated!\n", cs);
	}

	return 0;
}

