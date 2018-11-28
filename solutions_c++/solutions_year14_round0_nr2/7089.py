#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#define db double
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,te,test;
db C,F,X,mi,s,zhuan;
int main() {
	freopen("cook.in","r",stdin);
	freopen("cook.out","w",stdout);
	scanf("%d",&test);
	For(te,1,test) {
		printf("Case #%d: ",te);
		scanf("%lf%lf%lf",&C,&F,&X);
		db lim=(X-C)*F/C;
		mi=X/2,s=0; zhuan=2;
		for (;zhuan<=lim;) {
			s+=C/zhuan;
			zhuan+=F;
			mi=min(mi,s+X/zhuan);
		}
		printf("%.11lf\n",mi);
	}
	return 0;
}
