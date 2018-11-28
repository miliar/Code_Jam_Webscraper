#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define rep2(i,m,n) for(int i=(int)m;i<(int)n;i++)

bool isFair(char* str) {
    int len;
	for(len=0;str[len];len++);
	rep(i,len/2) if(str[i] != str[len-1-i]) return false;
	return true;
}

char* itoa(unsigned long long int num) {
    char str[20];
    sprintf(str, "%llu", num);
    return str;
}

int solution() {
	unsigned long long int A, B;
	unsigned long long int low, high;
	scanf("%llu %llu", &A, &B);
	low = (int)sqrt(A);
	high = (int)sqrt(B) + 1;
	int cnt = 0;
	for(long long int i = low; i < high; i++) {
		if(isFair(itoa(i)) && isFair(itoa(i*i)) && i*i >= A && i*i <= B) cnt++;
	}
	return cnt;
}

int main() {
	int tc;
	scanf("%d", &tc);
	rep(i,tc) {
		printf("Case #%d: %d\n", i+1, solution());
	}
}