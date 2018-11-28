#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

long long find(long long n)
{
	long long i;
	for(i = 2;i * i <= n;i++)
		if(n % i == 0)
			return i;
	return -1;
}

long long b10(char str[], int n, int base)
{
	int i;
	long long sum = 0, pow = 1;
	for(i = n - 1;i >= 0;i--){
		sum += pow * (str[i] - '0');
		pow *= base;
	}
	return sum;
}

void next(char str[], int n)
{
	int idx = n - 2;
	while(idx >= 0 && str[idx] != '0'){
		str[idx--] = '0';
	}
	str[idx] = '1';
}

int main()
{
	int t, caseNum = 1, n, jj, ans = 0, i;
	long long qq, qq2, ans_arr[11];
	char num[35];
	scanf("%d", &t);
	while(t--){
		scanf("%d%d", &n, &jj);
		num[0] = num[n - 1] = '1';
		for(i = 1;i < n - 1;i++)
			num[i] = '0';
		num[n] = 0;
		printf("Case #%d:\n", caseNum++);
		while(jj){
			for(i = 2;i <= 10;i++){
				qq = b10(num, n, i);
				qq2 = find(qq);
				//printf("b10 = %lld, divisor = %lld\n", qq, qq2);
				if(qq2 != -1)
					ans_arr[i] = qq2;
				else
					break;
			}
			if(i == 11){
				printf("%s", num);
				for(i = 2;i <= 10;i++)
					printf(" %lld", ans_arr[i]);
				printf("\n");
				jj--;
			}
			next(num, n);
		}
	}
	return 0;
}
