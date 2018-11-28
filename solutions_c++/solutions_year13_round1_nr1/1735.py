#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <climits>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
const int MOD =1e9 + 7;
const int INF = 0x3f3f3f3f;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int kas=1;kas<=T;++kas)
	{
		LL ans;
		LL r,t;
		scanf("%lld%lld",&r,&t);
		long double da=sqrtl((2*r-1)*(2*r-1)+8*t);
		da+=1-2*r;
		ans=da/4;
		printf("Case #%d: %lld\n",kas,ans);
	}
	
	return 0;
}
