#include <stdio.h>

using namespace std;

#define MAX 100
#define NOTFOUND 0

int m[100][100];
int N, M;

int check_solution (void)
{
	int rflag;
	int cflag;

	for (int i = 0; i < N; i++)
	{
		rflag = !NOTFOUND;
		cflag = !NOTFOUND;
		for (int j = 0; j < M; j++)
		{
			int val = m[i][j];
			for (int x = 0; x < N; x++)
				if (m[x][j] > val)
				{
					rflag = NOTFOUND;
				}
			for (int x = 0; x < M; x++)
				if (m[i][x] > val)
					cflag = NOTFOUND;
		}

		if (rflag == NOTFOUND && cflag == NOTFOUND)
			return 0;
	}
	return 1;
}

int main (int argc, char *argv[])
{
	FILE *ifp, *ofp;

	ifp = fopen(argv[1], "r");
	ofp = fopen(argv[2], "w");

	if (ifp == NULL || ofp == NULL)
		return 0;

	int T;
	fscanf (ifp, "%d\n", &T);

	for (int i = 1; i <= T; i++)
	{
		int j;

		fscanf (ifp, "%d %d\n", &N, &M);

		for (int j = 0; j < N; j++)
			for (int k = 0; k < M; k++)
				fscanf(ifp, "%d ", &m[j][k]);


		int retVal = check_solution();

		if (retVal)
		{
			fprintf (ofp, "Case #%d: YES\n", i);
			printf("Case #%d: YES\n", i);
		}
		else	
		{
			fprintf (ofp, "Case #%d: NO\n", i);
			printf("Case #%d: NO\n", i);
		}
	}
}