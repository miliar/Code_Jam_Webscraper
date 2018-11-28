#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;
#define MAX 210
double matr[MAX][MAX];
double mas[MAX];
void process(int t)
{
	cout << "Case #" << t << ": ";
	
	int N, K;
	cin >> N >> K;
	for (int i = 0; i < N; i++)
		cin >> mas[i];


	int NN = 1 << N;
	double res = 0;
	for (int mask = 0; mask < NN; mask++)
	{
		for (int i = 0; i < MAX; i++)
			for (int j = 0; j < MAX; j++)
				matr[i][j] = 0;
		matr[0][0] = 1;
		int cnt = 0;
		for (int i = 0; i < N; i++)
			if (mask & (1 << i))
			{
				cnt++;
				double p = mas[i];
				for (int j = cnt; j >= cnt; j--)
					for (int k = N; k >= 0; k--)
					{

						double a = 0;
						if (j > 0 && k > 0)
							a += matr[j - 1][k - 1] * p;
						if (j > 0)
							a += matr[j - 1][k] * (1 - p);
						matr[j][k] = max(matr[j][k], a);
					}
			}
		if (cnt == K)
			res = max(res, matr[K][K / 2]);
	}
	cout << res;



	cout << "\n";
}


int main()
{
	freopen("c:\\Projects\\CodeJam2016R2\\B\\B.in", "r", stdin);
	freopen("c:\\Projects\\CodeJam2016R2\\B\\B.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
		process(t + 1);

	fclose(stdin);
	fclose(stdout);
	return 0;
}