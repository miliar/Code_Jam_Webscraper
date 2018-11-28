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
#define N 1000
char s[N+10];

void solve(){
	int n = strlen(s);
	string ret;
	string tmp = "A";

	for (int i=0; i<n; ++i){
		tmp[0] = s[i];
		if (ret.size()==0 || s[i]>=ret[0])
			ret = tmp + ret;
		else
			ret = ret + tmp;
	}
	cout<<ret<<endl;
}

int main(){
	int ts;
	scanf("%d\n", &ts);

	for (int te=1; te<=ts; ++te){
		gets(s);	
		printf("Case #%d: ", te);
		solve();
	}
	return 0;
}
