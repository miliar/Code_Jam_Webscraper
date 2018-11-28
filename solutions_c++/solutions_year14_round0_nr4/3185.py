#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define all(a) a.begin(), a.end()

int main() {
	int t, tc, n, i, y = 0, z, p, beg;
	double w;

	scanf("%d",&tc);
	for(t=1;t<=tc;t++) {
		scanf("%d",&n);
		vector<double> she, he;
		for(i=0;i<n;i++) {
			scanf("%lf",&w);
			she.push_back(w);
		}
		for(i=0;i<n;i++) {
			scanf("%lf",&w);
			he.push_back(w);
		}
		sort(all(she));
		sort(all(he));
		//
		y = 0;
		p = 0;
		for(i=0;i<n;i++) {
			if(she[i] > he[p]) {
				p++;
				y++;
			}
		}
		z = 0;
		beg = 0;
		for(i=0;i<n;i++) {
			if(he[he.size()-1] > she[i] ) {
				p = lower_bound(he.begin()+beg, he.end(), she[i]) - he.begin();
				he.erase(he.begin()+p);
			} else {
				z++;
				beg++;
			}
		}
		printf("Case #%d: %d %d\n",t,y,z);
	}
	return 0;
}
