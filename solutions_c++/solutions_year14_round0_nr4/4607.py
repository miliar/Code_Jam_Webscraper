#include <iomanip>
#include <algorithm>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);	
	for (int T_t = 1; T_t <= T; T_t++)
	{
		printf("Case #%d: ",T_t);
		int n;
		scanf("%d",&n);

		vector<double> a,b,c,d;
		a.clear(); b.clear(); c.clear(); d.clear();
		
		for (int i = 0; i < n; i++)
		{
			double x;
			scanf("%lf",&x);
			a.push_back(x);
			c.push_back(x);
		}

		for (int i = 0; i < n; i++)
		{
			double x;
			scanf("%lf",&x);
			b.push_back(x);
			d.push_back(x);
		}

		sort(a.begin(),a.end());
		sort(d.begin(),d.end());
		sort(b.rbegin(),b.rend());
		sort(c.rbegin(),c.rend());

		int ans1 = 0, ans2 = 0;
		int i = 0,j = 0;
		while (i < n)
		{
			if (c[i] > b[j]) ans2++;
			else j++;
			i++;
		}
		i = 0; j = 0;
		while (i < n)
		{
			if (a[i] > d[j]) { ans1++; j++; }
			i++;
		}

		printf("%d %d\n",ans1,ans2);
	}

	return 0;	
}
