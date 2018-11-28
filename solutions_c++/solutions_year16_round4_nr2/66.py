#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
double dp[201][201][201];
int main()
{
	freopen("b-small-attempt0.in", "r", stdin);
	freopen("small.txt", "w", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		for (int i = 0; i < 201; i++)for (int j = 0; j < 201; j++)for (int k = 0; k < 201; k++)dp[i][j][k] = 0.0;
		int num, gen;
		scanf("%d%d", &num, &gen);
		vector<double>vec;
		for (int i = 0; i < num; i++)
		{
			double z;
			scanf("%lf", &z);
			vec.push_back(z);
		}
		double maxi = 0;
		for (int i = 0; i < (1 << num); i++)
		{
			double d[100];
			fill(d, d + num + 1, 0);
			d[0] = 1;
			double n[100];
			int cnt = 0;
			for (int j = 0; j < num; j++)
			{
				if (i&(1 << j))
				{
					cnt++;
					n[0] = d[0] * (1 - vec[j]);
					for (int k = 0; k < num; k++)
					{
						n[k + 1] = d[k] * vec[j] + d[k + 1] * (1.0 - vec[j]);
					}
					for (int k = 0; k < num; k++)
					{
						d[k] = n[k];
					}
				}
			}
			if (cnt == gen)maxi = max(maxi, d[gen / 2]);
		}
		printf("Case #%d: %.10lf\n", p, maxi);
	}
}