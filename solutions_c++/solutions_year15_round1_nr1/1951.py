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
#include <climits>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

int n,m[1010];

int solve1()
{
	int ret=0;
	for (int i = 0; i < n-1; ++i) {
		// cout<<m[i]<<" "<<m[i+1]<<endl;
		if(m[i]>=m[i+1])
			ret+=(m[i]-m[i+1]);
		// cout<<ret<<endl;
	}
	return ret;
}

int solve2()
{
	int rate=0,ret=0;
	for (int i = 0; i < n-1; ++i) {
		if(m[i]>=m[i+1])
			rate = max(rate,m[i]-m[i+1]);
	}
	// cout<<rate<<endl;
	for (int i = 0; i < n-1; ++i) {
		// if(i!=n-2)
			ret+=min(m[i],rate);
		// else {
		// 	ret+=rate;
		// }
		// cout<<ret<<endl;
	}

	return ret;
}

int main()
{
	int t;
	cin>>t;
	for (int T = 1; T <= t; ++T) {
		cin>>n;
		for (int i = 0; i < n; ++i){
			cin>>m[i];
		}
		int ans1 = solve1();
		int ans2 = solve2();
		printf("Case #%d: %d %d\n",T,ans1,ans2);
	}
	return 0;
}