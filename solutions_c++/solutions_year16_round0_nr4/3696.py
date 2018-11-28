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

int main()
{
	freopen("D-small-attempt0.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long i,j,k,c,s,p,cases,ans;
	vector<long long> v;

	scanf("%lld",&cases);

	for(int t = 1;t<=cases;t++)
	{
		scanf("%lld%lld%lld",&k,&c,&s);
		v.clear();
		p = 1;
		for(i = 1;i<=c-1;i++)
			p = p*k;

		v.push_back(1);
		for(i = 1;i<s;i++)
			v.push_back(1+i*p);

		//printf("p = %lld ..... v.size() = %lld\n",p, v.size());
		printf("Case #%d: ", t);
		for(i = 0;i<s;i++) printf("%lld ", v[i]);
		printf("\n");
	}

	return 0;

}
