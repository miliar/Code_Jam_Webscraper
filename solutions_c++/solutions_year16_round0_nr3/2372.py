#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

long long base[11], num[11], ret[11];

long long doit(long long x){
	if (!(x&1)) return 2;
	int xx = (int)sqrt(x)+1;
	for (int o=3; o<=xx; o+=2)
	if (x % o == 0) 
		return o;
	return 0;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("a.out","w",stdout);
	int task, n, m;
	scanf("%d%d%d", &task, &n, &m);
	printf("Case #1:\n");
    long long firstDigit = (long long)1<<((long long)n-1);
	for (long long mask=0; mask<((long long)1<<((long long)n-2)); mask++){
		
		for (int i=2; i<=10; i++){
			base[i] = 1;
			num[i] = 0;
		}

		long long v = firstDigit + (mask<<1) + 1;
		
		for (long long y = v; y; y>>=1){
			for (int i=2; i<=10; i++){
				if (y&1) num[i] += base[i];
				base[i] *= i;
			}
		}

		bool valid = true;
		for (int i=2; i<=10; i++){
			ret[i] = doit(num[i]);
			if (!ret[i]){
				valid = false;
				break;
			}
		}

		if (!valid){
			continue;
		}
	
		for (long long i=n-1; i>=0; i--)
		if (v&(1<<i)){
			printf("1");
		}else{
			printf("0");
		}
		
		for (int i=2; i<=10; i++)
			printf(" %lld", ret[i]);
		printf("\n");
		
		if (!--m) break;
	}

	return 0;
}
