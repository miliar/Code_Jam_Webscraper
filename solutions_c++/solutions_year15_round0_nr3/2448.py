#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define int64 long long
#define N 30
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
const int a1[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
const int a2[4][4]={{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}};
int i,j,k,n,T,te,nn,i1,i2,i3,j1,j2,j3;
int64 m;
bool a[N][N],b[N][N];
char p[10010];
inline int C(int x,int y,int z) {
	return x*8+y*2+z;
}
inline void mul(bool a[N][N],bool b[N][N]) {
	int i,j,k;
	bool c[N][N];
	memset(c,0,sizeof(c));
	For(i,0,nn-1)For(j,0,nn-1)For(k,0,nn-1) c[i][k]|=a[i][j]&b[j][k];
	For(i,0,nn-1)For(j,0,nn-1) a[i][j]=c[i][j];
}
int main() {
	freopen("p3.in","r",stdin);
	freopen("p3.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		printf("Case #%d: ",te);
		scanf("%d%lld%s",&n,&m,p+1);
		nn=24;
		memset(b,0,sizeof(b));
		For(i1,0,2)For(i2,0,3)For(i3,0,1) {
			int qi=C(i1,i2,i3);
			b[qi][qi]=1;
			For(i,1,n) {
				bool c[N];
				memcpy(c,b[qi],sizeof(c));
				memset(b[qi],0,sizeof(b[qi]));
				int _=p[i]=='i'?1:p[i]=='j'?2:p[i]=='k'?3:0;
				For(j1,0,2)For(j2,0,3)For(j3,0,1) {
					int now=C(j1,j2,j3);
					if (c[now]) {
						int x=a1[j2][_],y=j3^a2[j2][_];
						b[qi][C(j1,x,y)]=1;
						if (!y&&j1<2&&j1+1==x) b[qi][C(j1+1,0,0)]=1;
					}
				}
			}
		}
		memset(a,0,sizeof(a));
		For(i,0,nn-1) a[i][i]=1;
		for (;m;m>>=1) {
			if (m&1) mul(a,b);
			mul(b,b);
		}
		printf("%s\n",a[0][C(2,3,0)]?"YES":"NO");
	}
	return 0;
}
