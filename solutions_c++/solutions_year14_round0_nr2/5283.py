#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <memory.h> 
#include <math.h> 
#include <assert.h> 
#include <stack> 
#include <queue> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <string> 
#include <functional> 
#include <vector> 
#include <deque> 
#include <utility> 
#include <bitset> 
#include <limits.h>  

using namespace std; 
typedef long long ll; 
typedef unsigned long long llu; 
typedef double lf;
typedef unsigned int uint;
typedef long double llf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
#define memset0(x) memset(x, 0, sizeof (x));
int TC, TCC;

double C, X, F;

void init () {
}

void solve () {
	scanf("%lf%lf%lf", &C, &F, &X);

	lf res = X / 2;
	lf sumt = 0;
	for(int farms = 0; farms < 100000; farms++) {
		res = min(res, sumt + X / (farms * F + 2.0));
		sumt += C / (farms * F + 2.0);
	}

	printf("Case #%d: %.7lf\n", TCC, res);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &TC);
	while(++TCC <= TC) {
		init();
		solve();
	}
	return 0;
}