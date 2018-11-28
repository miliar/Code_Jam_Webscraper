#pragma comment(linker, "/STACK:120000000")

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>


using namespace std;

typedef long long ll;
#define MAXN 200000

int a[MAXN];
int n, x;

int main(){
    int tc;
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
	
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
		scanf("%i %i", &n, &x);
		fprintf(stderr, "%i\n", tt);
        printf("Case #%i: ", tt);        
		for(int i=0; i<n; ++i) scanf("%i", &a[i]);
		sort(a, a + n);
		int best = n;
		for(int j=n-1; j>=0; --j) {
			bool ok = true;
			for(int i1=0, i2=j; i1<i2 && ok; ++i1, --i2) ok = ok && (a[i1] + a[i2] <= x);
			if (ok) {
				int tmp = (n - (j+1)) + (j+1)/2;
				if ((j+1) & 1) tmp++;
				best = min(tmp, best);
			}
		}
		printf("%i\n", best);
    }

    return 0;
}

