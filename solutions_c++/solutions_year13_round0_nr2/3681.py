#include<cstdio>
#include<cstring>
using namespace std;
int a[105][105];
int main()
{
	int cas;
	int n,m;
	int ca = 0;
	scanf( "%d", &cas );
	while ( cas-- )
	{
		scanf( "%d%d", &n, &m );
		for ( int i = 0; i < n; i++ )
			for ( int j = 0; j < m; j++ )
				scanf("%d", &a[i][j] );
		bool u = true;
		for ( int i = 0; i < n; i++ )
		{
			for ( int j = 0; j < m; j++ )
			{
				bool f1 = false;
				bool f = true;
				for ( int k = 0; k < m; k++ )
				if ( a[i][k] > a[i][j] ) f = false;
				if ( f ) f1 = true;	
				f = true;
				for ( int k = 0; k < n; k++ )
				if ( a[k][j] > a[i][j] ) f = false;
				if ( f ) f1 = true;
				if ( f1 == false ) 	
				{
					u = false;
					break;
				}
			}
			if ( u == false ) break;
		}
		ca++;
		printf("Case #%d: ",ca);
		if ( u ) 
		printf("YES\n");
		else
		printf("NO\n");
	}
	return 0;
}
