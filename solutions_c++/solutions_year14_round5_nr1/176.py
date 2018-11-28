

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
const int MAXN = 1001000;
long long sum[MAXN];
int A[MAXN];
int N;
int calc(long long need){
	int L = 0, R = N, mid, left;
	while(L<=R){
		mid = L+R>>1;
		if (sum[mid]>=need){
			left = mid;
			R = mid-1;
		}else {
			L = mid+1;
		}
	}
	return left;
}
int main(){
	int tt;
	int  p, q, r, s;
	scanf("%d",&tt);
	for (int tcas = 1; tcas<=tt; tcas++){
		scanf("%d%d%d%d%d",&N,&p, &q, &r, &s);
		
		for (int i = 1; i<= N; i++){
			A[i] = (1LL*(i-1)*p+q)%r+s;
			sum[i] = sum[i-1]+A[i];
		}
		long long need = sum[N]/3;
		int left = calc(need);
		need = sum[N]/3*2;
		int right = calc(need);
		int bound = 1000;
		double ans = 0;
		for (int L = max(1, left-bound); L< min(N, left+bound); L++)
			for (int R = max(L, right-bound); R< min(N, right+bound); R++)
			if (L<=R){
				long long get = sum[L-1];
				get = max(sum[R]-sum[L-1], get);
				get = max(sum[N]-sum[R], get);
				ans = max(ans, (sum[N]-get)*1.0/sum[N]);
			}
		printf("Case #%d: %.11lf\n", tcas, ans);
	}
}
		
		
		
