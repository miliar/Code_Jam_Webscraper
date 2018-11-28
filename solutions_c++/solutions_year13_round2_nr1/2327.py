#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

#define ll __int64
#define sz 105

ll min(ll a, ll b){
	if(a > b)
		return b;
	return a;
}

typedef struct{
	ll n;
}data;

data a[sz];

int comp(const void *a, const void *b){
	data *x = (data *)a;
	data *y = (data *)b;

	return x->n - y->n;
}

ll n;

int dp(int i, int sum){
	if(i == n)return 0;
	if(sum > a[i].n)
		return dp(i+1, sum+a[i].n);
	else{
		if(sum != 1)
			return min(1 + dp(i, sum+sum-1), 1 + dp(i+1, sum));
		else
			return 1 + dp(i+1, sum);
	}
}


int main(){

	freopen("inp.txt", "r", stdin);
	freopen("o.txt", "w", stdout);

	ll t,sum,i,cas = 1;

	scanf("%I64d",&t);
	while(t--){
		scanf("%I64d %I64d",&sum, &n);
		for(i = 0; i < n; i++){
			scanf("%I64d",&a[i]);
		}
		qsort(a, n, sizeof(data), comp);
		printf("Case #%I64d: %I64d\n",cas++,dp(0,sum));
	}

	return 0;
}