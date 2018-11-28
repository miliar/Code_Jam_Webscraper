/*************************************************************************
    > File Name: a.cpp
    > Author: james47
    > Mail: 
    > Created Time: Sat Apr  9 16:07:10 2016
 ************************************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long ll;
const int all = (1 << 10) - 1;

int checkbit(int n){
	int ret = 0;
	while(n){
		ret |= 1 << (n % 10);
		n /= 10;
	}
	return ret;
}

ll getlast(int n){
	int has = checkbit(n);
	ll fac = 1;
	while(has != all){
		fac ++;
		has |= checkbit(fac * n);
	}
	return fac * n;
}

int main()
{
	int T, cas = 0;
	scanf("%d", &T);
	while(T--){
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", ++cas);
		if (n == 0) puts("INSOMNIA");
		else printf("%lld\n", getlast(n));
	}
	return 0;
}
