#include <stdio.h>
#include <string.h>

int n;
int j;
int num[40];
long long div[15];

void init()
{
    memset(num, 0, sizeof(num));
    num[n-1] = 1;
    num[0] = 1;
    puts("Case #1:");
}

long long is_prime(long long x) 
{
    for (long long i = 2; i*i <= x; i++) {
        if (x % i == 0) {
            return i;
        }
    }
    return 0;
}

int check(int x) 
{
    long long t = 0;
    for (int i = n - 1; i >= 0 ; i--) {
        t *= x;
        if (num[i]) {
            t ++;
        }
    }
    div[x] = is_prime(t);
    return div[x];
}

int calc()
{
    num[1] ++;
    for (int i = 1; num[i] > 1; i++) {
        num[i] = 0;
        num[i + 1]++;
    }
    for (int i = 2; i <= 10; i++) {
        if (!check(i)) {
            return 0;
        }
    }
    return 1;
}

int main()
{
    scanf("%*d%d%d", &n, &j);
    init();
    while (j--) {
        while(!calc());
        for (int i = n-1; i >= 0; i--) {
            printf("%d", num[i]);
        }
        for (int i = 2; i <= 10; i++) {
            printf(" %lld", div[i]);
        }
        puts("");
    }
	return 0;
}

