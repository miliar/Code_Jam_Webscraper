#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int map[105][105],n,m;

bool judge(int x,int y){
	bool ok1=true,ok2=true;
	for(int i=1;i<=n;++i)
		if(map[i][y]>map[x][y]) ok1=false;
	for(int j=1;j<=m;++j)
		if(map[x][j]>map[x][y]) ok2=false;
	return (ok1 || ok2);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;++cas){
		printf("Case #%d: ",cas);
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;++i)
			for(int j=1;j<=m;++j)
				scanf("%d",&map[i][j]);
		bool ok=true;
		for(int i=1;i<=n;++i)
			for(int j=1;j<=m;++j)
				if(!judge(i,j)){
					ok=false;
					break;
				}
		if(!ok) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}
