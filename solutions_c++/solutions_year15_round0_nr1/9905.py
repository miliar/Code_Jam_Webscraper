#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <inttypes.h>

using namespace std;

#define _inline(f...) f() __attribute__((always_inline)); f

#define REP(i,n) for(int i = 0;i < n;++i)
#define FUP(i,a,b) for(int i = (a); i <= (b);++i)
#define FDOWN(i,a,b) for(int i = (a); i >= (b);--i)

#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))

#define ABS(x) ((x) < 0 ? -(x) : (x))

#define PB push_back
#define MP make_pair

const int INF = 0x3F3F3F3F ;
const int NULO = -1 ;
const double EPS = 1e-10 ;

_inline(int cmp)(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main(){

	int n_cases;
	int nums = 1;

	scanf("%d", &n_cases);
	while(n_cases--){
		int S_max;
		scanf("%d", &S_max);

		char S[ S_max + 1 ];
		scanf("%s", S);

		int friends = 0;
		int peeps = 0;

		REP(i, S_max + 1){
			if(S[ i ] != '0'){
				if(peeps < i){
					friends += (i - peeps);
					peeps += friends;
				}
			}
			peeps += (S[ i ] - '0');
		}

		printf("Case #%d: %d\n", nums++, friends);

	}

	return 0 ;
}

