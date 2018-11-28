#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

#define MX 111

int n,m;
int A[MX][MX];
int R[MX],C[MX];

int ok(){
	for(int i=0;i<n;++i)
		for(int j=0;j<m;++j)
			if (A[i][j]!=min(R[i],C[j]))
				return 0;
	return 1;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&m);
		memset(R,-1,sizeof R);
		memset(C,-1,sizeof C);
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j){
				scanf("%d",&A[i][j]);
				R[i]=max(R[i],A[i][j]);
				C[j]=max(C[j],A[i][j]);
			}
		puts(ok()?"YES":"NO");
	}
	return 0;
}
