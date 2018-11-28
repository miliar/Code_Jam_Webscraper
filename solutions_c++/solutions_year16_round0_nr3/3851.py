#include<stdio.h>
#include<string.h>

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int T;
int N, J;
long long int V[33];
int X[33];
void DFS(int next)
{
	for (int i = 0; i <= N; i++)X[i] = 0;
	for (int i = 0; i < N; i++)
	{
		X[i] += V[i];
		X[i + 1] += V[i];
	}
	bool check = 0;
	for (int i = 0; i < N; i++)
	{
		if (!(X[i] ==1 || X[i] == 0))
		{
			check = 1;
			break;
		}
	}

	if (check == 0 && X[N-1] == 1 && X[0] == 1 && X[N] == 0)
	{
		J--;
		for (int i = 0; i < N; i++)
		{
			fprintf(out,"%d", X[i]);
		}
		fprintf(out, " ");
		for (int i = 2; i <= 10; i++)
		{

			fprintf(out, "%d ", i+1);
		}
		fprintf(out, "\n");
		if (J == 0)return;
	}
	if (next == -1)return;

	V[next] = 1;
	DFS(next - 1);
	if (J == 0)return;
	V[next] = -1;
	DFS(next - 1);
	if (J == 0)return;
	V[next] = 0;
	DFS(next - 1);
	if (J == 0)return;
	
}

int main()
{
	fscanf(in,"%d", &T);
	for (int t = 1; t <= T;t++)
	{
		fscanf(in ,"%d %d", &N,&J);
		fprintf(out, "Case #1:\n");
		V[N - 2] = 1;
		DFS(N-3);
	}

}