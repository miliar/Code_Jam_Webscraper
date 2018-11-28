#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cstring>
#include <cmath>
#include <set>
#define maxl 1000000000
#define mod 1000000007
#define maxn 5010
#define maxs 150
using namespace std;

int calc(int n, int a[], int b[]){
	int now = 0, result = 0;
	for(int i = 0; i < n; ++i){
		while(now < n && a[now] < b[i]) ++now;
		if(now < n){
			++now;
			++result;
		}
	}
	return result;
}

int a[1100], b[1100];

void solve(){
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; ++i){
		double x;
		scanf("%lf", &x);
		a[i] = (int)(x * 10000000 + 0.1);
	}
	for(int i = 0; i < n; ++i){
		double x;
		scanf("%lf", &x);
		b[i] = (int)(x * 10000000 + 0.1);
	}
	sort(a, a + n);
	sort(b, b + n);
	printf("%d %d\n", calc(n, a, b), n - calc(n, b, a));
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}