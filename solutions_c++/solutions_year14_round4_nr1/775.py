#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <ctime>
using namespace std;

#define rep(i, n) for (int i=0; i<(n); ++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define repd(i, a, b) for (int i=(a); i>=(b); --i)
#define clr(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define sz(a) ((int)(a).size())

#define M 700

int i,j,k,m,n,l;
int a[M+10];

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int ts;
	scanf("%d", &ts);
	repf(te, 1, ts){
	scanf("%d%d", &n, &m);
		
		clr(a, 0);
		rep(i, n) scanf("%d", &k), a[k]++;

		int ans=0;
		repf(i, 1, m) while (a[i]){
			a[i]--;
			j=m-i;
			ans++;
			while (j>=0 && !a[j]) --j;
			if (a[j]) --a[j];
		}

		printf("Case #%d: %d\n", te, ans);
	}
	return 0;
}
