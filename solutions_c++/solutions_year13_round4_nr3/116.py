#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
bool w[2001][2001],v[2001],vv[2001];
int in[2001],de[2001],C,Res[2001];
vector<int> E[2001],E2[2001];
void DFS(int a)
{
	int i;
	v[a]=true;
	for(i=0;i<E[a].size();i++){
		if(!v[E[a][i]])DFS(E[a][i]);
	}
}
void DFS2(int a)
{
	if(!Res[a])C++;
	int i;
	v[a]=true;
	for(i=0;i<E2[a].size();i++){
		if(!v[E2[a][i]])DFS2(E2[a][i]);
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int TC,T=0,i,j,N,x,y,cc;
	scanf("%d",&TC);
	while(TC--)
	{
		printf("Case #%d: ",++T);
		scanf("%d",&N);
		for(i=1;i<=N;i++){
			scanf("%d",&in[i]);
			x=y=0;
			for(j=1;j<i;j++){
				if(in[j]==in[i]-1)x=j;
				if(in[j]==in[i])y=j;
			}
			if(x)w[x][i]=true;
			if(y)w[i][y]=true;
		}
		for(i=1;i<=N;i++){
			scanf("%d",&de[i]);
		}
		for(i=1;i<=N;i++){
			x=y=0;
			for(j=N;j>i;j--){
				if(de[j]==de[i]-1)x=j;
				if(de[j]==de[i])y=j;
			}
			if(x)w[x][i]=true;
			if(y)w[i][y]=true;
		}
		for(i=1;i<=N;i++){
			for(j=1;j<=N;j++){
				if(w[i][j])E[i].push_back(j),E2[j].push_back(i);
			}
		}
		for(i=1;i<=N;i++){
			for(j=1;j<=N;j++)v[j]=0;
			C=0;
			DFS2(i);
			DFS(i);
			cc=0;
			for(j=1;j<=N;j++){
				if(!vv[j])cc++;
				if(cc==C)break;
			}
			Res[i]=j;
			vv[j]=true;
		}
		for(i=1;i<=N;i++)printf("%d ",Res[i]);
		printf("\n");
		for(i=1;i<=N;i++){
			vv[i]=false;
			Res[i]=0;
			E[i].clear();
			E2[i].clear();
			for(j=1;j<=N;j++)w[i][j]=false;
		}
	}
}