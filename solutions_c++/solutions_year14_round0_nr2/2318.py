#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <iterator>

#define MOD 1000000007
#define INF 1000000000000000000
#define PI acos(-1)

using namespace std;

int main()
{
//	freopen("input.in","r",stdin);
//	freopen("output.in","w",stdout);
	int t,y;
	scanf("%d",&t);
	y = 1;
	while (t --) {
		int i;
		double c,f,x,div,ans,time,extra;
		scanf("%lf%lf%lf",&c,&f,&x);
		div = 2.0;
		ans = x / div;
		time = 0.0;
		for (i = 0; ; i++) {
			time = time + c / div;
			div = div + f;
			extra = x / div;
			if (time + extra <= ans) {
				ans = time + extra;
			} else {
				break;
			}
		}
		printf("Case #%d: %0.7lf\n",y,ans);
		y++;
	}
	return 0;
}
