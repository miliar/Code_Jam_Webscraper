#include <cstdio>

using namespace std;

int N, ans, p;
int a[10][10];
int b[10];

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	bool w;
	scanf ("%d", &N);
	for (int i=1; i <= N; ++i)
	{
		w = false;
		scanf ("%d", &ans);
		for (int j=1; j <= 4; ++j)
			for (int k=1; k <= 4; ++k)
				scanf ("%d", &a[j][k]);
		for (int j=1; j <= 4; ++j)
			b[j] = a[ans][j];
		scanf ("%d", &ans);
		for (int j=1; j <= 4; ++j)
			for (int k=1; k <= 4; ++k)
				scanf ("%d", &a[j][k]);
		printf ("Case #%d: ", i);
		p = 0;
		for (int j=1; j <= 4; ++j)
		{
			for (int k=1; k <= 4; ++k)
				if (b[j] == a[ans][k])
				{
					if (p == 0)
						p = b[j];
					else
					{
						printf ("Bad magician!\n");
						w = true;
						break;
					}
				}
			if (w)
				break;
		}
		if (w)
			continue;
		if (p == 0)
			printf ("Volunteer cheated!\n");
		else
			printf ("%d\n", p);
	}
	return 0;
}