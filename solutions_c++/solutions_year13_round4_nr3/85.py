#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
#define LL long long

const int MaxN = 2000 + 10;

int A[MaxN],B[MaxN];
vector<int> adj[MaxN],rev[MaxN];
int deg[MaxN];
int N;
vector<int> prev;
int ans[MaxN],arr[MaxN];
/*
int go(int cnt, int l,int r)
{
	int c = min_element(arr+l,arr+r+1)-arr;
	
	vector<int> prev;
	dfs(prev,c);
	
	return cnt + r - l + 1;
}
*/
void run()
{
	scanf("%d",&N);
	for(int i=1;i<=N;++i)
	{
		deg[i]=0;
		adj[i].clear();
		rev[i].clear();
		scanf("%d", A+i);
	}
	for(int i=1;i<=N;++i) scanf("%d", B+i);
	
	for(int i=1;i<=N;++i) {
		for(int j=i+1;j<=N;++j) {
			if(A[i] >= A[j]) // P[i] > P[j]
			{
				adj[j].push_back(i);
				++ deg[i];
				
		//		cerr << j << " < "<<i<<endl;
			}
			if(B[i] <= B[j]) // P[i] < P[j]
			{
				adj[i].push_back(j);
				++ deg[j];
				
		//		cerr << i << " < "<<j<<endl;
			}
		}
		for(int j=i-1;j>0;--j)
			if(A[j] == A[i]-1) // P[j] < P[i]
			{
				adj[j].push_back(i); 
				++ deg[i];
			//	cerr << j << " < "<<i<<endl;
				break;
			}
		for(int j=i+1;j<=N;++j)
			if(B[j] == B[i]-1) // P[i] > P[j]
			{
				adj[j].push_back(i);
				++ deg[i];
			//	cerr << j << " < "<<i<<endl;
				break;
			}
	}
	
	for(int i=1;i<=N;++i)
		for(int j=0;j<adj[i].size();++j)
			rev[adj[i][j]].push_back(j);
	
//	for(int i=1;i<=N;++i) arr[i]=i;
//	go(0,1,N);
	
	
	priority_queue<int> Q;
	for(int i=1;i<=N;++i)
	{
		if(!deg[i]) Q.push(-i);
	}
	
	vector<int> T(N,0);
	
	int cnt=0;
	while(!Q.empty())
	{
		int u = -Q.top(); Q.pop();
		T[u-1] = ++ cnt;
		for(int i=0;i<adj[u].size();++i)
			if(!--deg[adj[u][i]])
				Q.push(-adj[u][i]);
	}
	for(int i=0;i<N;++i)
		printf(" %d", T[i]);
	puts("");
	
	
	vector<int> X(N,0),Y(N,0);
	for(int i=0;i<N;++i)
	{
		X[i] = 1;
		for(int j=0;j<i;++j)
			if(T[j] < T[i])	
				X[i] = max(X[i], 1 + X[j]);
	}
	for(int i=N-1;i>=0;--i)
	{
		Y[i] = 1;
		for(int j=i+1;j<N;++j)
			if(T[j] < T[i])
				Y[i] = max(Y[i], 1 + Y[j]);
	}
	/*
	cerr << "A : ";
	for(int i=1;i<=N;++i)
	{
		cerr << A[i]<<" ";
	}cerr << endl;
	
	cerr << "B : ";
	for(int i=1;i<=N;++i)
	{
		cerr << B[i]<<" ";
	}cerr << endl;
	
	cerr << "P : ";
	for(int i=0;i<N;++i)
	{
		cerr <<T[i]<<" ";
	}cerr << endl;
	
	cerr << "X : ";
	for(int i=0;i<N;++i)
	{
		cerr << X[i]<<" ";
	}cerr << endl;
	
	cerr << "Y : ";
	for(int i=0;i<N;++i)
	{
		cerr << Y[i]<<" ";
	}cerr << endl;
	*/
	bool flag=true;
	for(int i=0;i<N;++i)
		if(A[i+1] != X[i] || B[i+1] != Y[i])
		{
			flag=false;
		}
	if(!flag) {
		cerr << "error!"<<endl;
		cerr << "N = "<<N<<endl;
		cerr << "# : ";
	for(int i=1;i<=N;++i)
	{
		fprintf(stderr,"%3d",i);
	}cerr << endl;
		cerr << "A : ";
	for(int i=1;i<=N;++i)
	{
		fprintf(stderr,"%3d",A[i]);
	}cerr << endl;
	
	cerr << "B : ";
	for(int i=1;i<=N;++i)
	{
		fprintf(stderr,"%3d",B[i]);
	}cerr << endl;
	
	cerr << "P : ";
	for(int i=0;i<N;++i)
	{
		fprintf(stderr,"%3d",T[i]);
	}cerr << endl;
	
	cerr << "X : ";
	for(int i=0;i<N;++i)
	{
		fprintf(stderr,"%3d",X[i]);
	}cerr << endl;
	
	cerr << "Y : ";
	for(int i=0;i<N;++i)
	{
	fprintf(stderr,"%3d",Y[i]);
	}cerr << endl;
	}
	else cerr << "correct!"<<endl;
	
}

int main()
{
	freopen("log.txt","w",stderr);
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int test;scanf("%d", &test);
	for(int no=1;no<=test;++no)
	{
		printf("Case #%d:", no);
		run();
	}
}
