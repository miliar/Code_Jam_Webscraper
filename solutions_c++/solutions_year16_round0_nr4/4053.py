#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

vector<long long> vv;
int main()
{
	freopen("input.txt","r", stdin);
	freopen("o.txt","w", stdout);

	long long a, b, c, cc,k, s, i,j, prdt, tests, ans;

	cin >> tests;

	for(int test = 1;test<=tests;test++)
	{
		cin >> k >> c >> s;

		vv.clear();
		prdt = 1;


		for(i = 1;i<c;i++) prdt = prdt*k;

		cc = min(k,c);

		int mincnt = 1;

		if(k>=c) mincnt = k-c+1;

		if(s < mincnt) {
			printf("Case #%d: IMPOSSIBLE\n", test);
			continue;
		}

		long long sum = 0;
		for(int level = 1; level < cc; level++)
		{
			//printf("level = %lld\n", level);
			sum = k*(sum + level-1);
		}

		sum += cc;
		//printf("sum = %lld, cc = %d .... k = %d\n",sum, cc, k);
		vv.push_back(sum);

		for(i = cc+1;i<= k;i++)
			vv.push_back(1+(i-1)*prdt);

		printf("Case #%d: ", test);
		for(i = 0;i<vv.size();i++)
			printf("%lld ", vv[i]);

		printf("\n");
	}

	return 0;

}
