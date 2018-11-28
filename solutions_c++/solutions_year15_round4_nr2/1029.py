		//	   - -- --- ---- -----be name khoda----- ---- --- -- -		\\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

double r[N], x[N];
double V, X;

inline double val(double v1)
{
	assert(0);
}

int main()
{
	int _ = in();
	for(int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		int n = in();
		double res = -1;
		cin >> V >> X;
		for(int i = 0; i < n; i++)
			cin >> r[i] >> x[i];
		if(n == 1)
		{
			if(x[0] != X)
				res = -1;
			else
				res = double(V / r[0]);
		}
		else
		{
			if(X < min(x[0], x[1]) || X > max(x[0], x[1]))
				res = -1;
			else
			{
				if(x[0] == x[1])
				{
					double chi = r[0] + r[1];
					res = double(V / chi);
				}
				else
				{
					double alpha = (X - x[1]) / (x[0] - X);
					double v2 = V / (alpha + 1.0);
					double v1 = V - v2;
					assert(abs(v1 * x[0] + v2 * x[1] - X * V) < 1e-7);
					double ans = max(v1 / r[0], v2 / r[1]);
					res = ans;
				}
			}
		}
		if(res < 0)
			cout << "IMPOSSIBLE\n";
		else
			printf("%0.10f\n", res);

	}
}
