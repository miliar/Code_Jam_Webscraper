#include <cstdio>

int lawn[100][100];
int simul[100][100];
int n, m;

bool isYes()
{
	for (int i=0; i<n; ++i)
		for (int j=0; j<m; ++j)
			if (lawn[i][j] != simul[i][j])
				return false;

	return true;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int c=1; c<=t; ++c)
	{
		scanf("%d %d", &n, &m);
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
			{
				scanf("%d", &lawn[i][j]);
				simul[i][j] = 100;
			}

		for (int i=0; i<n; ++i)
		{
			int mv = 0;
			for (int j=0; j<m; ++j)
				if (lawn[i][j] > mv)
					mv = lawn[i][j];

			for (int j=0; j<m; ++j)
				if (simul[i][j] > mv)
					simul[i][j] = mv;
		}

		for (int i=0; i<m; ++i)
		{
			int mv = 0;
			for (int j=0; j<n; ++j)
				if (lawn[j][i] > mv)
					mv = lawn[j][i];

			for (int j=0; j<n; ++j)
				if (simul[j][i] > mv)
					simul[j][i] = mv;
		}

		printf("Case #%d: ", c);
		if (isYes())
			printf("YES\n");
		else
			printf("NO\n");
	}
	
	return 0;
}