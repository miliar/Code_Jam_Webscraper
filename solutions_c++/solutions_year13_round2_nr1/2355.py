#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 1000000

int N, K;
int a;
int m[MAX];
int st[MAX];
int cu[MAX];

class algorithm
{

public:
void solution(char *input, char *output);

/* You can add your own class functions, 
but main function call "solution" function only. */

};

FILE *ifp, *ofp;

void algorithm::solution(char *input, char *output){


	ifp = fopen(input, "r");
	ofp = fopen(output, "w");

	if (ifp == NULL || ofp == NULL)
		return;

	int C;
	int inia;
	fscanf (ifp, "%d\n", &C);

	for (int i = 1; i <= C; i++)
	{
		int steps = 0;
		int count = 0;
		fscanf (ifp, "%d %d\n", &a, &N);
		inia = a;
		for (int j = 0; j < N; j++)
		{
			fscanf (ifp, "%d ", (m+j));
		}

		vector <int> v;
		v.assign(m, m+N);
	
		sort (v.begin(), v.end());

		for (int i = 0; i < N; i++)
			m[i] = v[i];

		v.clear();

		for (int j = 0; j < N; j++)
		{
			while (a <= m[j])
			{
				int t = a;

				a += (t-1);
				st[j]++;
				if (st[j] == (N - j))
					goto A;
			}
			a += m[j];
		}

		for (int j = N-1; j >= 0; j--)
		{
			if (st[j] == 0 || st[j] == 1)
			{
				break;
			}
			else
				st[j] = 0;
		}

A:		for (int j = 0; j < N; j++)
		{
			steps += st[j];
		}

		fprintf (ofp, "Case #%d: %d\n", i, steps);
		printf ("Case #%d: %d %d\n", i, steps, inia);
		for (int i = 0; i < N; i++)
			printf ("%d ", m[i]);
		printf ("\n");

		memset (st, 0, sizeof(int)*N);
	}
	fclose(ifp);
	fclose(ofp);
}


/* You can add your own functions, 
but main function call "solution" function only. */

int main (int argc, char *argv[])
{
	algorithm alg;
	alg.solution(argv[1], argv[2]);
	return 0;
}