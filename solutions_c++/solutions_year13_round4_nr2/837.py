#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>

#define LL long long int
#define FOR(i, s, e) for (int i=(s); i<(e); i++)
#define FOE(i, s, e) for (int i=(s); i<=(e); i++)
#define CLR(x, a) memset(x, a, sizeof(x))

using namespace std;

int test, n, y;
LL m, H, T, S, low, high, mid, t;

LL low_rank(int n, LL p){
	if (p == 0) return 0;
	else return (1<<(n - 1)) + low_rank(n - 1, (p - 1)/2);
}

LL high_rank(int n, LL p){
	if (p == (1LL<<n) - 1) return 0;
	else return (1<<(n - 1)) + high_rank(n - 1, (p + 1)/2);
}

int main(){
	scanf("%d", &test);
	FOE(tc, 1, test){
		scanf("%d%I64d", &n, &m);
		H = 0;
		T = (1LL<<n) - 1;
		low = high = 0;
		// low
		while (T >= H){
			mid = (T + H) >> 1;
			S = low_rank(n, mid);
			if (S < m){
				low = max(mid, low);
				H = mid + 1;
			}
			else T = mid - 1;
		}
		// high
		H = 0;
		T = (1LL<<n) - 1;
		
		while (T >= H){
			mid = (T + H) >> 1;
			S = (1LL<<n) - high_rank(n, mid);
			
			if (S <= m){
				high = max(high, mid);
				H = mid + 1;
			}
			else T = mid - 1;
		}
		
		printf("Case #%d: %I64d %I64d\n", tc, low, high);
		
	}
	return 0;
}
