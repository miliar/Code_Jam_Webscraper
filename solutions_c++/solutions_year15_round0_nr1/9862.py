#include <bits/stdc++.h>
#define max(x,y) ((x) > (y) ? (x) : (y))
#define min(x,y) ((x) < (y) ? (x) : (y))
#define abs(x) ((x) < 0 ? -(x) : (x))
using namespace std;

char dum;
int shy[1001];
int t,smax,i,j,s,sm,need;

int main()
{
	scanf("%d",&t);
	for (s=1;s<=t;++s) {
		scanf("%d",&smax);
		getchar();
		for (i=0;i<=smax;++i) {
			scanf("%c",&dum);
			shy[i]=dum-'0';
		}
		sm=0;
		need=0;
		for (i=0;i<=smax;++i) {
			if (shy[i] > 0) {
				if (i<=sm) sm+=shy[i];
				else {
					need+=i-sm;
					sm+=need+shy[i];
				}
			}
		}
		printf("Case #%d: %d\n",s,need);
	}
	return 0;
}

