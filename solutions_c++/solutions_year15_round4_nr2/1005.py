#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;

#define eps 1e-8
#define PB push_back
#define LL long long
#define INF 0x3f3f3f3f

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}

const int N = 105;
int n;
double R[N], C[N], V, X;
int main()
{
	int t, cas = 1;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d%lf%lf", &n, &V, &X);
		for(int i = 1; i <= n; i++)
			scanf("%lf%lf", &R[i], &C[i]);
		printf("Case #%d: ", cas++);
		if(n == 1)
		{
			if(fabs(C[1] - X) < eps)
				printf("%.9lf\n", V / R[1]);
			else
				printf("IMPOSSIBLE\n");
		}
		else
		{
			if(fabs(C[1] - X) < eps && fabs(C[2] - X) < eps)
				printf("%.9lf\n", V / (R[1] + R[2]));	
			else if(fabs(C[1] - X) < eps)
				printf("%.9lf\n", V / R[1]);
			else if(fabs(C[2] - X) < eps)
				printf("%.9lf\n", V / R[2]);
			else if(max(C[1], C[2]) + eps < X || min(C[1], C[2]) - eps > X)
				printf("IMPOSSIBLE\n");
			else
			{
				double t2 = V / R[2];
				double t1 = t2 * R[2] * (X - C[2]) / R[1] / (C[1] - X);
				double v = t1 * R[1] + t2 * R[2];
				// double x = (t1 * R[1] * C[1] + t2 * R[2] * C[2]) / v;
				// if(fabs(x - X) > eps)
				// 	cout << "error:" << x << " " << X << endl;
				//cout << v << " " << x << " " << max(t1, t2) << endl;
				double ans = max(t1, t2) * V / v;
				printf("%.9lf\n", ans);
			}
		}
	}
    return 0;
}
/*
5
1 10.0000 50.0000
0.2000 50.0000

2 30.0000 65.4321
0.0001 50.0000
100.0000 99.9000

2 5.0000 99.9000
30.0000 99.8999
20.0000 99.7000

2 0.0001 77.2831
0.0001 97.3911
0.0001 57.1751

2 100.0000 75.6127
70.0263 75.6127
27.0364 27.7990
*/
