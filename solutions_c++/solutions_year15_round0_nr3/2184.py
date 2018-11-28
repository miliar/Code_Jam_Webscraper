#include <cstdio>
#include <cstdlib>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int state[5][5]={	{0,0, 0, 0, 0},
					{0,1, 2, 3, 4},
					{0,2,-1, 4,-3},
					{0,3,-4,-1, 2},
					{0,4, 3,-2,-1}};
int T,n,m,pos,now;
int a[10010];

int Get() {
	while (1) {
		char c=getchar();
		if (c=='i') return 2;
		if (c=='j') return 3;
		if (c=='k') return 4;
	}
	return 0;
}

int F(int x,int y) {
	int ret=state[abs(x)][abs(y)];
	if ((x<0 && y>0) || (x>0 && y<0)) return -ret;
	else return ret;
}

bool Pd() {
	now=1; pos=1;
	while (now!=2) {
		if (pos>n) break;
		now=F(now,a[pos++]);
	}
	if (pos>n) return false;
	now=1;
	while (now!=3) {
		if (pos>n) break;
		now=F(now,a[pos++]);
	}
	if (pos>n) return false;
	now=1;
	for (int i=pos;i<=n;++i)
		now=F(now,a[i]);
	return now==4;
}

int main() {
	freopen("C-small-attempt0.in","r",stdin);
//	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		scanf("%d%d",&n,&m);
		REP(i,n) a[i]=Get();
		REP(i,n*m) a[i]=a[(i%n==0)?n:i%n];
		n=n*m;
		if (Pd()) printf("Case #%d: YES\n",T_T);
		else printf("Case #%d: NO\n",T_T);
	}
	return 0;
}