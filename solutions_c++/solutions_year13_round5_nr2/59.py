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
typedef double ld;
typedef pair<int, int> pi;
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),(a).end()
const ld eps = 1e-9;
struct pnt {
	ld x, y;
	pnt(){
	}
	pnt(ld x, ld y):x(x),y(y) {
	}
};
bool cmp1(pnt a, pnt b) {
	return a.x < b.x - eps || (fabs(a.x - b.x) <= eps && a.y < b.y - eps);
}
ld vp(pnt a, pnt b) {
	return a.x * b.y - a.y * b.x;
}
pnt operator - (pnt a, pnt b) {
	return pnt(a.x - b.x, a.y - b.y);
}
pnt operator *(ld c, pnt a) {
	return pnt(c * a.x, c * a.y);
}
int zn(ld x) {
	if (x > eps) return 1;
	if (fabs(x) <= eps) return 0;
	return -1;
}
bool inters(pnt a1, pnt a2, pnt b1, pnt b2) {
	if (fabs(vp(a2 - a1, b2 - b1)) <= eps) {
		if (fabs(vp(a2 - a1, b2 - a1)) <= eps) {
			return !(max(a1.x, a2.x) < min(b1.x, b2.x) || max(b1.x, b2.x) < min(a1.x, a2.x) ||
			         max(a1.y, a2.y) < min(b1.y, b2.y) || max(b1.y, b2.y) < min(a1.y, a2.y));
		} else {
			return false;
		}
	}
	return zn(vp(a2 - a1, b2 - a1)) * zn(vp(a2 - a1, b1 - a1)) <= 0 && 
		   zn(vp(b2 - b1, a2 - b1)) * zn(vp(b2 - b1, a1 - b1)) <= 0;
}
int n;
pnt p[100];
int a[100];
int ans[100];
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
    	scanf("%d", &n);
    	for (int i = 0; i < n; i++) {
    		int x, y;
    		scanf("%d %d", &x, &y);
    		p[i] = pnt(x, y);
    	//	pp[i] = p[i];
    	}
    	for (int i = 0; i < n; i++) {
    		a[i] = i;
    	}
    	ld mx = -1;
    	while (1) {
    		ld tks = 0;
    		a[n] = a[0];
    		for (int i = 0; i < n; i++) {
    			tks += vp(p[a[i]], p[a[i + 1]]);
    		}
    		bool can = true;
    		for (int i = 0; i < n; i++) {
    			for (int j = i + 1; j < n; j++) {
    				if (inters(p[a[i]], p[a[i + 1]] - (1e-3 * (p[a[i + 1]] - p[a[i]])), p[a[j]], p[a[j + 1]] - (1e-3 * (p[a[j + 1]] - p[a[j]])))) {
    					can = false;
    					break;
    				}
    			}
    		}
    		tks = abs(tks);
    		if (can && tks >= mx) {
    			mx = tks;
    			for (int i = 0; i < n; i++) {
    				ans[i] = a[i];
    			}
    		}
    		if (!next_permutation(a + 1, a + n)) {
    			break;
    		}
    	}
    	for (int i = 0; i < n; i++) {
    		printf("%d%c", ans[i], " \n"[i + 1 == n]);
    	}
	}
	return 0;
}