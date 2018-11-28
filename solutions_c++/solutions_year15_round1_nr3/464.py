#include <fstream>
#include <cmath>
#include <algorithm>

using namespace std;

ifstream fin ("C.in");
ofstream fout ("C.out");

const double ep = 0.00000000001;
const double pi = 3.1415926535898;

long long da, db;

struct VPoint
{
	int n;
	long long x;
	long long y;
};

bool operator < (const VPoint &a, const VPoint &b)
{
	return ((da * a.x + db * a.y) < (da * b.x + db * b.y));
}

int main ()
{
	int T;
	long long N;
	long long ans[5000];
	double X[5000] = {0}, Y[5000] = {0};
	VPoint P[5000];
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> N;
		for (long long i = 1; i <= N; i++)
		{
			fin >> X[i] >> Y[i];
			P[i].x = X[i];
			P[i].y = Y[i];
			P[i].n = i;
			ans[i] = N - 1;
		}
		for (long long k = 1; k <= N; k++)
			for (long long j = k + 1; j <= N; j++)
			{
				da = Y[k] - Y[j];
				db = X[j] - X[k];
				sort (&P[1], &P[N + 1]);
				long long f = 0, ta;
				for (long long i = 1; i <= N / 2; i++)
				{
					if (i > 1 && (da * P[i].x + db * P[i].y) == (da * P[i - 1].x + db * P[i - 1].y))
						ta = f;
					else
					{
						f = i - 1;
						ta = f;
					}
					if (ans[P[i].n] > ta) ans[P[i].n] = ta;
				}
				f = 0;
				for (long long i = N; i >= N / 2 + 1; i--)
				{
					if (i < N && (da * P[i].x + db * P[i].y) == (da * P[i + 1].x + db * P[i + 1].y))
						ta = f;
					else
					{
						f = N - i;
						ta = f;
					}
					if (ans[P[i].n] > ta) ans[P[i].n] = ta;
				}
			}
		fout << "Case #" << t << ":" << endl;
		for (long long i = 1; i <= N; i++)
			fout << ans[i] << endl;
	}
}
