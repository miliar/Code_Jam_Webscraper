#include<cstdio>
#include<algorithm>

using namespace std;

int W[111];
int H[111];
int T[111][111];

int NN;

void test(){
	int n,m;
	printf("Case #%d: ",++NN);
	scanf("%d%d",&n,&m);
	for (int i=0;i<n;i++) W[i]=0;
	for (int i=0;i<m;i++) H[i]=0;
	
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++){
			scanf("%d",&T[i][j]);
			W[i]=max(W[i],T[i][j]);
			H[j]=max(H[j],T[i][j]);
		}
	
	int C=1;
	
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(W[i]>T[i][j] && H[j]>T[i][j]) C=0;
	
	if(C) printf("YES\n");
	else printf("NO\n");
	
	
}

int main(){
	int t;
	scanf("%d",&t);
	while(t--) test();
   return 0;
}

