#include <iostream>
#include <cstdio>

using namespace std;

int N, n, M, m;
int P[100][101];

bool checkCol()
{
	int i;
	for(i = 0; i < N; i++)
		if(P[n][m] < P[i][m])
			return false;
	return true;
}

const char *solve()
{
	for(n = 0; n < N; n++)
		for(m = 0; m < M; m++)
			if(P[n][m] < P[n][M] && !checkCol())
				return "NO";
	return "YES";
}

int main()
{
	FILE *in,*out;
//	char line[1000];
	int T, t;
	in = fopen("B.in","r");
	out = fopen("B.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d",&T);
	for(t = 1; t <= T; t++)
	{
		fscanf(in, "%d %d", &N, &M);
		for(n = 0; n < N; n++)
		{
			P[n][M] = 0;
			for(m = 0; m < M; m++)
			{
				fscanf(in, "%d", &P[n][m]);
				if(P[n][m] > P[n][M])
					P[n][M] = P[n][m];
			}
		}
		fprintf(out, "Case #%d: %s\n",t,solve());
	}
	fclose(in);
	fclose(out);
}
