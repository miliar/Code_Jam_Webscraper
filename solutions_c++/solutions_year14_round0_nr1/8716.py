#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int a[4][4];
int b[4][4];
int used [17];

int main()
{
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt","w", stdout);
	int n;
	scanf ("%d", &n);
	for (int t = 0; t < n; t++)
	{
		for (int i = 1; i <= 16; i++)
			used[i] = 0;
		int k1;
		scanf ("%d", &k1);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf ("%d", &a[i][j]);
		int k2;
		scanf ("%d", &k2);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf ("%d", &b[i][j]);
		for (int i = 0; i < 4; i++)
		{
			used[a[k1 - 1][i]]++;
			used[b[k2 - 1][i]]++;
		}
		int cnt = 0;
		int curnum;
		for (int i = 1; i <= 16; i++)
		{
			if (used[i] == 2)
			{
				cnt++;
				curnum = i;
			}
		}
		printf ("Case #%d: ", t + 1);
		if (cnt == 0)
			printf ("Volunteer cheated!\n");
		else
		if (cnt == 1)
			printf ("%d\n", curnum);
		else
			printf ("Bad magician!\n");
	}
	return 0;
}
