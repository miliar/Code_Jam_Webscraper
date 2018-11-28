#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stdio.h>
#include <string>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

vector<double> prob;
double mem[16][16];

double calc(int start, int count, int s)
{
	if (start == s)
	{
		return count == 0 ? 1 : 0;
	}

	if (count < 0 || count > s - start)
	{
		return 0;
	}

	double& ans = mem[start][count];
	if (ans >= -0.5)
	{
		return ans;
	}

	
	ans = prob[start] * calc(start + 1, count - 1, s) + (1 - prob[start]) * calc(start + 1, count, s);

	return ans;
}

int main()
{
	cin.sync_with_stdio(0);
	freopen( "..\\input.txt", "r", stdin );
	freopen( "..\\output.txt", "w", stdout );

	int t;
	cin >> t;
	for( int tt = 1; tt <= t; tt++ )
	{
		int n, k;
		cin >> n >> k;
		double best_ans = 0;
		vector<double> all_probs(n);
		for (int i = 0; i < n; i++)
		{
			cin >> all_probs[i];
		}


		for (int mask = 0; mask < (1 << n); mask++)
		{
			int count = 0;
			int temp = mask;
			while (temp > 0)
			{
				count++;
				temp = temp & (temp - 1);
			}
			if (count != k)
			{
				continue;
			}
			
			prob.clear();
			for (int i = 0; i < n; i++)
			{
				if ((mask & (1 << i)) == 0)
				{
					continue;
				}

				prob.push_back(all_probs[i]);
			}

			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					mem[i][j] = -1;
				}
			}

			double ans = calc(0, k / 2, k);

			best_ans = max(best_ans, ans);
		}

		//printf( "Case #%d: ", tt );
		cout << "Case #" << tt << ": ";
		printf("%.8lf\n", best_ans);

	}
	return 0;
}