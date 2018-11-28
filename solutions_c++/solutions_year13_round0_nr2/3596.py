#include <cstdio>
#include <cstring>

int b[105][105];
int T,x,y;

bool check(int xx,int yy){
	bool r,c;
	r=c=1;
	for (int i=0;i<y;++i){
		if (b[xx][i]>b[xx][yy])
			r=0;
	}
	for (int j=0;j<x;++j){
		if (b[j][yy]>b[xx][yy])
			c=0;
	}
	return r||c;
}

int main(){
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%d%d",&x,&y);
		for (int i=0;i<x;++i)
			for (int j=0;j<y;++j)
				scanf("%d",&b[i][j]);
		bool f=1;
		for (int i=0;i<x;++i)
			for (int j=0;j<y;++j){
				f = f&&check(i,j);
			}
		printf("Case #%d: %s\n",t,(f?"YES":"NO"));
	}
}
