#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-small-attempt2 (1).in" , "r" , stdin);
	freopen("kiddie.out" , "w" , stdout);
	int t;
	cin >> t;
	for(int cnt = 1;cnt <= t;cnt++)
	{
		int n;
		double v , c;
		cin >> n >> v >> c;
		double vi[n] , ci[n];
		for(int i = 0;i < n;i++)
			cin >> vi[i] >> ci[i];
		if(n == 2)
		{
			if((ci[0] - c)*(c - ci[1]) < 0)
				cout << "Case #" << cnt << ": " << "IMPOSSIBLE\n";
			else if(ci[1] == ci[0])
			{
				printf("Case #%d: %.8lf\n",cnt,v/(vi[1] + vi[0]));
			}
			else
			{
				double t2 , t1;
				t2 = ((c - ci[0]) * v)/((ci[1] - ci[0]) * vi[1]);
				t1 = (v - vi[1]*t2)/vi[0];
				printf("Case #%d: %.8lf\n",cnt,max(t1 , t2));
			}
		}
		else
		{
			if(ci[0] == c)
			{
				printf("Case #%d: %.8lf\n",cnt,v/vi[0]);
			}
			else
			{
				cout << "Case #" << cnt << ": " << "IMPOSSIBLE\n";
			}
		}
	}
	return 0;
}