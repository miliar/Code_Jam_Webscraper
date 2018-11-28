#include<stdio.h>
#include<string.h>
#include<algorithm>
struct LIST
{
	int x,n;
	bool operator()(LIST a,LIST b)
	{
		return a.x<b.x;
	}
}list[1001];
int A[1001],B[1001];
int N;
int D[1001][1001];
int Tree[10001],Start;
int ABS(int x)
{
	if(x<0) return -x;
	return x;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t,x;
	int i,j,S,E;
	int SumL,Ans;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d",&N);
		for(i=1;i<=N;i++) scanf("%d",&A[i]),list[i].x=A[i],list[i].n=i;
		std::sort(list+1,list+1+N,LIST());
		for(i=1;i<=N;i++) B[list[i].n]=i;
		memset(Tree,0,sizeof(Tree));
		Start=1;
		while(Start<N) Start*=2;
		memset(D,12,sizeof(D));
		D[0][0]=0;
		for(i=1;i<=N;i++)
		{
			SumL=0;
			S=Start; E=Start+list[i].n-1;
			while(S<=E)
			{
				if(S&1)
				{
					SumL+=Tree[S];
					S++;
				}
				if(!(E&1))
				{
					SumL+=Tree[E];
					E--;
				}
				S>>=1; E>>=1;
			}
			for(j=0;j<i;j++)
			{
				// From D[j][i-1-j]
				if(D[j+1][i-1-j]>D[j][i-1-j]+ABS(list[i].n-SumL+j - (j+1)))
					D[j+1][i-1-j]=D[j][i-1-j]+ABS(list[i].n-SumL+j - (j+1));
				if(D[j][i-j]>D[j][i-1-j]+ABS((N-(i-1-j))-(list[i].n-SumL+j)))
					D[j][i-j]=D[j][i-1-j]+ABS((N-(i-1-j))-(list[i].n-SumL+j));
			}
			x=Start+list[i].n-1;
			while(x!=0) Tree[x]++,x>>=1;
		}
		Ans=D[0][N];
		for(i=0;i<=N;i++)
		{
			if(Ans>D[i][N-i]) Ans=D[i][N-i];
		}
		printf("Case #%d: %d\n",t,Ans);
	}
}
/*

#include<algorithm>
#include<stdio.h>
int A[11];
int B[11];
int N;
struct LIST
{
	int x,n;
	bool operator()(LIST a,LIST b)
	{
		return a.x<b.x;
	}
}list[11];
bool V[11];
int C[11];
int Ans;
int D[11];
void check()
{
	int i,j,k,cnt=0;
	for(i=1;i<=N;i++) if(C[i]==N) break;
	for(j=1;j<i;j++) if(C[j]>C[j+1]) return;
	for(j=i;j<N;j++) if(C[j]<C[j+1]) return;
	int imsi;
	for(i=1;i<=N;i++) D[i]=B[i];
	for(i=1;i<=N;i++) printf("%d ",B[i]);
	printf("-> ");
	for(i=1;i<=N;i++)
	{
		for(j=i;j<=N;j++) if(C[i]==D[j]) break;
		for(k=j-1;k>=i;k--)
		{
			imsi=D[k];
			D[k]=D[k+1];
			D[k+1]=imsi;
			cnt++;
		}
	}
	for(i=1;i<=N;i++) printf("%d ",D[i]);
	printf(" : %d\n",cnt);
	if(Ans==-1) Ans=cnt;
	else if(Ans>cnt) Ans=cnt;
}
void dfs(int x)
{
	if(x==N+1)
	{
		check();
		return;
	}
	int i;
	for(i=1;i<=N;i++)
	{
		if(V[i]) continue;
		V[i]=1;
		C[x]=i;
		dfs(x+1);
		V[i]=C[x]=0;
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int t,i;
	for(t=1;t<=T;t++)
	{
		scanf("%d",&N);
		Ans=-1;
		for(i=1;i<=N;i++) scanf("%d",&A[i]),list[i].x=A[i],list[i].n=i;
		std::sort(list+1,list+1+N,LIST());
		for(i=1;i<=N;i++) B[list[i].n]=i,V[i]=0;
		dfs(1);
		printf("Case #%d: %d\n",t,Ans);
	}
}*/