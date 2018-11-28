#include<cstdio>
#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int T, N, J;
long long int in2, in3, in4, in5, in6, in7, in8, in9, in10;
bool* num;

long long int isPrime(long long int n){
	for (long long int i=2; i<sqrt(n)+1; ++i){
		if (n % i == 0) return i;
	}
	return 0;
}

long long int toBase (int base){
    long long int n = 0;
    for (int i = N-1; i >= 0; --i){
        if (num[i]){
            long long int temp = 1;
            for (int j = 0; j < N-1-i; ++j) temp*=base;
            n+=temp;
        }
    }
    return n;
}

int main(){
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    scanf("%d\n", &T);
    for (int t = 1; t <= T; ++t){
        scanf("%d %d\n", &N, &J);
        printf("Case #%d:\n", t);
        num = new bool [N]; num[0] = true; num[N-1] = true;
        int maxRange = pow(2, N-2)-1;
        int cnt = 0;
        for (int i = 0; i < maxRange, cnt < J; ++i){
            int temp = i;
            for (int j = N-2; j > 0; --j){
                int remainder = temp%2;
                if (remainder) num[j] = true;
                else num[j] = false;
                temp/=2;
            }
            in2 = isPrime(toBase(2)); in3 = isPrime(toBase (3)); in4 = isPrime(toBase (4)); in5 = isPrime(toBase (5)); in6 = isPrime(toBase (6)); in7 = isPrime(toBase (7)); in8 = isPrime(toBase (8)); in9 = isPrime(toBase (9)); in10 = toBase (10);
            long long int num10 = in10; in10 = isPrime(in10);
            if (in2 && in3 && in4 && in5 && in6 && in7 && in8 && in9 && in10){
                printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld %lld\n", num10, in2, in3, in4, in5, in6, in7, in8, in9, in10);
                ++cnt;
            }
        }
        delete [] num;
    }
}
