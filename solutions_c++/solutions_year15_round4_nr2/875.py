#include <bits/stdc++.h>
using namespace std;

const int INF = 0x3f3f3f3f;
const double ERROR = 1e-6;

int N;
double V, X;
double r[105], c[105];
double ans;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int T;
	cin >> T;

	for(int t = 1; t<=T; t++)
	{
		cin >> N >> V >> X;
		for(int i=1; i<=N; i++)
			cin >> r[i] >> c[i];
		ans = -1;
		for(int i=1; i<=N; i++)
			if(fabs(c[i] - X) < ERROR)
				ans = (ans < 0 ? V / r[i] : min(ans, V / r[i]));

		if( fabs(c[1] - X) < ERROR && fabs(c[2] - X) < ERROR)
			ans = (ans < 0 ? V / r[1]+r[2] : min(ans, V / (r[2]+r[1])));

		for(int i=1; i<N; i++)
		{
			for(int j=i+1; j<=N; j++)
			{
				if((c[i] < X && c[j] > X) || (c[i] > X && c[j] < X))
				{
					double v1 = V * (X - c[j]) / (c[i] - c[j]);
					double v2 = V * (X - c[i]) / (c[j] - c[i]);
					double nans = max(v1 / r[i], v2 / r[j]);
					ans = (ans < 0 ? nans : min(ans, nans));
				}
			}
		}
		cout << "Case #" << t << ": ";
		ans < 0 ? cout << "IMPOSSIBLE" << endl : cout << fixed << setprecision(9) << ans << endl;
	}

	return 0;
}
