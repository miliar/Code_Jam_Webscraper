#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int T;
int x,y;
int a[5][5],b[5][5];
int p[105];

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for (int t=0;t<T;t++){
		printf("Case #%d: ",t+1);
		scanf("%d",&x);
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&y);
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		--x; --y;
		memset(p,0,sizeof(p));
		for (int i=0;i<4;i++)
			p[a[x][i]]++;
		int ok=0,ans=0;
		for (int i=0;i<4;i++)
			if (p[b[y][i]]){
				ok++; ans=b[y][i];
			}
		if (ok>1)
			printf("Bad magician!\n");
		else if (ok==0)
			printf("Volunteer cheated!\n");
		else printf("%d\n",ans);
	}
	return 0;
}