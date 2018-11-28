#include <bits/stdc++.h>

using namespace std;

int t,tes,i,j,k,l,n;
vector<double> b;
double ans;
double a[207],mem[207][207];

double DP(int pos, int sisa) {
	if (pos == k) {
		if (sisa > 0) return 0.0;
		return 1.0;
	}
	if (mem[pos][sisa] > -0.5) return mem[pos][sisa];
	
	double tmp = b[pos] * DP(pos+1,sisa);
	if (sisa > 0) tmp += (1 - b[pos]) * DP(pos+1,sisa-1);
	
	return mem[pos][sisa] = tmp;
}

int main() {
	scanf("%d",&t);
	for (tes=1 ; tes<=t ; tes++) {
		scanf("%d%d",&n,&k);
		for (i=0 ; i<n ; i++) scanf("%lf",&a[i]);
		sort(a,a+n);
		ans = 0.0;
		
		for (i=0 ; i<=k ; i++) {
			b.clear();
			j = 0;
			while (b.size() != i) {
				b.push_back(a[j]);
				j++;
			}
			j = n-1;
			while (b.size() != k) {
				b.push_back(a[j]);
				j--;
			}
			
			for (j=0 ; j<=k ; j++) {
				for (l=0 ; l<=k ; l++) {
					mem[j][l] = -1.0;
				}
			}
			
			//printf("-- ");
			//for (j=0 ; j<k ; j++) printf("%.3lf ",b[j]);
			//printf("\n%.9lf\n",DP(0,k/2));
			ans = max(ans,DP(0,k/2));
		}
		
		printf("Case #%d: %.9lf\n",tes,ans);
	}
}