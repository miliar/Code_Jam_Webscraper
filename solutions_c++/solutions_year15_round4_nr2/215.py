#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long double fl;

fl eps=1e-11;

int T;

int main()
{
	scanf("%d", &T);

	for(int t=1; t<=T; t++) {
		int n;
		fl v, x;
		scanf("%d%Lf%Lf", &n, &v, &x);
		pair<fl,fl> s[123];
		for(int i=0; i<n; i++) scanf("%Lf%Lf", &s[i].second, &s[i].first);
		sort(s, s+n);
		fl l=0.0, r=1.0e10;
		while(r-l>eps) {
			fl t=(l+r)/2.0;
			fl w[123];
			for(int i=0; i<n; i++) w[i]=t*s[i].second;
			fl sum=0.0;
			for(int i=0; i<n; i++) sum+=w[i];
			if(sum-v<eps) {
				l=t;
				continue;
			}
			fl mint=0.0, maxt=0.0;
			sum=0.0;
			for(int i=0; i<n; i++) {
				mint+=s[i].first*min(w[i], v-sum);
				sum+=min(w[i], v-sum);
				if(v-sum<eps) break;
			}
			mint/=v;
			sum=0.0;
			for(int i=n-1; i>=0; i--) {
				maxt+=s[i].first*min(w[i], v-sum);
				sum+=min(w[i], v-sum);
				if(v-sum<eps) break;
			}
			maxt/=v;
			if(mint-x<eps && x-maxt<eps) {
				r=t;
			} else {
				l=t;
			}
		}
		if(l>1.0e9) {
			printf("Case #%d: %s\n", t, "IMPOSSIBLE");
		} else {
			printf("Case #%d: %.9Lf\n", t, l);
		}
	}

	return 0;
}
