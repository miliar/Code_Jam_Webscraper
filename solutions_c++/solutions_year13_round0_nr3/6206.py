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

int digit[19];
int len;

bool is_palindrome(long long t){
	len=0;
	while(t>0){
		digit[len++] = t%10;
		t/=10;
	};

	for(int i=0; i<len; ++i) if(!(digit[i] == digit[len - i - 1])) return false;
	return true;
};

bool test(long long t){
	return is_palindrome(t) && is_palindrome(t*t);
};

#define MAXS 10000000

int res[MAXS];

LL binary_search(LL A, LL l, LL r){
	if(l+1 == r) {
		return l;
	}
	LL x=(l+r)/2;
	if(x*x <= A) return binary_search(A, x, r);
	else return binary_search(A,l,x);
};

void doit(int q) 
{
	long long A, B;
	scanf("%lld %lld", &A, &B);
	A = binary_search(A-1, 0, 15000000);
	B = binary_search(B, 0, 15000000);
	printf("Case #%d: %d\n", q, res[B] - res[A]);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i=1; i<MAXS; ++i) {
		res[i]=test(i) + res[i-1];
	};

	for(int i=1; i<=T; ++i)
		doit(i);
	return 0;
}

