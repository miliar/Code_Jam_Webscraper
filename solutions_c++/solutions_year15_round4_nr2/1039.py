#include <bits/stdc++.h>
using namespace std;

int test;
int n;
double xx1, vv1;
long long xx, vv;
double x1[111], v1[111];
long long x[111], v[111];

int main()
{
	freopen("B.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> n >> vv1 >> xx1;
		vv = vv1*10000000;
		xx = xx1*10000000;
		for(int i = 1; i <= n; i++)
		{
			cin >> v1[i] >> x1[i];
			v[i] = v1[i]*10000000;
			x[i] = x1[i]*10000000;
		}

		if(n == 1 )
			{
				if(x[1] != xx) cout << "IMPOSSIBLE\n";
				else
					cout << fixed << setprecision(9) << vv1/v1[1] << "\n";
			}
		else
		{
			if(xx == x[1] && xx == x[2])
			{
				cout << fixed << setprecision(9) << vv1/(v1[1] + v1[2]);
				cout << "\n";
			}
			else
			if(xx == x[1] || xx == x[2])
			{
				if(xx == x[1]) 
					cout << fixed << setprecision(9) << vv1/(v1[1]);
				else
				if(xx == x[2])
					cout << fixed << setprecision(9) << vv1/(v1[2]);
					cout << "\n";
			}
			else
			{
			if((xx > x[1] && xx > x[2]) || (xx < x[1] && xx < x[2])) cout << "IMPOSSIBLE\n";
			else
			{
				double t1 = vv1*(xx1 - x1[2])/v1[1]/(x1[1] - x1[2]);
				double t2 = vv1*(xx1 - x1[1])/v1[2]/(x1[2] - x1[1]);
			if(t1 < 0 && t2 < 0) cout << "IMPOSSIBLE\n";
			else
			{
				if(t1 < t2) cout << fixed << setprecision(9) << t2;
				else cout << fixed << setprecision(9) << t1;
				cout << "\n";
			}
			}
			}
		}
	}
	return 0;
}