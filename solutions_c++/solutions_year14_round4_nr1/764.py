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

void init () {
}

int N, X, S[15005];

void solve () {
	scanf("%d%d", &N, &X);
	for(int i = 1; i <= N; i++) scanf("%d", S+i);
	sort(S+1, S+N+1);

	int res = 0;
	for(int i = N; i > 0; i--) if(S[i] >= 0) {
		int x = -1;
		for(int j = i-1; j > 0 && x == -1; j--) if(S[j] >= 0 && S[i] + S[j] <= X) x = j;
		S[i] = -1;
		if(x > 0) S[x] = -1;
		++res;
	}

	printf("Case #%d: %d\n", TCC, res);
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