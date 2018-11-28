#include<stdio.h>

int data[105][105];
int rowMax[105],colMax[105];
int n,m;

void input()
{
	int i,j;
	scanf("%d%d",&n,&m);
	for(i=1;i<=n;i++){
		for(j=1;j<=m;j++){
			scanf("%d",&data[i][j]);
		}
	}
}

void solve()
{
	int i,j;
	for(i=1;i<=n;i++){
		rowMax[i]=data[i][1];
		for(j=1;j<=m;j++){
			if(rowMax[i]<data[i][j])rowMax[i]=data[i][j];
		}
	}
	for(i=1;i<=m;i++){
		colMax[i]=data[1][i];
		for(j=1;j<=n;j++){
			if(colMax[i]<data[j][i])colMax[i]=data[j][i];
		}
	}
	for(i=1;i<=n;i++){
		for(j=1;j<=m;j++){
			if(data[i][j]<rowMax[i]&&data[i][j]<colMax[j])break;
		}
		if(j!=m+1)break;
	}
	if(i==n+1)printf("YES\n");
	else printf("NO\n");
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		input();
		solve();
	}
}