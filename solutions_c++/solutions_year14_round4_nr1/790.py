#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <ctime>
#include <stdint.h>

using namespace std;

int a[10001];

void Solve()
{
	int n, X;
	scanf("%d%d", &n, &X);
	for(int i = 0; i<n; ++i){
		scanf("%d", &a[i]);
	}
	sort(a, a+n);
	int ans = 0;
	int l = 0, r = n-1;
	while(l <= r){
		if(a[l]+a[r] <= X){
			l++;
			r--;
		}else{
			r--;
		}
		ans++;
	}
	printf("%d\n", ans);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}

