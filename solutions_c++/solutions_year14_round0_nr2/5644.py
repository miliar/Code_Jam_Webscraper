#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>

using namespace std;


int main()
{
	int i, j;
	int T;
	double c, f, x;

	scanf("%d ", &T);
	for (int t=0; t<T; t++) {
		printf("Case #%d: ", t+1);

		scanf("%lf%lf%lf ", &c, &f, &x);

		int n = 0;
		vector<double> ct;
		ct.push_back(0.0);
		while (1) {
			if (!n)
				ct.push_back(c / 2.0);
			else
				//ct.push_back( ct[n] + c / (2.0 + f*(n-1)));
				ct.push_back( ct[n] + c / (2.0 + f*n));

			double prdAmt = (2.0 + f*n)*ct[n+1] - c*n;
			for (i=1; i<=n; i++)
				prdAmt -= f*ct[i];

			if (prdAmt >= x)
				break;

			double noAdd = x / (2.0 + f*n);
			double oneAdd = x / (2.0 + f*(n + 1)) + c / (2.0 + f*n);
			if (noAdd <= oneAdd) break;

			n++;
		}

		double res = 0.0;	
		for (i=1; i<=n; i++)
			res += ct[i];
		res = x + c*n + res*f;
		res = res / (2.0 + f*n);

		printf("%.7lf\n", res);
	}

	return 0;
}

