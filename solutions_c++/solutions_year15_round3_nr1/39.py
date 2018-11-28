#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;

#define eps 1e-9
#define PB push_back
#define LL long long
#define INF 0x3f3f3f3f

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}


int main()
{
	int t, cas = 1;
	scanf("%d", &t);
	while(t--)
	{
		int r, c, w;
		scanf("%d%d%d", &r, &c, &w);
		int ans = r * (c / w) + w;
		if(c % w == 0)
			ans--;
		printf("Case #%d: %d\n", cas++, ans);
	}
    return 0;
}
