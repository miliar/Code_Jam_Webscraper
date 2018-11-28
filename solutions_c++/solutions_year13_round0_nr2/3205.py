#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;;
int n,m;int T;
int f[111][111];
bool v[111][111];
int h[111][111];
const int di[4] = {0,0,1,-1};
const int dj[4] = {1,-1,0,0};
FILE *fout;
inline bool verify(int nx,int ny){
	return (nx>=0 && nx<n && ny>=0 && ny < m);
}
int cnt = 0;
void flord(int i,int j,int limit){
	if (v[i][j]) return ;
	if (f[i][j]==limit) return;
	cnt++;
	v[i][j]=true;
	if (h[i][j]==limit) 
		f[i][j] = true;
	for (int d = 0 ; d < 4 ; d++){
		if (verify(i+di[d],j+dj[d])){
			if (h[i+di[d]][j+dj[d]]<=limit) flord(i+di[d],j+dj[d],limit);
		}
	}
	//v[i][j]=false;
}
void work(int c){
	int maxh = 0;
	scanf("%d%d",&n,&m);
//	printf("start %d X %d\n",n,m);
	for (int i = 0 ; i < n; i++)
		for (int j = 0 ; j < m ; j++){
			scanf("%d",&h[i][j]);
			if (h[i][j]>maxh)maxh = h[i][j];
			f[i][j] = 101;
		};
	for (int j = 0;j<m;j++){
		// (0,j)~(n,j)
		int x = 0;
		for (int k = 0;k < n ;k++)
			x = max(x,h[k][j]);
		//printf("set (%d %d) to %d : ",0,j,x);
		for (int k = 0;k < n ;k++)
			f[k][j] = min(f[k][j],x);
	}
	for (int j = 0;j<n;j++)
	{
		// (j,0)~(j,m)
		int x = 0;
		for (int k = 0;k < m ;k++)
			x = max(x,h[j][k]);
		//printf("set (%d %d) to %d\n",j,0,x);
		for (int k = 0;k < m ;k++)
			f[j][k] = min(f[j][k],x);
	}

	bool rst = true;
	for (int i = 0 ; i < n ; i++)
		for (int j = 0 ; j < m ; j ++){
			rst&=f[i][j]==h[i][j];
			//printf("%d%c",f[i][j],(j==(m-1))?'\n':' ');
		}

	//printf("Case #%d: %s\n",c,rst?"YES":"NO");
	fprintf(fout,"Case #%d: %s\n",c,rst?"YES":"NO");
//	printf("%d/%d\n",c,T);
}
/*
2
10 10
1 2 1 2 1 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1
1 2 1 2 1 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 2 1 2 1 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1
1 2 1 2 1 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1

1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 2 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 2 1 2 1 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1
1 2 1 2 1 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
*/
int main(){
	freopen("B.in","r",stdin);
	fout = fopen("B.out","w");
	scanf("%d",&T);
	for (int i = 1 ; i <= T ;i++) work(i);
}