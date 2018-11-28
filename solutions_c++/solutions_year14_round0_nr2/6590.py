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

int T;
double c, f, x, total;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d", &T);
	for (int casenum=0; casenum<T; casenum++)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		total = 0;
		double ans = x/2.0;
		int k = 1;
		while(true)
		{
			
			total = total + c/((k-1)*f+2);
			double next = total + x/(k*f + 2);
			if (next < ans) ans = next;
				else break;
			k = k + 1;
		}
		printf("Case #%d: %.7f\n", casenum+1, ans);
	}
}
