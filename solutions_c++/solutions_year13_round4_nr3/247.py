#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long

int n,a[2005],b[2005],ret[2005],v[2005],end = 0,st[2005];

void doit(int at) {
	if (at == n+1) end = 1;
	if (end) return;

	int mb[2005],ma[2005];
	memset(mb,0,sizeof(mb));
	memset(ma,0,sizeof(ma));
	int cs = 0;
	for (int j=n-1; j>=0; j--)
		if (v[j] == 1) {
			if (cs == 0) { st[cs++] = ret[j]; }
			else {
				int k;
				for (k=cs-1; k>=0; k--)
					if (st[k] < ret[j]) {
						break;
					}
				//printf("  %d: %d\n",ret[j],k);
				if (k == cs-1) st[cs++] = ret[j];
				else st[k+1] = ret[j];
			}
		}
		else mb[j] = cs;
	cs = 0;
	for (int j=0; j<n; j++)
		if (v[j] == 1) {
			if (cs == 0) { st[cs++] = ret[j]; }
			else {
				int k;
				for (k=cs-1; k>=0; k--)
					if (st[k] < ret[j]) {
						break;
					}
				//printf("  %d: %d\n",ret[j],k);
				if (k == cs-1) st[cs++] = ret[j];
				else st[k+1] = ret[j];
			}
		}
		else ma[j] = cs;

	int id = n;
	for (int j=0; j<n; j++)
		if (v[j] == 0 && b[j]-mb[j] == 1 && ma[j]+1 == a[j]) {
			v[j] = 1;
			ret[j] = at;
			doit(at+1);
			if (end) return;
			v[j] = 0;
		}
}


int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d",&n);
		for (int i=0; i<n; i++)
			scanf("%d",&a[i]);
		for (int i=0; i<n; i++)
			scanf("%d",&b[i]);
		end = 0;

		memset(v,0,sizeof(v));

		doit(1);

		printf("Case #%d:",t);
		for (int i=0; i<n; i++) printf(" %d",ret[i]);
		puts("");
	}
	return 0;
}
