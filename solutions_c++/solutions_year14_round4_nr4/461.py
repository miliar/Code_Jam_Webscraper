#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
struct ww {
	int a[26];
	inline void cl() {
		int i;
		For(i,0,25) a[i]=0;
	}
} b[10000];
int i,j,k,n,m,test,T,ma,re,t;
int a[10][10];
char p[10][20];
inline int work(int x) {
	int i,j,v;
	if (!*a[x]) return 0;
	t=1;
	b[1].cl();
	For(i,1,*a[x]) {
		int A=a[x][i],len=strlen(p[A]+1);
		v=1;
		For(j,1,len) {
			int B=p[A][j]-'A';
			if (!b[v].a[B]) b[v].a[B]=++t,b[t].cl();
			v=b[v].a[B];
		}
	}
	return t;
}
void dfs(int x) {
	int i;
	if (x>n) {
		int s=0;
		For(i,1,m) s+=work(i);
		if (ma<s) ma=s,re=1;
		else re+=s==ma;
		return;
	}
	For(i,1,m) {
		a[i][++*a[i]]=x;
		dfs(x+1);
		(*a[i])--;
	}
}
int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&T);
	For(test,1,T) {
		printf("Case #%d: ",test);
		scanf("%d%d",&n,&m);
		ma=0;
		For(i,1,n) scanf("%s",p[i]+1);
		For(i,1,m) *a[i]=0;
		dfs(1);
		printf("%d %d\n",ma,re);
	}
	return 0;
}
