#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
using namespace std;

typedef long long ll;
ll T,K,C,S;
ll a[110];
ll qpow(ll x,int k) {
    ll ret = 1;
    while(k > 0) {
        if(k & 1) {
            ret *= x;
        }
        x *= x;
        k >>= 1;
    }
    return ret;
}

int main() {
//	#ifdef wotok
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
//	#endif
	scanf("%I64d",&T);
	int Case = 1;
	while(T --) {
        scanf("%I64d%I64d%I64d",&K,&C,&S);
        long long begin = qpow(K,C - 1);
        for (long long i = 0;i < S;i ++) {
            a[i] = i * begin + 1;
        }
        printf("Case #%d: ",Case ++);
        for (int i = 0;i < S;i ++) {
            printf("%I64d%s",a[i],i == S - 1? "\n" : " ");
        }
	}

}


