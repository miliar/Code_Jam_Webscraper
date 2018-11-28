#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cmath>

using namespace std;

#define rep(a,b,c) for(int a=b;a<=c;++a)
#define per(a,b,c) for(int a=b;a>=c;--a)
#define X first
#define Y second
#define PII pair<int,int>
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define pb push_back
#define mp make_pair

typedef long long ll;

const int dx[]={0,-1,1,0,0};
const int dy[]={0,0,0,-1,1};
int T,n,m,ans;
int a[110][110];

int read(){
	while	(1){
		char c=getchar();
		switch	(c){
			case	'.':	return	0;
			case	'^':	return	1;
			case	'v':	return	2;
			case	'<':	return	3;
			case	'>':	return	4;
		}
 	}
}

bool ok(int x,int y){
	if	(!a[x][y])	return	1;
	int tx=dx[a[x][y]],ty=dy[a[x][y]];
	while (1){
		x+=tx;y+=ty;
		if (x==0 || x==n+1 || y==0 || y==m+1)	return	0;
		if (a[x][y])	return	1;
	}
}

void work() {
	ans=0;
	rep(i,1,n)	rep(j,1,m)
		if (!ok(i,j)){
			bool pass=0;
			rep(k,1,4){
				a[i][j]=k;
				if	(ok(i,j)){
					pass=1;
					break;
				}
			}
			if (!pass){
				puts("IMPOSSIBLE");
				return;
			}
			++ans;
		}
	printf("%d\n",ans);
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d",&T);
	rep(TT,1,T){
		printf("Case #%d: ",TT);
		scanf("%d%d",&n,&m);
		rep(i,1,n)	rep(j,1,m)	a[i][j]=read();
		work();
	}
	return 0;
}


