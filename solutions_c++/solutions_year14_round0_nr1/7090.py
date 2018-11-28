#include <cstdio>
#include <cstring>

#define N 4
#define M 16

using namespace std;

int T,ans1,ans2,ans,cnt,A[N+10][N+10],B[N+10][N+10];
bool f[M+10];

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%d",&ans1);
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j) scanf("%d",&A[i][j]);
		scanf("%d",&ans2);
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j) scanf("%d",&B[i][j]);
		printf("Case #%d: ",t);
		memset(f,0,sizeof(f));
		ans=cnt=0;
		for (int i=1;i<=4;++i) f[A[ans1][i]]=1;
		for (int i=1;i<=4;++i) if (f[B[ans2][i]]) ans=B[ans2][i],cnt++;
		if (!cnt) printf("Volunteer cheated!\n");
		else if (cnt>1) printf("Bad magician!\n");else printf("%d\n",ans);
	}
	return 0;
}
