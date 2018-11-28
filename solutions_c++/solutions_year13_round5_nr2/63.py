#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
using namespace std;

int n, ord[55], bet[55];
int px[55], py[55];
double bests, s;

struct point {
  int x, y;
  
  point () {
    x = y = 0;
	}
  point (int xx, int yy) {
    x = xx;
    y = yy;
	}
};

struct segment {
	point a, b;
	segment() {
	}
	segment(point aa, point bb) {
	  a = aa;
	  b = bb;
	}
};

int multiply(point p0, point p1, point p2) {
  return (p1.x - p0.x)*(p2.y - p0.y) - (p2.x - p0.x)*(p1.y - p0.y);
}

bool intersect(segment u, segment v) {
	return ((max(u.a.x, u.b.x) >= min(v.a.x, v.b.x)) &&
					(max(v.a.x, v.b.x) >= min(u.a.x, u.b.x)) &&
					(max(v.a.y, v.b.y) >= min(u.a.y, u.b.y)) &&
					(max(u.a.y, u.b.y) >= min(v.a.y, v.b.y)) &&
					(multiply(v.a, u.b, u.a) * multiply(u.b, v.b, u.a)) > 0 &&
					(multiply(u.a, v.b, v.a) * multiply(v.b, u.b, v.a)) > 0);
}

bool on(point i, segment l) {
  return  (i.x >= min(l.a.x, l.b.x) && i.y >= min(l.a.y, l.b.y) &&
  				 i.x <= max(l.a.x, l.b.x) && i.y <= max(l.a.y, l.b.y) &&
  				 multiply(l.a, i, l.b) == 0);
}

bool check() {
	segment l1, l2;
	for (int i = 0; i < n; ++i) {
		l1 = segment(point(px[ord[i]], py[ord[i]]), point(px[ord[i + 1]], py[ord[i + 1]]));
		for (int j = i + 1; j < n; ++j) {
			l2 = segment(point(px[ord[j]], py[ord[j]]), point(px[ord[j + 1]], py[ord[j + 1]]));
			if (intersect(l1, l2)) {
			  return false;
			}
	  }
	  
	  for (int j = 0; j < n; ++j) {
	    if (j == ord[i] || j == ord[i + 1]) continue;
	    if (on(point(px[j], py[j]), l1)) return false;
		}
		
	}
	return true;
}

double cal() {
	double ret = 0;
	for (int i = 0; i < n; ++i) {
	  ret = ret + (px[ord[i]] * py[ord[i + 1]] - px[ord[i + 1]] * py[ord[i]]);
	}
	if (fabs(ret) / 2 < bests) return 0;
	if (!check()) return 0;
	return fabs(ret) / 2;
}

int main() {
	
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small.out", "w", stdout);	
	
	int T;
	scanf("%d", &T);
	for (int V = 1; V <= T; ++V) {
	  printf("Case #%d:", V);
	  scanf("%d", &n);
	  for (int i = 0; i < n; ++i) {
	  	ord[i] = i;
	    scanf("%d %d", &px[i], &py[i]);
		}
		px[n] = px[0]; py[n] = py[0];
		bests = 0; s;
		do {
			ord[n] = ord[0];
			s = cal();
//			cout << s << endl;
			if (s > bests) {
				bests = s;
			  for (int i = 0; i < n; ++i) {
			    bet[i] = ord[i];
				}
			}
		} while (next_permutation(ord, ord + n));
		for (int i = 0; i < n; ++i) {
		  printf(" %d", bet[i]);
		}
		printf("\n");
	}
	return 0;
}

