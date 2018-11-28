#include<stdio.h>
#include<string.h>
#define max(a,b) (a)>(b)?(a):(b)

const int maxn = 1024;

int up[maxn][maxn],dn[maxn][maxn];
int lf[maxn][maxn],rt[maxn][maxn];

int a[maxn][maxn];


int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	scanf("%d",&T);
	for ( int kk=1;kk<=T;kk++ ){
		int M,N;
		memset(up,0,sizeof up);
		memset(dn,0,sizeof dn);
		memset(lf,0,sizeof lf);
		memset(rt,0,sizeof rt);
		memset(a,0,sizeof a);
		scanf("%d%d",&N,&M);
		for ( int i=1;i<=N;i++ )
			for ( int j=1; j<=M; j++ ){
				scanf ( "%d",&a[i][j] );
				lf[i][j] = max(lf[i][j-1],a[i][j]);
				up[i][j] = max(up[i-1][j],a[i][j]);
			}
		for ( int i=N;i;i-- )
			for ( int j=M;j;j-- ){
				rt[i][j] = max(rt[i][j+1],a[i][j]);
				dn[i][j] = max(dn[i+1][j],a[i][j]);
			}
		int ans=1;
		for ( int i=1;i<=N;i++ )
			for ( int j=1;j<=M;j++ ) {
				int ii=0,jj=0,k = a[i][j];
				if ( k >= up[i][j] && k >= dn[i][j] ) ii = 1;
				if ( k >= lf[i][j] && k >= rt[i][j] ) jj = 1;
				ans &= ( ii | jj );
			}
		printf("Case #%d: ",kk);
		if ( ans ) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
