#include<cstdio>
#include<vector>

using namespace std;

int Kl[210];

int S[210][210];
int C[210];

int CZ[2000000],n;
vector<int> V;

int W;

int dfs(int A){
	CZ[A]=1;
//	printf("A: %d\n", A);
	if(__builtin_popcount(A)==n){
		W=1;
		for(int i=0;i<V.size();i++) printf(" %d", V[i]+1);
	}
	for(int i=0;i<n;i++){
//		printf("   %d    %d || %d %d	\n", A,i,C[i],Kl[C[i]]);
		if(Kl[C[i]]!=0 && CZ[A|(1<<i)]==0 && 0==(A&(1<<i))){
			Kl[C[i]]--;
			V.push_back(i);
			for(int j=0;j<210;j++) Kl[j]+=S[i][j]; 
			dfs(A|(1<<i));
			for(int j=0;j<210;j++) Kl[j]-=S[i][j];
			V.pop_back();
			Kl[C[i]]++;
		}
	}
}

int T;
void test(){
	printf("Case #%d:", ++T);
	W=0;
	int k;
	scanf("%d%d",&k,&n);
	for(int i=0;i<210;i++) Kl[i]=0;
	for(int i=0;i<210;i++)
	 for(int j=0;j<210;j++)
	 	S[i][j]=0;
	for(int i=0;i<k;i++){
		int a;
		scanf("%d",&a);
		Kl[a]++;
	}
	for(int i=0;i<n;i++){
		int a,b;
		scanf("%d%d",&C[i],&a);
		for(int j=0;j<a;j++){
			scanf("%d", &b);
			S[i][b]++;
		}
	}
	for(int i=0;i<2000000;i++) CZ[i]=0;
	dfs(0);
	if(!W) printf(" IMPOSSIBLE");
	printf("\n");
}

int main(){
	int t;
	scanf("%d",&t);
	while(t--) test();
   return 0;
}

