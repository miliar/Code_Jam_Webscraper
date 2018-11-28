#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int n,t,m;
typedef long long ll;

int soma[10000005];
char num[15];

bool test(ll a){
	sprintf(num, "%lld", a);
	int s = strlen(num);
	int s2 = s--/2;
	for(int j = 0; j < s2; ++j) if(num[j] != num[s-j]) return false;
	return true;
}

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	
	for(ll i = 1; i < 10000004; ++i){
		soma[i] = soma[i-1];
		if(test(i) && test(i*i)) ++soma[i];
	}
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		ll a,b;
		scanf("%lld %lld", &a, &b);
		a = ceil(sqrt(a));
		b = floor(sqrt(b));
		printf("Case #%d: %d\n", _, soma[b]-soma[a-1]);
	}
	return 0;
}
