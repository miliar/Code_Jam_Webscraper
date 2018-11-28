#include<stdio.h>
#include<algorithm>
using namespace std;
bool cmp(double a,double b) {
	return a<b;
}
int main() {
	double a[2000],b[2000];
	int t,T,i,n,ahead,atail,bhead,btail,win1,win2;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lf",&a[i]);
		for(i=0;i<n;i++) scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		ahead=bhead=win1=0;
		atail=btail=n-1;
		while(ahead<=atail) {
			if(a[ahead]>b[bhead]) {
				win1++;
				ahead++;
				bhead++;
			}
			else {
				ahead++;
				btail--;
			}
		}
		ahead=bhead=win2=0;
		atail=btail=n-1;
		while(ahead<=atail) {
			if(b[bhead]>a[ahead]) {
				ahead++;
				bhead++;
			}
			else {
				win2++;
				bhead++;
				atail--;
			}
		}
		printf("Case #%d: %d %d\n",t,win1,win2);
	}
	return 0;
}
