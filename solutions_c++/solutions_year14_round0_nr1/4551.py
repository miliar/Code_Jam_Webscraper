#include <cstdio>

int main()
{
	FILE *f;
	f = fopen("test.out", "w");
	//freopen("test.in", "r", stdin);
	freopen("A-small-attempt0.in", "r", stdin);
	int n, a, b, count2, index;
	int arra[4][4], arrb[4][4], check[17];
	scanf("%d", &n);
	for(int N=1;N<=n;N++)
	{
		count2 = 0;
		for (int y=1;y<17;y++)
			check[y] = 0;

		scanf("%d", &a);
		for(int y=0;y<4;y++)
			for(int x=0;x<4;x++)
			{
				scanf("%d", &arra[x][y]);
				if (y+1 == a)
					check[arra[x][y]]++;
			}

		scanf("%d", &b);
		for(int y=0;y<4;y++)
			for(int x=0;x<4;x++)
			{
				scanf("%d", &arrb[x][y]);
				if (y+1 == b)
					check[arrb[x][y]]++;
			}

		
		for (int y=1;y<17;y++)
			if (check[y] == 2)
			{
				count2++;
				index = y;
			}

		if (count2 == 1)
			fprintf(f, "Case #%d: %d\n", N, index);
		else if (count2 == 0)
			fprintf(f, "Case #%d: Volunteer cheated!\n", N);
		else
			fprintf(f, "Case #%d: Bad magician!\n", N);
	}
	fclose(f);
	return 0;
}
