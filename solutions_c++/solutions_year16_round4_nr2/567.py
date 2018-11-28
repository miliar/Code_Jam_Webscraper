#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin ("B.in");
ofstream fout ("B.out");

int T, N, K;
double P[300];
double p[1000], q[1000];
double ans = 0;

int main ()
{
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		ans = 0;
		fin >> N >> K;
		for (int i = 1; i <= N; i++)
			fin >> P[i];
		sort (P, &P[N + 1]);
		for (int i = 0; i <= K; i++)
		{
			for (int j = 500 - K; j <= 500 + K; j++) p[j] = 0;
			p[500] = 1;
			for (int j = 1; j <= i; j++)
			{
				for (int k = 500 - K; k <= 500 + K; k++)
					q[k] = p[k - 1] * P[j] + p[k + 1] * (1 - P[j]);
				for (int k = 500 - K; k <= 500 + K; k++)
					p[k] = q[k];
			}
			for (int j = N; j >= N - K + i + 1; j--)
			{
				for (int k = 500 - K; k <= 500 + K; k++)
					q[k] = p[k - 1] * P[j] + p[k + 1] * (1 - P[j]);
				for (int k = 500 - K; k <= 500 + K; k++)
					p[k] = q[k];
			}
			if (ans < p[500]) ans = p[500];
		}
		fout << "Case #" << t << ": " << ans << endl;
	}
}

