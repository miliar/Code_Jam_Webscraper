#include<stdio.h>
#include<algorithm>
#include<vector>
#include<functional>
#define all(A) (A).begin(), (A).end()
#define II(A) int (A); scanf("%d",&(A));
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int MN = 4 + 1;
const int INF = 10000;

int A[MN][MN];
int perm[MN];
int N;
int used[MN];

bool test(int n){
	if(n==N)return true;
	bool flag=true;
	int possible[MN];
	for(int i=0;i<N;i++){
		possible[i]=(!used[i])&A[perm[n]][i];
		if(possible[i])flag=false;
	}
	if(flag)return false;
	for(int i=0;i<N;i++)if(possible[i]){
		used[i]=1;
		if(!test(n+1))return false;
		used[i]=0;
	}
	return true;
}

int makearray(int i,int j,int c){
	if(i==N){
		for(int it=0;it<N;it++)perm[it]=it;
		do{
			for(int it=0;it<N;it++)used[it]=0;
			if(!test(0))return INF;
		}while(next_permutation(perm,perm+N));
		return c;
	}
	if(j==N){
		return makearray(i+1,0,c);
	}
	if(A[i][j]==1){
		return makearray(i,j+1,c);
	}
	A[i][j]=1;
	int v1=makearray(i,j+1,c+1);
	A[i][j]=0;
	int v2=makearray(i,j+1,c);
	return min(v1,v2);
}

int main(){
	freopen("input.txt","r",stdin),freopen("output.txt","w",stdout);
	int TC;
	scanf("%d",&TC);
	for(int tc=1;tc<=TC;tc++){
		scanf("%d",&N);
		for(int i=0;i<N;i++)for(int j=0;j<N;j++)scanf("%1d",&A[i][j]);
		int ans = makearray(0,0,0);
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}