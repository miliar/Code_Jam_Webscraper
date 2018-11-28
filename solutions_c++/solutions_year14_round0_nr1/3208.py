#include <cstdio>
using namespace std;
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int p = 0; p < t; ++p)
	{
		int a1;
		scanf ("%d", &a1);
		int g1[5][5];
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf ("%d", &g1[i][j]);
		int a2;
		scanf ("%d", &a2);
		int g2[5][5];
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf ("%d", &g2[i][j]);
		int i = a1-1;
		int g11[4] = {0};
		for (int j = 0; j < 4; ++j)
			g11[j] = g1[i][j];
		i = a2-1;
		int g22[4] = {0};
		for (int j  =0; j < 4; ++j)
			g22[j] = g2[i][j];
		int c = 0;
		int ans = -99;	
		for (int j = 0; j < 4; ++j)
		{
			for (int x = 0; x < 4; ++x)
			{
				if (g11[j] == g22[x])
				{
					++c;
					ans = g11[j];	
				}
			}
		}		
		if (c == 1)
			printf ("Case #%d: %d\n", p+1, ans);
		else if (c == 0)
			printf ("Case #%d: Volunteer cheated!\n", p+1);
		else
			printf ("Case #%d: Bad magician!\n", p+1);
	}
	return 0;
}