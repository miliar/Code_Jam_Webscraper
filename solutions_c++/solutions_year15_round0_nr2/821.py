#include <algorithm>
#include <cstdio>
using namespace std;

int t;
int d;
int p[1234];
int ini;
int ans;

int main()
{
scanf("%d", &t);

for(int q=1; q<=t; q++) {
	scanf("%d", &d);
	for(int i=0; i<d; i++) scanf("%d", &p[i]);
	ini=0;
	for(int i=0; i<d; i++) ini=max(ini, p[i]);
	ans=ini;
	for(int m=1; m<=ini; m++) {
		int res=0;
		for(int i=0; i<d; i++) {
			if(p[i]>m) {
				int diff=p[i]-m;
				if(diff%m==0) res+=diff/m;
				else res+=diff/m+1;
			}
		}
		ans=min(ans, m+res);
	}
	printf("Case #%d: %d\n", q, ans);
}

	return 0;
}
