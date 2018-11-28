

#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;

void work()
{
	double c,f,x;
	double res = 0;
	double curV = 2;
	cin>>c>>f>>x;
	while(x/curV > c/curV + x/(curV+f))
	{
		res += c/curV;
		curV += f;
	}
	res += x/curV;
	printf("%.7f",res);
}

int main()
{
	freopen("a2.in", "r", stdin);
	freopen("a2.out", "w", stdout);

	int t2;
	cin >> t2;
	for (int t1 = 1; t1 <= t2; ++t1) {
		printf("Case #%d: ", t1);
		work();
		printf("\n");
	}

	return 0;
}

