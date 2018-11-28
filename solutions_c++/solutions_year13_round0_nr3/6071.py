#include <cstdio>

#define MAXN 100000

int palin(long long int n) {
    int num[20];
    int k = 0;
    while(n > 0) {
        num[k++] = n%10;
        n /= 10;
    }
    for(int i = 0;i <= (k/2-!(k%2));i++) {
        if(num[i] != num[k-1-i]) return 0;
    }

    return 1;
}

int main() {
    long long int num[MAXN];
    int n = 0;

    for(int i = 1;i <= 10000000;i++) {
        if(!palin((long long int) i)) continue;
        long long int j = (long long int)(i*i);
        if(palin(j)) num[n++] = j;
    }

	int t;
	scanf("%d",&t);
	for(int k = 1;k <= t;k++) {
        long long int a,b;
        scanf("%lld %lld",&a,&b);
        int i,j;
        for(i = 0;i < n;i++)
            if(num[i] >= a) break;
        j = i;
        for(;j < n;j++)
            if(num[j] > b) break;
        printf("Case #%d: %d\n",k,j-i);
	}
	return 0;
}
