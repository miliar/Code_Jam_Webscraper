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

#define raiz 10000005
ll ar[raiz + 5];
char str[raiz];
bool palind(ll x) {
	sprintf(str, "%lld", x);
	int len = strlen(str);
	for(int i = 0; i < len; ++i) if(str[i] != str[len - i - 1]) return false;
	return true;
}

int main() {
	int p = 0;
	for(ll i = 1; i <= raiz; ++i) if(palind(i) /**/ && palind(i * i) /**/) ar[p++] = i * i;
//	puts(""); Fr(i,0,p) printf("%lld\n", ar[i]); puts("");
	
	int t, caso = 0; scanf("%d", &t);
	while(t--) {
		ll a, b;
		scanf("%lld%lld", &a, &b);
		int c = 0;
		Fr(i,0,p) if(a <= ar[i] && ar[i] <= b) c++;
		printf("Case #%d: %d\n", ++caso, c);
	}
	
	return 0;
}


