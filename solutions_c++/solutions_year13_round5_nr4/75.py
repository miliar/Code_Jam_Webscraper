#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
#include<cstring>
#include<set>
#include<ctime>
#include<cassert>


using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),(a).end()
int n;
int go(int x, int y) {
	for (int t = y; t < y + n; t++) {
		if (((x >> (t % n)) & 1) == 0) {
			return t % n;
		}
	}
	assert(false);
}
char s[100];
ld dp1[1 << 21];
ld dp2[1 << 21];
int main() {
	#ifdef home
    	freopen("a.in", "r", stdin);
	    freopen("a.out", "w", stdout);
	#endif
	int T;
	scanf("%d", &T);
    for (int ti = 1; ti <= T; ti++) {
    	printf("Case #%d: ", ti);
    	cerr<<ti<<endl;
    	scanf("%s", s);
    	n = strlen(s);
    	int msk = 0;
    	for (int i = 0; i < n; i++) {
    		if (s[i] == 'X') {
    			msk |= 1 << i;
    		}
    	}
    	for (int i = 0; i < (1 << n); i++) {
    		dp1[i] = 0;
    		dp2[i] = 0;
    	}
    	dp1[msk] = 1;
    	for (int i = 0; i < (1 << n) - 1; i++) {
    		if (dp1[i] > 0) {
    			for (int j = 0; j < n; j++) {
    				int nx = go(i, j);
//    				assert(((i >> nx) & 1) == 0 && n);
    				int cs = nx - j;
    				if (cs < 0) {
    					cs += n;
    				}
//    				cerr<<i<<" "<<j<<" "<<nx<<endl;			
    				dp1[i | (1 << nx)] += dp1[i];
    				dp2[i | (1 << nx)] += (n - cs) * dp1[i] + dp2[i];
    			}
    		}
    	}
//    	    	for (int i = 0; i < (1 << n); i++) {
  //  	    		cerr<<i<<" "<<dp1[i]<<" "<<dp2[i]<<endl;
    //	    	}
    	printf("%.18lf\n", (double)(dp2[(1 << n) - 1] * 1. / dp1[(1 << n) - 1]));
    }
	return 0;
}