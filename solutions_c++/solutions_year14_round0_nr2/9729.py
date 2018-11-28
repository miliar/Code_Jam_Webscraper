//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt3.in", "r", stdin);
	//freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int T, t;
	double C, F, X;

	scanf("%d", &T);
	for (t=1; t<=T; ++t)
	{		
		scanf("%lf %lf %lf", &C, &F, &X);

		int n = 0;
		double ans = X / 2;
		while (1)
		{	
			double ans1 = ans - X / (2 + n*F) + C / (2 + n * F) + X / (2 + (n+1) * F);

			if (ans1 >= ans)
				break;

			ans =  ans1; 
			++n;
		}
		
		printf("Case #%d: %.7lf\n", t, ans);
	}
}
