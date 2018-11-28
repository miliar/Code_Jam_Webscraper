#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int n,m;
int ans;
struct node{
	int x,y;
} a[101];
int cnt=0;
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int color[11][11];
void print(int a[11][11]) {
	int i,j,k=0;
	for (i=1; i<=n; i++) {
		for (j=0; j<m; j++) cout<<a[i][j]<<" ";
		cout<<endl;
	}
	cout<<endl;
}
bool jud(int u,int v) {
	int i,x,y;
	int b[4]={0};
	//cout<<u<<" "<<v<<endl;
	for (i=0; i<4; i++) {
		x=u+dx[i];
		y=((v+dy[i])%m+m)%m;
		if (x<1||x>n) continue;
		b[color[x][y]]++;
	}
	//for (i=0; i<4; i++) cout<<b[i]<<" ";
	//cout<<endl;
	if (color[u][v]==0) return 0;
	//for (i=1; i<4; i++) {
	i=color[u][v];
		if (b[i]>i) return 1;
		if (b[i]+b[0]<i) return 1;
	//}
	return 0;
}
bool is() {
	int i,j;
	for (i=1; i<=n; i++) {
		for (j=0; j<m; j++)
			if (jud(i,j)) {
				//cout<<i<<" "<<j<<" "<<color[i][j]<<endl;
				return 1;
			}
	}
	return 0;
}
int rec[10001][11][11];
int top=0;
bool isl(int u) {
	int i, j, k;
	for (i=0; i<m; i++) {
		for (j=1; j<=n; j++)
			for (k=0; k<m; k++)
				if (rec[u][j][k]!=color[j][(k+i)%m]) {
					//cout<<u<<" "<<i<<" "<<j<<" "<<k<<endl;
					goto F;
				}
		return 1;
		F:;
	}
	return 0;
}
void add() {
	int i;
	for (i=1; i<=top; i++)
		if (isl(i)) break;
	if (i==top+1) {
		top++;
		memcpy(rec[top],color,sizeof rec[top]);
		//print(rec[top]);
	}
}
void dfs(int u) {
	int i,x,y;
	int b[4]={0};
	//cout<<u<<endl;
	//print();
	//if (u==6) print();
	if (is()) return;
	if (u==cnt+1) {
		//ans++;
		//print();
		add();
		return;
	}
	for (i=0; i<4; i++) {
		x=a[u].x+dx[i];
		y=((a[u].y+dy[i])%m+m)%m;
		
		if (x<1||x>n) continue;
		//if (jud(x,y)) return;
		b[color[x][y]]++;
	}
	/*if (color[1][0]==1&&color[1][1]==2) {//&&color[1][2]==3&&color[2][0]==3&&color[2][1]==3) {
		for (i=0; i<4; i++) cout<<b[i]<<" ";
		cout<<endl;
	}*/
	for (i=1; i<4; i++) {
		if (b[i]>i) continue;
		if (b[i]+b[0]<i) continue;
		color[a[u].x][a[u].y]=i;
		dfs(u+1);
		color[a[u].x][a[u].y]=0;
	}
}
int main() {
	int _,__, i, j;
	//freopen("drum.in","r",stdin);
	//freopen("drum.out","w",stdout);
	scanf("%d",&__);
	for (_=1; _<=__; _++) {
	//while (__--) {
		scanf("%d%d",&n,&m);
		cnt=0;
		for (i=1; i<=n; i++)
			for (j=0; j<m; j++) a[++cnt]=(node){i,j};
		memset(color,0,sizeof color);
		ans=0;
		top=0;
		dfs(1);
		printf("Case #%d: %d\n",_,top);
		//for (i=1; i<=top; i++) print(rec[i]);
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
} 
