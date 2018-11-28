#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	for (int j = 0; j < t; ++j)
	{
		int n; 
		double x, v;
		cin>>n>>v>>x;
		double Ri[2];
		double Ti[2];
		for (int i = 0; i < n; ++i)
			cin>>Ri[i]>>Ti[i];
		double res = -1;
		if (n == 2)
		{
			if (Ti[0] != Ti[1])
			{
				double t1 = (x - Ti[1])/(Ti[0] - Ti[1]) * v / Ri[0];
				double t2 = (Ti[0] - x)/(Ti[0] - Ti[1]) * v / Ri[1];
				if (t1 >= 0 && t2 >= 0) res = max(t1, t2);
			}
			else if (Ti[0] == x) res = v/(Ri[0] + Ri[1]);
		}
		else if (Ti[0] == x) res = v / Ri[0];
		cout<<"Case #" << j + 1 <<": ";
		if (res >= 0)
			cout<<setprecision(10)<<fixed<<res<<endl;
		else cout<<"IMPOSSIBLE\n";
	}
    return 0;
}
