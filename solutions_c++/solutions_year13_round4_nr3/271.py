#include<stdio.h>
#include<algorithm>

int A[2005];
int B[2005];
int seq[2005];
int check[2005][2005];
int n;

bool DFS(int x)
{
	if(x==n+1){
		return true;
	}
	int i,max=0;
	for(i=1;i<=n;i++){
		check[x][i]=0;
		if(seq[i]!=0)max=std::max(A[i],max);
		else if(A[i]==max+1)check[x][i]=1;
	}
	max=0;
	for(i=n;i>=1;i--){
		if(seq[i]!=0)max=std::max(B[i],max);
		else if(B[i]==max+1&&check[x][i]==1)check[x][i]=2;
	}
	for(i=1;i<=n;i++){
		if(check[x][i]==2){
			seq[i]=x;
			if(DFS(x+1))return true;
			seq[i]=0;
		}
	}
	return false;
}

void solve()
{
	scanf("%d",&n);
	for(int i=1;i<=n;i++)scanf("%d",A+i);
	for(int i=1;i<=n;i++)scanf("%d",B+i);
	for(int i=1;i<=n;i++)seq[i]=0;
	DFS(1);
	for(int i=1;i<=n;i++)printf("%d ",seq[i]);
	printf("\n");
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}