#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>
using namespace std;
int T;
long long int N, M;
int Max = 0;

int main()
{
	freopen("..\\A-small-attempt0.in","r",stdin);
	freopen("..\\A-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T;t++)
	{
		long long int r, tt;
		scanf("%lld",&r);
		scanf("%lld",&tt);
		double aa = (double)((2 * r - 1) * (2 * r - 1)) + (double)((double)8 * (double)tt);
		double bb = sqrt(aa);
		long long int x = bb - (double)(2 * r) + 1;
		printf("Case #%d: %lld\n", t, x / 4);
	}
	return 0;
}