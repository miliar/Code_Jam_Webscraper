using namespace std;
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>

typedef long long L;
typedef unsigned long long U;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;

main()
{
	int tc;
	cin>>tc;
	for(int t = 1;t<=tc;t++)
	{
		double C, F, X, sol, T = 0, R = 2.0;
		cin>>C>>F>>X;
		sol = X/R;
		for(int i = 1; i<=X;i++)
		{
			T = T + C/R;
			R = R + F;
			if(sol < T + X/R)
				break;
			sol = T + X/R;
		}
		printf("Case #%d: %.7lf\n", t, sol);
	}
}
