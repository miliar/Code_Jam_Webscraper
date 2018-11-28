#include <cstdio>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

const int dx[]={0,-1,1,0,0};
const int dy[]={0,0,0,-1,1};
int T,n,m,ans;
int a[110][110];

int Get() {
	while (1) {
		char c=getchar();
		if (c=='.') return 0;
		if (c=='^') return 1;
		if (c=='v') return 2;
		if (c=='<') return 3;
		if (c=='>') return 4;
 	}
}

bool Can(int x,int y) {
	if (!a[x][y]) return true;
	int tx=dx[a[x][y]];
	int ty=dy[a[x][y]];
	while (1) {
		x+=tx;
		y+=ty;
		if (x==0 || x==n+1 || y==0 || y==m+1) return false;
		if (a[x][y]) return true;
	}
}

void Work() {
	ans=0;
	REP(i,n) REP(j,m)
		if (!Can(i,j)) {
			bool flag=false;
			REP(k,4) {
				a[i][j]=k;
				if (Can(i,j)) {flag=true;break;}
			}
			if (!flag) {puts("IMPOSSIBLE");return;}
			++ans;
		}
	printf("%d\n",ans);
}

int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ",T_T);
		scanf("%d%d",&n,&m);
		REP(i,n) REP(j,m) a[i][j]=Get();
		Work();
	}
	return 0;
}