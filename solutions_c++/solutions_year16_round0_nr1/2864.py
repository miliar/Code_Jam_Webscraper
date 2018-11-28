#ifndef _HEAD_H_
#define _HEAD_H_
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>

#define rep(i, n) for (int i=0; i<(n); ++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define repd(i, a, b) for (int i=(a); i>=(b); --i)
#define sz(a) ((int)(a).size())
#define SQR(x) ((x)*(x))

using namespace std;

template <class T> void checkmin(T &a, T b){ if (b<a) a=b; }
#endif
void solve(int n){
	if (n == 0){
		puts("INSOMNIA");
		return;
	}

	bool v[10];
	memset(v, 0, sizeof(v));
	int cnt = 0;
	
	int m = n;
	for(;;){
		int k = m;
		while (k){
			int i = k%10;
			if (!v[i]){
				++cnt;
				v[i] = 1;
			}
			k/=10;
		}

		if (cnt == 10){
			printf("%d\n", m);
			return;
		}
		m += n;
	}
}

int main(){
	int ts;
	scanf("%d", &ts);

	for (int te=1; te<=ts; ++te){
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", te);
		solve(n);
	}

	return 0;
}
