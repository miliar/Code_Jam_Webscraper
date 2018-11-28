#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
using namespace std;

#define rep(i,N) for((i) = 0; (i) < (N); (i)++)
#define rab(i,a,b) for((i) = (a); (i) <= (b); (i)++)
#define Fi(N) rep(i,N)
#define Fj(N) rep(j,N)
#define Fk(N) rep(k,N)
#define sz(v) (v).size()
#define all(v) (v).begin(),(v).end()

typedef pair<int,int> PII;

vector <PII> v;
int pos[1000];

int cache[1001][1001];

int memo(int p,int q) {
	if(p == 0 && q == 0) return 0;

	int &r = cache[p][q];
	if(r >= 0) return r;
	r = 1 << 30;
	int c1,c2;

	int i = sz(v) - (p + q + 1);

	if(p > 0) c1 = pos[i] + memo(p - 1,q); else c1 = 1 << 30;
	if(q > 0) c2 = ((p + q) - pos[i]) + memo(p,q-1); else c2 = 1 << 30;

	r = (c1 < c2) ? c1 : c2;

	return r;
}

int main() {
	int T,cs;
	int N,i,j;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d",&N);

		v.clear();
		Fi(N) {
			scanf("%d",&j);
			v.push_back(make_pair(j,i));
		}
		sort(all(v));

		pos[sz(v) - 1] = 0;

		for(i = sz(v) - 2; i >= 0; i--) {
			int c = 0;

			for(j = i + 1; j < sz(v); j++) {
				if(v[i].second > v[j].second) {
					c++;
				}
			}
			pos[i] = c;
			//printf("pos %d: %d\n",v[i].first,c);
		}
		memset(cache,-1,sizeof(cache));

		int r = -1,c;

		for(i = 0; i < N; i++) {
			c = memo(i,N - i - 1);
			//printf("%d %d\n",i,c);
			if(r == -1 || c < r) r = c;
		}

		printf("Case #%d: %d\n",cs,r);
	}
	return 0;
}
