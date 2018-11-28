#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>

typedef long long int lli;
typedef long int li;

#define F(i, n) for(i = 0;i < n; ++i)
#define FI(i, st, ft) for(i = st;i <= ft; ++i)
#define pb(a, b) a.push_back(b)

using namespace std;

li normal(double a[1024], double b[1024], li n)
{
	li i, ans = 0, ft = n - 1;
	for(i = n - 1;i >= 0; --i){
		if(a[i] > b[ft]){
			++ans;
		}
		else{
			--ft;
		}
	}
	return ans;
}

li deceit(double a[1024], double b[1024], li n)
{
	li i, j = 0, ans = 0;
	F(i, n){
		while(a[j] < b[i] && i < n) ++j;
		if(j < n) ++ans;
		++j;
	}
	return ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	li t, cnt = 1;	
	cin >> t;
	while(t--){
		double a[1024], b[1024];
		li i, n;
		cin >> n;
		F(i, n){
			scanf("%lf", &a[i]);
		}
		F(i, n){
			scanf("%lf", &b[i]);
		}
		sort(&a[0], &a[n]);
		sort(&b[0], &b[n]);
		printf("Case #%ld: ", cnt); 
		cout << deceit(a, b, n) << " " << normal(a, b, n) << "\n";
		++cnt;
	}
	return 0;
}
