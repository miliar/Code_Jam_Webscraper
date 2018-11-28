/*
 * Problem: 
 * Link: 
 * Author: 
 * Handle: 
 * State: 
 * Date: 
 * Comments: 
 */
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
using namespace std;
#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 2000000000
#define EPS 		1e-8
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define F(i,a)      FOR(i,0,a)
#define PB          push_back
#define S           size()
#define MP          make_pair
#define MS(v, x)	memset(v, x, sizeof v)
#define ALL(v)      v.begin(),v.end()
#define LLA(v)      v.rbegin(),v.rend()
#define fi          first
#define se          second
#define NL 			printf("\n")
#define SP 			system("pause")
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)
const double PI = acos(-1.0);
#define BitSet(arg,posn) ((arg) | (1L << (posn)))
#define BitClr(arg,posn) ((arg) & ~(1L << (posn)))
#define BitTst(arg,posn) bool((arg) & (1L << (posn)))
#define BitFlp(arg,posn) ((arg) ^ (1L << (posn)))
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef long long   LL;

void run() {
	LL n = in() * 1LL;
	if(n == 0LL) {
		printf("INSOMNIA\n");
		return;
	}
	LL mask = (1LL << 10) - 1LL;
	LL ans = 0LL;
	LL rep = 0LL;
	while(ans != mask) {
		rep += 1LL;
		if(n > INF_LL / rep) {
			printf("INSOMNIA\n");
			return;
		}
		LL copy = n * rep;
		int digit;
		while (copy != 0LL) {
			digit = copy % 10LL;
			copy /= 10LL;
			ans |= (1LL << digit);
		}
	}
	printf("%lld\n", n * rep);
}

int main() {
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	int n = in();
	FOR(i, 1, n+1) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}