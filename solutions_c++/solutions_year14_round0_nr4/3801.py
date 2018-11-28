#include <cstdio>
#include <algorithm>

using namespace std;

	int t,n,w,dw;
	float nao[1200],ken[1200];

int main() {

	freopen ("D-large.in","r",stdin);
	freopen ("Output.in","w",stdout);
	scanf("%d",&t);
	for (int k=1; k<=t; k++) {
		w = dw = 0;
		scanf("%d",&n);
		for (int i=0; i<n; i++) scanf("%f",&nao[i]);
		for (int i=0; i<n; i++) scanf("%f",&ken[i]);
		sort(nao, nao + n);
		sort(ken, ken + n);
		for (int i=0,j=0; i<n; i++) {
			if (nao[i] > ken[j]) {
				j++;
				dw++;
			}
		}
		for (int i=0,j=0; i<n; i++) {
			if (nao[j] < ken[i]) j++;
			else w++;
		}
		printf("Case #%d: %d %d\n",k,dw,w);
	}

	return 0;
}
