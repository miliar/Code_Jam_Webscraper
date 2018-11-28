#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <bitset>

typedef long long LL;
#define pb push_back
#define MPII make_pair<int, int>
#define PII pair<int, int>
#define sz(x) (int)x.size()

using namespace std;

template<class T> T abs(T x){if (x < 0) return -x; else return x;}

int tot, a[20], prime[100], ans;

void getPrime(){
	tot = 0;
	for (int i = 2; i <= 100; ++i){
		bool f = true;
		for (int j = 2; j < i; ++j)
			if (i % j == 0){
				f = false;
				break;
			}
		if (f){
			prime[tot++] = i;
		}
	}
}

void check(){
	bool ok = true;
	vector<int> vec;
	vec.clear();
	for (int i = 2; i <= 10; ++i){
		LL tmp = 1, x = 0;
		for (int j = 0; j < 16; ++j){
			if (a[j]) x += tmp;
			tmp = tmp * (LL)i;
		}
		bool f = false;
		for (int j = 0; j < tot; ++j)
			if (x % prime[j] == 0){
				f = true;
				vec.push_back(prime[j]);
				break;
			}
		if (!f){
			ok = false;
			break;
		}
	}
	if (ok){
		ans += 1;
		for (int i = 15; i >= 0; --i)
			printf("%d", a[i]);
		for (int i = 15; i >= 0; --i)
			printf("%d", a[i]);
		for (int i = 0; i < sz(vec); ++i)
			printf(" %d", vec[i]);
		printf("\n");
	}
}

void dfs(int u){
	if (ans == 500) return;
	if (u == 15){
		check();
		return;
	}
	a[u] = 0;
	dfs(u + 1);
	a[u] = 1;
	dfs(u + 1);
}

int main(){
	freopen("C_big.out", "w", stdout);
	getPrime();
	printf("Case #1:\n");
	a[0] = 1; a[15] = 1; ans = 0;
	dfs(1);
	return 0;
}

