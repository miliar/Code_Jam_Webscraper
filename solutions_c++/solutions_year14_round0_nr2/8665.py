#include<map>
#include<set>
#include<iostream>
#include<string.h>
#include<string>
#include<queue>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<memory.h>
#include <iomanip>
using namespace std;

#define mp make_pair
#define X first
#define Y second

double const eps = 1e-10;
int const INF = 100000;
int const MOD = 1;
int const MAX = 1000 + 5;

int main()
{
#ifdef _DEBUG
    freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif
	int t, i, j;
	cin >> t;
	for(j = 0; j < t; ++j)
	{
		cout << "Case #" << j + 1 << ": ";

		double C, F, X;
		cin >> C >> F >> X;
		int z = ceil((F*(X - C) - 2*C)/C/F);
		z = max(z, 0);
		double ans = X/(2 + z*F); 
		for(i = 0; i < z; ++i)
			ans += C/(2 + i*F);

		
		printf("%.8lf", ans);

		cout << endl;
	}

	return 0;
}