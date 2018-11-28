#include <cstdio>
#include <cstring>

const long long list[20] = {0, 0, 19ll, 109ll, 199ll,
							1099ll, 1999ll, 10999ll, 19999ll, 109999ll,
							199999ll, 1099999ll, 1999999ll, 10999999ll, 19999999ll};


long long count(long long n){
	char s[20];
	long long d = 1;
	for (; d * 10 <= n; d *= 10);
//	printf("%I64d\n", d);
	if (d == n)
		return 0;
	sprintf(s, "%I64d", n);
	int len = strlen(s);
	long long high = 0, low = 0;
	long long k = 1;
	int l, r;
	for (l=0,r=len-1;l<r;++l,--r,k*=10){
		high += (s[l] - '0') * k;
		low += (s[r] - '0') * k;
	}
	if (l == r)
		low += (s[l] - '0') * k;

	if (low != 0){
		if (high == 1)
			return low;
		else
			return high + low;
	}
	else
		return count(n - 1) + 1;
}

long long n;
int len;
char s[20];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi=1;casi<=cas;++casi){
		printf("Case #%d: ", casi);
		scanf("%s", s);
		sscanf(s, "%I64d", &n);
		len = strlen(s);
		if (strlen(s) == 1)
			puts(s);
		else if (n <= 20)
			printf("%I64d\n", n);
		else{
			long long ans = 10;
			long long j = 1;
			for (int i=2;i<len;++i, j *= 10)
				ans += list[i];
			printf("%I64d\n", ans + count(n));
//			printf("%I64d %I64d\n", ans, count(n));
/*			j *= 10;
//			printf("%I64d\n", ans);
			if (n / j == 1 && n % j == 0)
				printf("%I64d\n", ans);
			else if (n % j == 0){
				ans += n / j - 1 - (n / j == 2);
				ans += j;
				printf("%I64d\n", ans);
			}
			else{
				long long k = 1, high = 0, low = 0;
				int l, r;
				for (l=0,r=len-1;l<r;++l,--r,k*=10){
					high += (s[l] - '0') * k;
					low += (s[r] - '0') * k;
				}
				if (l == r)
					low += (s[r] - '0') * k;
//				printf("%I64d %I64d %d %d\n", high, low, l, r);
				if (n / j == 1 && high == 1)
					printf("%I64d\n", ans + low);
				else if (low == 0){
					k = 1;
					int i;
					for (i=len/2-1;i>=0 && s[i] == '0';--i);
					--s[i];
					for (;i>0;--i)
						k *= 10;
					high -= k;
					long long n1;
					sscanf(s, "%I64d", &n1);
					printf("%I64d\n", ans + high + n - n1 - 1);
				}
				else
					printf("%I64d\n", ans + low + high);
			}*/
		}
	}
	return 0;
}
