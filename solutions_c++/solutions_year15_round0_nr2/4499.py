#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <memory.h>
#include <stdlib.h>
#include <time.h>

typedef long long ll;

const int N = 1e5+3;
const int inf = 1e9;

using namespace std;

int a[N], b[N];
int ans;

void rec(int v, int n)
{
	if (v==n) {
		int mx=0, c=0;
		for(int i=0;i<n;++i) {
			c += b[i];
			mx = max(mx, (a[i] + b[i]) / (b[i] + 1));
		}
		ans = min(ans, mx + c);
		return;
	}
	
	for(int i=0;i<a[v];++i){
		b[v] = i;
		rec(v+1, n);
		b[v] = 0;
	}
}
int solve()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;++i)
		scanf("%d", &a[i]);
	
	ans = inf;
	memset(b, 0, n * sizeof(b[0]));
	rec(0, n);
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	int t;
	scanf("%d",&t);
	for(int i = 0; i < t; ++i)
		printf("Case #%d: %d\n", i+1, solve());
	return 0;
}