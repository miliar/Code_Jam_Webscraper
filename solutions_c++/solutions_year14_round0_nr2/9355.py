#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define pb push_back
#define fs first
#define sc second
#define openfile {freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);}
#define debug 01

const double eps = 1e-8;
double C, F, X;

bool isLarger(double a, double b)
{
	return a - b > eps;
}

void solve()
{
	double res1 = X / 2.0, res2, V = 2.0, sumTime = 0.0;
	do
	{
		res2 = sumTime + C / V + X / (V + F);
		if (isLarger(res2, res1))
			break;
		sumTime += C / V;
		V += F;
		res1 = res2;
	} while (1);
	printf("%.7lf\n", res1);
}

int main()
{
   if (debug) openfile;

	int te;
	scanf("%d", &te);
	for (int t = 1; t <= te; t++)
	{
		cin >> C >> F >> X;
		printf("Case #%d: ", t);
		solve();
	}

   return 0;
}
