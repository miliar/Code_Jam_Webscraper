#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std; 

int N;
double V, X;
double R[120], x[120];

int Chk(double T)
{
	// Vol = R[i] * T, Temp = x[i]
	double CurVol1 = 0, WT1 = 0;
	for (int i = 0; i < N; i ++)
	{
		double NewVol = min(R[i] * T, V - CurVol1);
		CurVol1 += NewVol;
		WT1 += NewVol * x[i];
	}
	double CurVol2 = 0, WT2 = 0;
	for (int i = N - 1; i >= 0; i --)
	{
		double NewVol = min(R[i] * T, V - CurVol2);
		CurVol2 += NewVol;
		WT2 += NewVol * x[i];
	}
	if (CurVol1 < V)
		return 0;
	return (WT1 <= V * X && V * X <= WT2);
}

double Work()
{
	scanf("%d%lf%lf", &N, &V, &X);
	double minx = 1e100, maxx = -1e100;
	for (int i = 0; i < N; i ++)
	{
		scanf("%lf%lf", &R[i], &x[i]);
	}

	for (int i = 0; i < N; i ++)
		for (int j = 0; j < N; j ++)
			if (x[i] < x[j])
			{
				swap(x[i], x[j]);
				swap(R[i], R[j]);
			}
	if (X < x[0] || X > x[N - 1])
		return -1;

	
	if (x[0] == x[1])
	{
		return V / (R[0] + R[1]);
	}
	else
	{
		double p = (X * V - x[1] * V) / (x[0] - x[1]);
		return max(p / R[0], (V - p) / R[1]);
	}

	double Left = 0, Right = 1e20;
	for (int Z = 0; Z < 1000; Z ++)
	{
		double Mid = (Left + Right) * 0.5;
		if (Chk(Mid))
			Right = Mid;
		else
			Left = Mid;
	}
	return Left;
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		double A = Work();
		printf("Case #%d: ", Case);
		if (A < 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%.10lf\n", A);
	}
	return 0;
}
