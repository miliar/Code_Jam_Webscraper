#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<cmath>
#define LL long long
using namespace std;
int t,r,c,a[1000],b[20][20],ans[20][20],ok,v[20][20][10];
void abc(int x,int y){
	if (ok==1) return;
	if (x==r+1){
		int tx,ty,tz;

		for (int i=0;i<2*(r+c);i++){
			if (a[i]<=c) tx=1,ty=a[i],tz=1;
			else if (a[i]<=c+r) tx=a[i]-c,ty=c,tz=2;
			else if (a[i]<=c+r+c) tx=r,ty=c+r+c-a[i]+1,tz=3;
			else tx=r+r+c+c-a[i]+1,ty=1,tz=4;
			for (int j=1;j<=r;j++)	
				for (int k=1;k<=c;k++)
					for (int l=1;l<=4;l++)
						v[j][k][l]=0;
			do{
				if (v[tx][ty][tz]==1) return;
				v[tx][ty][tz]=1;
				if (b[tx][ty]==-1){
					if (tz==1) ty--,tz=2;
					else if (tz==2) tx++,tz=1;
					else if (tz==3) ty++,tz=4;
					else if (tz==4) tx--,tz=3;
				}else{
					if (tz==1) ty++,tz=4;
					else if (tz==2) tx--,tz=3;
					else if (tz==3) ty--,tz=2;
					else if (tz==4) tx++,tz=1;
				}
			}while(b[tx][ty]<0);
			if (b[tx][ty]!=a[i^1]) return;
		}
		ok=1;
		for (int i=1;i<=r;i++)
			for (int j=1;j<=c;j++) ans[i][j]=b[i][j];
		return;
	}else{
		b[x][y]=-1;
		if (y==c) abc(x+1,1);
		else abc(x,y+1);
		b[x][y]=-2;
		if (y==c) abc(x+1,1);
		else abc(x,y+1);
	}
}
int main(){
	scanf("%d",&t);
	for (int I=1;I<=t;I++){
		scanf("%d%d",&r,&c);
		for (int i=0;i<2*(r+c);i++) scanf("%d",&a[i]);
		for (int i=1;i<=c;i++) b[0][i]=i;
		for (int i=1;i<=r;i++) b[i][c+1]=i+c;
		for (int i=1;i<=c;i++) b[r+1][i]=c+r+c-i+1;
		for (int i=1;i<=r;i++) b[i][0]=c+r+r+c-i+1;
		ok=0;
		abc(1,1);
		printf("Case #%d:\n",I);
		if (ok==0) printf("IMPOSSIBLE\n");
		else{
			for (int i=1;i<=r;i++){
				for (int j=1;j<=c;j++)
					if (ans[i][j]==-1) printf("/");
					else printf("\\");
				printf("\n");
			}
		}
	}
    return 0;
}

