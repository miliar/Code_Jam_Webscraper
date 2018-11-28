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
void solve(int k, int c, int s){
	long long delta = 1;
	for (int i=0; i<c-1; ++i)
		delta = delta * k;

	long long ans = 1;
	cout<<ans;
	for (int i=0; i<s-1; ++i){
		ans += delta;
		cout<<' '<<ans;
	}
	cout<<endl;
}

int main(){
	int ts;
	scanf("%d", &ts);
	for (int te=1; te<=ts; ++te){
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d: ", te);
		solve(k, c, s);
	}
	return 0;
}
