#include <iostream>
#include <cstdio>
#include <cmath>
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

vector <int> v;

int main() {
	int T,cs;
	int N,r,i,j,m,mp,c;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d",&N);

		v.clear();
		mp = 0;

		Fi(N) {
			scanf("%d",&r);
			v.push_back(r);
			if(r > mp) mp = r;
		}

		m = mp;

		for(i = 1; i <= mp ; i++) {
			c = 0;

			Fj(N) {
				if (v[j] > i) c += ((v[j]-1)/i);
			}
			c += i;

			if(c < m) m = c;
		}
		printf("Case #%d: %d\n",cs,m);
	}
	return 0;
}
