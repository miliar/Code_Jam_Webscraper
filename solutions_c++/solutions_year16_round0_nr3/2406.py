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
#define N 11
#define M 16
#define L 100000000

long long x[N][M+10];
long long a[11];
bool v[L+10];
vector<long long> prime;


void init(){
	for (int i=2; i<=10; ++i){
		x[i][0] = 1;
		for (int j=1; j<=M; ++j)
			x[i][j] = x[i][j-1] * i;
	}

	for (int i=2; i<=L; ++i){
		if (!v[i]){
			for (int j=2; j<=L/i; ++j)
				v[i*j] = 1;
			prime.push_back((long long)i);
		}
	}
}


void solve(int n, int m){
	for (int i=(1<<(n-1)); i<(1<<n); ++i) if (i&1){

		memset(a, 0, sizeof(a));
		for (int j=0; j<n; ++j) if (i&(1<<j)){
			for (int k=2; k<=10; ++k)
				a[k] += x[k][j];
		}

		vector<long long> ans;

		for (int k=2; k<=10; ++k){
			for (int j=0; j<prime.size() && prime[j]*prime[j]<= a[k]; ++j)
				if (a[k] % prime[j]==0){
					ans.push_back(prime[j]);
					break;
				}
			if (ans.size() != k-1) break;
		}

		if (ans.size() == 9){
			cout<<a[10];
			for (int k=0; k<ans.size(); ++k)
				cout<<' '<<ans[k];
			cout<<endl;

			if (--m == 0)
				return;
		}
	}
}

int main(){
	init();
	int ts;
	scanf("%d", &ts);
	for (int te=1; te<=ts; ++te){
		int n, m;
		scanf("%d%d", &n, &m);
		printf("Case #%d:\n", te);
		solve(n, m);
	}
	return 0;
}
