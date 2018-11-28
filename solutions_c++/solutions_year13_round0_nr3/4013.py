#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
#include<string.h>
#include<string>
#include<math.h>
using namespace std;
bool check(long long n)
{
	int arr[20], k;
	k = 0;
	while(n) {
		arr[k++] = n % 10;
		n /= 10;
	}
	for(int i = 0; i < k; i++) {
		if(arr[i] != arr[k - i - 1]) return false;
	}
	return true;
}

int main()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("C.out.large-1", "w", stdout);
	int ans = 0, T;
	long long n, A, B;
	long long arr[1000];
	int k = 0;
	for(long long i = 1; i <= 10000000; i++) {
		n = i * i;
		if(check(i) == true && check(n) == true) {
            arr[k++] = n;
            //printf("%lld %lld\n", i, n);
            //ans++;
        }
	}
	scanf("%d", &T);
	for(int i = 1; i <= T; i++) {
        scanf("%lld%lld", &A, &B);
        int ans = 0;
        for(int j = 0; j < k; j++) {
            if(arr[j] >= A && arr[j] <= B) ans++;
        }
        printf("Case #%d: %d\n", i, ans);
    }
//	system("pause");
	return 0;
}
