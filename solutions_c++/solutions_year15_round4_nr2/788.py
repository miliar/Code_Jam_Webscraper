#include<iostream>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<functional>
#include<cmath>


using namespace std;

double r[100], c[100];

bool diff(const double& a, const double& b)
{
	return abs(a - b) > 1e-9;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	
	for(int kase = 1; kase <= T; ++kase)
	{
		int n;
		double v, x;
		cin >> n >> v >> x;
		
		for(int i = 0; i < n; ++i)
			cin >> r[i] >> c[i];
		
		// all same
		bool check = true;
		for(int i = 0; i < n - 1; ++i)
		{
			if(diff(c[i], c[i+1]))
			{
				check = false;
				break;
			}
		}
		if(check)
		{
			if(x != c[0])
			{
				printf("Case #%d: IMPOSSIBLE\n", kase);
				continue;
			}
			
			double total = 0.0;
			for(int i = 0; i < n; ++i)
			{
				total += r[i];
			}
			printf("Case #%d: %.8lf\n", kase, v / total);
			continue;
		}

		double mi = c[0], ma = c[0];
		for(int i = 0; i < n; ++i)
		{
			if(c[i] < mi) mi = c[i];
			if(c[i] > ma) ma = c[i];
		}

		if(x < mi || x > ma)
		{
			printf("Case #%d: IMPOSSIBLE\n", kase);
			continue;
		}

		double diffc[100];
		for(int i = 0; i < n; ++i)
			diffc[i] = abs(c[i] - x);

		double rate[100];
		rate[0] = diffc[1] / (diffc[0] + diffc[1]);
		rate[1] = diffc[0] / (diffc[0] + diffc[1]);

		double time[100];
		ma = 0.0;
		for(int i = 0; i < n; ++i)
		{
			time[i] = (v * rate[i]) / r[i];
			if(time[i] > ma) ma= time[i];
		}

		printf("Case #%d: %.8lf\n", kase, ma);
	


	}

	return 0;
}
