# include <iostream>
# include <algorithm>
# include <cstdio>
using namespace std;

int N;

double naaa[2048];
double keeee[2048];

int used[2048], aA, aB, p , q;
int main ()
{
	int i, jj, minnn, r, l, tt, kk;
	scanf ("%d", &tt);
	for (kk = 1; kk <= tt; kk ++)
	{

		aB = aA = 0;
		for (i = 0; i < 2001; i ++)
		{
			naaa[i] = keeee[i] = 0.0;
			used[i] = 0;
		}
			scanf ("%d", &N);
	for (i = 0; i < N; i ++)
	scanf ("%lf", &naaa[i]);
	for (i = 0; i < N; i ++)
	scanf ("%lf", &keeee[i]);
		sort (naaa, naaa + N);
		sort (keeee, keeee + N);
		for (i = 0; i < N; i ++)
		{
			l = 0;
			for (jj = 0; jj < N - i; jj ++)
			if (naaa[jj + i] < keeee[jj]) l = 1;
			if (l == 0)
			{
				aB = (N - i);
				break;}}for (i = 0; i < N; i ++)
		{
			r = -1;
			minnn = 2.0;
			for (jj = 0; jj < N; jj ++)
			if (keeee[jj] < minnn && keeee[jj] > naaa[i] && used[jj] == 0)
			{
				r = jj;
				minnn = keeee[   jj];
			}
			if (r == -1) aA ++;
			else used[r] = 1;
		}
		cout << "Case #" << kk << ": ";
		printf ("%d %d\n", aB, aA);
	}
	return 0;
}
