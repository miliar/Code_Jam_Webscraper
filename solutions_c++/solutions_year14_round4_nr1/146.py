#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#define maxn 10010
#define mod 1000000007
using namespace std;
int a[110000];


void solve(){
	int n, x, i, left;
	scanf("%d%d", &n, &x);
	for(int i = 1; i <= n;++i){
		scanf("%d", &a[i]);
	}
	sort(&a[1], &a[n + 1]);
	left = 1;
	int ans = 0;
	for(int i = n; i >= left; --i){
		//cout<<a[i] + a[left]<<endl;
		if(left < i && a[i] + a[left] <= x) ++left;
		//cout<<a[i] + a[left]<<endl;
		++ans;
	}
	printf("%d\n", ans);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}