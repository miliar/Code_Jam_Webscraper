#include <bits/stdc++.h>
using namespace std;
int Test,R,C,pt,x,y,l,r;
bool ok;
bool a[20][20];
int to[310],col[310],q[310];
int st[310],ne[3000010],go[3000010];
int exchange(int x){
	if (x<=C)x=x-1;
	else if (C<x&&x<=C+R)x=(x-C)*(2*C+1)-1;
	else if (C+R<x&&x<=2*C+R)x=R*(2*C+1)+C-(x-(C+R));
	else x=(R-(x-(2*C+R)))*(2*C+1)+C;
	return x;
}
void Add(int x,int y){ne[++pt]=st[x];st[x]=pt;go[pt]=y;}
bool check(){
	memset(st,0,sizeof(st));pt=0;
	for (int i=0;i<R;i++)
		for (int j=0;j<C;j++)
			if (a[i][j]==0){
				Add(i*(2*C+1)+j,i*(2*C+1)+C+j);
				Add(i*(2*C+1)+C+j,i*(2*C+1)+j);
				Add(i*(2*C+1)+C+j+1,(i+1)*(2*C+1)+j);
				Add((i+1)*(2*C+1)+j,i*(2*C+1)+C+j+1);
			}else{
				Add(i*(2*C+1)+j,i*(2*C+1)+C+j+1);
				Add(i*(2*C+1)+C+j+1,i*(2*C+1)+j);
				Add(i*(2*C+1)+C+j,(i+1)*(2*C+1)+j);
				Add((i+1)*(2*C+1)+j,i*(2*C+1)+C+j);
			}
	l=1;r=0;
	memset(col,255,sizeof(col));
	for (int i=1;i<=2*(R+C);i++)
		if (i<to[i]){
			int x=exchange(i);
			q[++r]=x,col[x]=x;
		}
	for (;l<=r;l++){
		int x=q[l];
		for (int i=st[x];i;i=ne[i])
			if (col[go[i]]==-1){
				q[++r]=go[i];
				col[go[i]]=col[x];
			}
	}
	for (int i=1;i<=2*(R+C);i++)
		if (to[i]<i){
			int x=exchange(i);
			int y=exchange(to[i]);
			if (col[y]!=y||col[x]!=y)return 0;
		}
	return 1;
}
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&Test);
	for (int tt=1;tt<=Test;tt++){
		printf("Case #%d:\n",tt);
		scanf("%d%d",&R,&C);
		memset(to,0,sizeof(to));
		for (int i=1;i<=(R+C);i++){
			scanf("%d%d",&x,&y);
			to[x]=y;to[y]=x;
		}
		int M=1<<(R*C);
		bool ok=0;
		for (int step=0;step<M;step++){
			for (int i=0;i<R;i++)
				for (int j=0;j<C;j++)
					a[i][j]=(step>>(i*C+j))&1;
			if (check()){
				for (int i=0;i<R;i++){
					for (int j=0;j<C;j++)
						if (a[i][j]==0)printf("/");else printf("\\");
					printf("\n");
				}
				ok=1;
				break;
			}
		}
		if (!ok)printf("IMPOSSIBLE\n");
	}
}