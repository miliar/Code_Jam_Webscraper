#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <assert.h>
#include <math.h>
#include <string.h>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MOD(a,b) (((a)%(b)+(b))%(b))
#define REP(i,n) for (int i = 0; i < (n); i++)

typedef ll co;

struct pu {
	co x,y;
	pu(co a=0, co b=0) {x=a;y=b;}
};
pu operator-(const pu &a, const pu &b) {
	return pu(a.x-b.x,a.y-b.y);
}
// Nicht unbedingt notwendig!
bool operator==(const pu &a, const pu &b) {
	return a.x == b.x && a.y == b.y;
}
///orientierung
co kr(const pu &a, const pu &b) { // z-Komponente de Kreuzprodukts $a\times b$
	return a.x*b.y-b.x*a.y;
}
// Gibt zurück, ob der Winkel zwischen a und b nichtnegativ (gegen den Uhrzeigersinn) ist
bool ccw(const pu &a, const pu &b) {
	return a.x*b.y-b.x*a.y >= 0;
}
// Gibt zurück, ob der Winkel zwischen a und b von r aus gemessen nichtnegativ (gegen den Uhrzeigersinn) ist
bool ccw(const pu &r, const pu &a, const pu &b) {
	return ccw(a-r,b-r);
}

// Gibt, falls a,b,c kollinear sind, zurück ob c auf der Strecke [ab] liegt
bool zwischen(const pu &a, const pu &b, const pu &c) {
	co x1 = min(a.x,b.x), x2 = max(a.x,b.x);
	co y1 = min(a.y,b.y), y2 = max(a.y,b.y);
	return x1 <= c.x && c.x <= x2 && y1 <= c.y && c.y <= y2;
}
bool gr(const pu &a1, const pu &a2, const pu &b1, const pu &b2) {
	co w1 = kr(b1-a1,a2-a1), w2 = kr(a2-a1,b2-a1);
	if (w1 == 0 && w2 == 0)
		return zwischen(a1,a2,b1) || zwischen(a1,a2,b2) ||
		       zwischen(b1,b2,a1) || zwischen(b1,b2,a2);
	if ((w1 >= 0 && w2 >= 0) || (w1 <= 0 && w2 <= 0))
		return true;
	return false;
}
// Gibt zurück, ob sich die Strecken $[a_1a_2]$ und $[b_1b_2]$ schneiden
bool schneidet(const pu &a1, const pu &a2, const pu &b1, const pu &b2) {
	return gr(a1,a2,b1,b2) && gr(b1,b2,a1,a2);
}

int T, N;
pu ps[2000];

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d", &N);
		REP(i, N) {
			scanf("%lld%lld", &ps[i].x, &ps[i].y);
		}
		vector<int> perm;
		REP(i, N)
			perm.push_back(i);
		ll bestarea = 0;
		vector<int> bestperm;
		do {
			ll area = 0;
			REP(i, N) {
				area += kr(ps[perm[i]], ps[perm[(i+1)%N]]);
			}
			if (area >= bestarea) {
				REP(i, N) {
					REP(j, i) {
						pu a1 = ps[perm[i]], a2 = ps[perm[(i+1)%N]], b1 = ps[perm[j]], b2 = ps[perm[(j+1)%N]];
						if (schneidet(a1,a2,b1,b2) && i != j+1 && j != (i+1)%N) {
	// 		REP(i, N) {
	// 			if (i)
	// 				fprintf(stderr, " ");
	// 			fprintf(stderr, "%d", perm[i]);
	// 		}
	// 		fprintf(stderr, ": ");
	// 		fprintf(stderr, "%d %d\n", i, j);
							area = 0;
						}
					}
					pu a1 = ps[perm[i]], a2 = ps[perm[(i+1)%N]], b1 = ps[perm[(i+N-1)%N]], b2 = ps[perm[i]];
					if (kr(a2-b1,b2-b1) == 0 && (zwischen(b1,b2,a2) || zwischen(b2,a2,b1)))
						area = 0;
				}
				area = abs(area);
				if (bestarea < area) {
					bestarea = area;
					bestperm = perm;
				}
			}
		} while(next_permutation(perm.begin(), perm.end()));
		assert(bestperm.size());
		REP(i, N) {
			if (i)
				printf(" ");
			printf("%d", bestperm[i]);
		}
		printf("\n");
	}
	return 0;
}
