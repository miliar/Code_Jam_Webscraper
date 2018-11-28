#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long i64;

int nums[] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002 };

int main()
{
	int t; scanf("%d",&t);
	for(int k = 1; k <= t; ++k) {
		i64 a, b, cnt = 0;
		scanf("%lld %lld",&a, &b);
		a = ceil(sqrt(a)), b = (i64)sqrt(b);
		for(int i = 0; i < 39; ++i) {
			if(nums[i] >= a && nums[i] <= b) cnt++;
		}
		printf("Case #%d: %d\n",k,cnt);
	}
	return 0;
}
