#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

#define Fr(a,b,c) for(int a = b; a < c; ++a)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define oo 0x3F3F3F3F

#define dbg if(0)

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long rash;

ull r, ink;

ull f(ull x) { return (x * (x + 1)) >> 1; }
int main() {
	int t, caso = 0; scanf("%d", &t);
	while(t--) {
		scanf("%llu%llu", &r, &ink);
		++r;
		ull a = ink / (2 * r);
		ull b = (ull) sqrt(ink + 0.0);
		
		ull ini = 1, fim;
		if(a < b) fim = a;
		else fim = b;
		
		fim += 3;
		
		#define test(x) ((x) * (2 * r - 1LL) + 4 * f((x) - 1LL))
		while(fim - ini > 1) {
			ll meio = (ini + fim) >> 1;
			if(test(meio) <= ink) ini = meio;
			else fim = meio;
		}

		while(test(fim) <= ink) ++fim;
		while(test(fim) > ink) --fim;
		
		printf("Case #%d: %llu\n", ++caso, fim);
	}
	
	return 0;
}


