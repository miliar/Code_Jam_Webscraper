#include <cstdio>
#include <cmath>
//#define reduce

using namespace std;

int result(int p, int q)
{
	int i,j,comp;
	comp = 1;
	for(i=0;comp!=q;i++) {
		if(comp>q) return -1;
		comp *= 2;
	}
	for(j=-1;p;j++) {
		p /= 2;
	}
	return i-j;
}

int main()
{
	int T,t, P,Q;
	int res;
	int sq,j;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d/%d",&P,&Q);
#ifdef reduce
		for(j=2;j<=P;j++) {
			if(P%j) continue;
			if(Q%j) continue;
			P /= j;
			Q /= j;
		}
//printf("%d/%d\n",P,Q);
#endif
		res = result(P,Q);
		if(res==-1) printf("Case #%d: impossible\n",t);
		else printf("Case #%d: %d\n", t, res);
	}
}
