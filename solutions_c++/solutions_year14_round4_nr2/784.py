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
#define N 1000

int i,j,k,m,n,l;
int a[N+10];

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int ts;
	scanf("%d", &ts);
	repf(te, 1, ts){
		scanf("%d", &n);
		set<int> st;
		rep(i, n) scanf("%d", &a[i]);



		int ans=0;
		while (n--){
			++n;
			k=0;

			rep(j, n) if (a[j]<a[k]) k=j;
			ans+=min(k, n-1-k);

			repf(j, k+1, n-1) a[j-1]=a[j];

			--n;
		}
		printf("Case #%d: %d\n", te, ans);
	}
	return 0;
}
