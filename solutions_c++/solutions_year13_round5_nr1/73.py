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

ll B;
int n;
ll a[100];
ll b[100];
ld ans;
void calc(ll g) {
			ll sum = 0;
    		ll MN = 1e15;
    		for (int j = 0; j <= 36; j++) {
    			b[j] = max(0LL, g - a[j]);
    			sum += b[j];
    			MN = min(MN, a[j] + b[j]);
    		}
    		assert(sum <= B);
    		
    		    			int k = 0;
    			for (int j = 0; j <= 36; j++) {
    				if (a[j] + b[j] == MN) {
    					k++;
    				}
    			}
    			ld tk = -sum;
    			for (int j = 0; j <= 36; j++) {
    				if (a[j] + b[j] == MN) {
    					tk += b[j] * 36. / k;
    				}
    			}
    			ans = max(ans, tk);
    			

    		int ptr = 0;    		
    		for (int i = 36; i > 0; i--) {
    			if (a[i] + b[i] != MN) continue;
    			ptr++;
    			if (sum + ptr > B) continue;
    			b[i]++;
    			int k = 0;
    			for (int j = 0; j <= 36; j++) {
    				if (a[j] + b[j] == MN) {
    					k++;
    				}
    			}
    			ld tk = -sum - ptr;
    			for (int j = 0; j <= 36; j++) {
    				if (a[j] + b[j] == MN) {
    					tk += b[j] * 36. / k;
    				}
    			}
    			ans = max(ans, tk);
    			
    		}
}
ll calc0(ll l, ll r) {
//	cerr<<l<<" "<<r<<endl;
	while (l < r) {
		ll g = (l + r + 1) / 2;
		ll sum = 0;
    		for (int j = 0; j <= 36; j++) {
    			b[j] = max(0LL, g - a[j]);
    			sum += b[j];
    		}
//    	cerr<<g<<" "<<sum<<endl;
    	if (sum <= B) {
    		l = g;
    	} else {
    		r = g - 1;
    	}
	}
	return l;
}
int main() {
	#ifdef home
    	freopen("a.in", "r", stdin);
	    freopen("a.out", "w", stdout);
	#endif
	int T;
	cin>>T;
    for (int ti = 1; ti <= T; ti++) {
    	printf("Case #%d: ", ti);
    	cin>>B>>n;
    	for (int i = 0; i <= 36; i++) {
    		a[i] = 0;
    	}
    	for (int i = 0; i < n; i++) {
    		cin>>a[i];
    	}
    	ll mn = 1e15;
    	for (int i = 0; i <= 36; i++) {
    		mn = min(mn, a[i]);
    	}
    	sort(a, a + 37);
    	ans = 0;
    	ll gg = calc0(mn, 1e15);
//    	cerr<<gg<<endl;
    	for (int i = -10; i <= 0; i++)
	    	calc(max(mn, gg + i));
    	printf("%.18lf\n", (double)ans);
    }
	return 0;
}