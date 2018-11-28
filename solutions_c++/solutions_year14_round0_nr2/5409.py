#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm> 
#include <iostream> 
#include <string.h> 
#include <stdlib.h> 
#include <sstream> 
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define inf (1ll * 1e9 * 1e3)
#define eps 1e-9
using namespace std;


int main()
{
	freopen("i.in", "rt", stdin);
	freopen("o.out", "wt", stdout);
	int t, test = 0;
	double c, f, x;
	cin >> t;
	while(t--)
	{
		test++;
		scanf("%lf %lf %lf", &c, &f, &x);
		double perSecond = 2, time = 0, res = x / perSecond;
		int iters = 1e8;
		while(iters--)
		{
			time += c / perSecond;
			perSecond += f;
			res = min(res, time + x / perSecond);
		}
		printf("Case #%d: %.7lf\n", test, res);
	}
}