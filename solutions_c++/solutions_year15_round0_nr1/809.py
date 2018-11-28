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

const int N = 1005;
int n;
char str[N];
int main()
{
	int t, cas = 1;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d%s", &n, str);
		int sum = 0, ans = 0;
		for(int i = 0; i <= n; i++)
		{
			if(sum < i)
			{
				ans += i - sum;
				sum = i;
			}
			sum += str[i] - '0';
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
    return 0;
}
