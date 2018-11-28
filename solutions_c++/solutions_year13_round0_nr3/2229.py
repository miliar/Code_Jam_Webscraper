#include <stdio.h>
#include <math.h>
#include <string.h>
#include <set>

using namespace std;

int fair(long long x)
{
	int n = 0, i = 0;
	int set[105];
	while(x > 0){
		set[n++] = x % 10;
		x /= 10;
	}
	n--;
	while(i < n){
		if(set[i] != set[n])
			return 0;
		i++;
		n--;
	}
	return 1;
}

int main()
{
	int count = 0, c = 1;
	long long n, i, a, b, table[39];
	for(i = 1;i <= 10000000;i++){
		if(fair(i) && fair(i * i)){
			table[count++] = i * i;
		}
	}
	scanf("%lld", &n);
	while(n--){
		scanf("%lld%lld", &a, &b);
		count = 0;
		for(i = 0;i < 39;i++){
			if(table[i] >= a && table[i] <= b)
				count++;
		}
		printf("Case #%d: %d\n", c++, count);
	}
	return 0;
}