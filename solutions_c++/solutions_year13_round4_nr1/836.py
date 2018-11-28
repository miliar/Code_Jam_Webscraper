#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>

#define f first
#define s second
#define mp make_pair

using namespace std;

typedef long long lld;
typedef pair<lld, lld> pii;

vector<pii> st;
vector<pii> ed;

lld c;

lld func(lld a, lld b) {
	lld dst = b-a;
	lld ret = dst*c - ((dst-1ll)*dst)/2ll;
	return ret;
}

int main() {
	freopen("bigin.txt", "r", stdin);
	freopen("bigout.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=0; ti<t; ti++) {
		st.clear();
		ed.clear();
		lld n;
		lld expsum = 0;
		scanf("%lld%lld", &c, &n);
		for (lld i=0; i<n; i++) {
			lld a, b, v;
			scanf("%lld%lld%lld", &a, &b, &v);
			st.push_back(pii(a, -v));
			st.push_back(pii(b, v));
			expsum = (expsum%1000002013ll + (func(a, b)%1000002013ll) * (v%1000002013ll))%1000002013ll;
		}
		priority_queue<pii> heap;
		sort(st.begin(), st.end());
		lld optsum = 0;
		for (lld i=0; i<2ll*n; i++) {
			if (st[i].s < 0) {
				st[i].s = -st[i].s;
				heap.push(pii(st[i]));
			}
			else {
				while (heap.empty() == false) {
					pii top = heap.top();
					heap.pop();
					lld used = min(top.s, st[i].s);
					top.s-= used;
					st[i].s-= used;
					optsum = (optsum + ((func(top.f, st[i].f)%1000002013ll) * (used%1000002013ll))%1000002013ll)%1000002013ll;
					if (top.s) {
						heap.push(top);
					}
					if (!st[i].s) {
						break;
					}
				}
			}		
		}
		printf("Case #%d: %lld\n", ti+1, (((expsum-optsum)%1000002013ll)+2*1000002013ll)%1000002013ll);
	}
	return 0;
}