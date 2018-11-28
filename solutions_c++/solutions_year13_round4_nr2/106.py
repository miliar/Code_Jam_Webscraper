#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<complex>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)
// #define dprintf(...)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}

LL n, p;
LL howfar(LL x, LL nn){
	while(nn>0){
		if(!(x&1LL)){
			x>>=1;
		}else{
			if(x == (1LL<<nn) - 1) return x;
			x >>= 1;
			x++;
		};
		nn--;
	};
	return x;
};

LL _binary_search(LL left, LL right){
	if(right == left+1) return left;
	LL q = (right+left)/2;
	if(howfar(q, n) < p) return _binary_search(q, right);
	else return _binary_search(left, q);
};

LL binary_search(LL left, LL right){
	if(howfar(right, n) < p) return right;
	return _binary_search(left, right);
};

int main2(int cn){
	scanf("%lld %lld", &n, &p);
	if (p == (1LL<<n)){
		printf("Case #%d: %lld %lld\n", cn, p-1, p-1);
		return 7;
	};
	LL s=binary_search(0, (1LL<<n)-1);
	p = (1LL<<n) - p;
	LL q=binary_search(0, (1LL<<n)-1);
	q = (1LL<<n) - q - 2;
	printf("Case #%d: %lld %lld\n", cn, q, s);
	return 7;
};

int main() {
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; ++i) main2(i+1);
	return 0;
}

