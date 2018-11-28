#include <cstdlib>  
#include <cctype>  
#include <cstring>  
#include <cstdio>  
#include <cmath>  
#include <algorithm>  
#include <vector>  
#include <string>  
#include <iostream>  
#include <sstream>  
#include <map>  
#include <set>  
#include <queue>  
#include <stack>  
#include <fstream>  
#include <numeric>  
#include <iomanip>  
#include <bitset>  
#include <list>  
#include <stdexcept>  
#include <functional>  
#include <utility>  
#include <ctime>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MEM(a,b) memset((a),(b),sizeof(a))
const LL INF = 1000000007;
const int N = 1e2+10;
const double eps = 1e-12;
int cmp(double d)
{
	if (abs(d) < 1e-6) return 0;
	if (d>0) return 1;
	else return -1;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		int n;
		double v, x;
		cin >> n >> v >> x;
		if (n == 1)
		{
			double r, c;
			cin >> r >> c;
			if (abs(c - x) < 1e-6)
			{
				printf("Case #%d: %.15f\n", ks++, v / r);
				continue;
			}
			else printf("Case #%d: IMPOSSIBLE\n",ks++);
			continue;
		}
		if (n == 2)
		{
			double r1, c1;
			double r2, c2;
			cin >> r1 >> c1 >> r2 >> c2;
			if (cmp(c1-c2) == 1) swap(r1, r2), swap(c1, c2);
			if (cmp(c1 - x) == 1 || cmp(c2 - x) == -1)
			{
				printf("Case #%d: IMPOSSIBLE\n", ks++);
				continue;
			}
			if (cmp(c1- c2) == 0)
			{
				printf("Case #%d: %.15f\n", ks++, v / (r1+r2));
				continue;
			}
			double l, r;
			l = 0;
			r = v;
			while (abs(r - l) > eps)
			{
				double mid = (l + r) / 2;
				if ((mid*c1 + (v - mid)*c2) < v*x) r = mid;
				else l = mid;
			}
			printf("Case #%d: %.15f\n", ks++, max(l/r1,(v-l)/r2));
		}

	}
	return 0;

}