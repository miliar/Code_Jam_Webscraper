#include <cmath>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

#define FORALL(c,i) for(auto i = (c).begin(); i != (c).end(); ++i)
#define ALL(c) (c).begin(),(c).end() 
#define SORT(a) sort(a.begin(), a.end())
#define UNIQ(a) a.resize(unique(a.begin(), a.end()) - a.begin())

double r[999], c[999];
int n;
double v, x;

double solve1()
{
	if(n == 1)
	{
		if(x == c[0])
			return v / r[0];
		else
			return -1.0;
	}

	if(x < min(c[0],c[1]) || max(c[0],c[1]) < x)
		return -1;
	
	if(c[0] == c[1])
	{
		return v / (r[1] + r[0]);
	}

	// (V0X0 + V1X1) / V = x
	// v0 + v1 = V
	//(V0X0 + V1X1) = V*x
	//(V0*X0 + (V-V0)*X1) = V*x
	//V0*(x0-x1) + v*x1 = v*x
	//V0 = v*(x - x1) / (x0 - x1)
	double v0 = v*(x-c[1]) / (c[0]-c[1]);
	double v1 = v-v0;
	double t0 = v0/r[0];
	double t1 = v1/r[1];
	return max(t0, t1);
}

int main() {
	int t;

	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		cin >> n >> v >> x;
		for(int i=0; i<n; ++i)
			cin >> r[i] >> c[i];

		double res = 0;
		res = solve1();
		
		if(res < 0)
			cout << "Case #" << tt << ": " << "IMPOSSIBLE\n";
		else
		{
			cout << "Case #" << tt << ":";
			printf(" %.6lf\n", res);
		}
	}

	return 0;
}
