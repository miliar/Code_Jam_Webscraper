#include <cstdio>
#include <algorithm>

#define Rep(i,l,r)			for(int i = (l) ; i <= (r) ; i++)

using namespace std ;

int a[110][110] , b[110][110] ;

int n,m ;

int main()
{
	freopen("in.txt","r",stdin) , freopen("out.txt","w",stdout) ;
	int T ; scanf("%d\n",&T) ; Rep(TT,1,T)
	{
		scanf("%d %d",&n,&m) ;
		Rep(i,1,n)
			Rep(j,1,m)	scanf("%d",&a[i][j]) , b[i][j] = 100 ;
		Rep(i,1,n)
		{
			int M = 0 ;
			Rep(j,1,m)	M = max(a[i][j] , M) ;
			Rep(j,1,m)	b[i][j] = M ;
		}
		Rep(j,1,m)
		{
			int M = 0 ;
			Rep(i,1,n)	M = max(a[i][j] , M) ;
			Rep(i,1,n)	b[i][j] = min(b[i][j] , M) ;
		}
		bool sig = true ;
		Rep(i,1,n)
			Rep(j,1,m)	sig &= (b[i][j] == a[i][j]) ;
		printf("Case #%d: %s\n",TT,(sig?("YES"):("NO"))) ;
	}
	return 0 ;
}
