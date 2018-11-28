#include<stdio.h>
#include<algorithm>
#include<vector>
#include<functional>
#define all(A) (A).begin(), (A).end()
#define II(A) int (A); scanf("%d",&(A));
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int MN = 100+5;
int N,M;
int st[MN],ed[MN];
int A[MN][MN];
int dx[]={-1,0,1,0},dy[]={0,1,0,-1};

int go(int x,int y,int dir){
	if(x<0)return y;	//upside
	if(y>=M)return M+x;	//rightside
	if(x>=N)return N+M+M-1-y;
	if(y<0)return N+M+M+N-1-x;
	int newdir;
	if(A[x][y]==1){	// '/'
		newdir=dir^1;
		return go(x+dx[newdir],y+dy[newdir],newdir);
	}
	else{	// '\'
		newdir=3-dir;
		return go(x+dx[newdir],y+dy[newdir],newdir);
	}
}

int gofrom(int n){
	if(n<M){	//upside
		return go(0,n,2);
	}
	else if(n<N+M){	//rightside
		return go(n-M,M-1,3);
	}
	else if(n<N+M+M){	//downside
		return go(N-1,N+M+M-1-n,0);
	}
	else{	//leftside
		return go(N+M+N+M-1-n,0,1);
	}
}

bool dfs(int x,int y){
	if(x==N){
		for(int i=0;i<N+M;i++){
			if(gofrom(st[i])!=ed[i])return false;
		}
		return true;
	}
	if(y==M){
		return dfs(x+1,0);
	}
	A[x][y]=1;
	if(dfs(x,y+1))return true;
	A[x][y]=2;
	return dfs(x,y+1);
}

int main(){
	freopen("input.txt","r",stdin),freopen("output.txt","w",stdout);
	int TC;
	scanf("%d",&TC);
	for(int tc=1;tc<=TC;tc++){
		scanf("%d%d",&N,&M);
		for(int i=0;i<N+M;i++){
			II(a)II(b);--a,--b;
			st[i]=a,ed[i]=b;
		}
		printf("Case #%d:\n",tc);
		if(!dfs(0,0)){
			puts("IMPOSSIBLE");
		}
		else{
			for(int i=0;i<N;i++){
				for(int j=0;j<M;j++){
					if(A[i][j]==1)printf("/");
					else printf("\\");
				}
				printf("\n");
			}
		}
	}
	return 0;
}