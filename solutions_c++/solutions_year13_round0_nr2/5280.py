#include "cstdio"
#include "algorithm"
using namespace std;
long long t,n,m,c,w[1000005],k[1000005],tab[1001][1001];
bool tak;
int main()
{
	scanf ("%lld", &t);
	
	for (int i=0; i<t; i++)
	{
		scanf ("%lld%lld", &n, &m);
		tak=true;
		
		printf ("Case #%d: ", i+1);
		
		for (int x=0; x<n; x++)
		{
			for (int y=0; y<m; y++)
			{
				scanf ("%lld", &c);
				tab[x][y]=c;
				w[x]=max(w[x],c);
				k[y]=max(k[y],c);
			}
		}
		
		for (int x=0; x<n; x++)
		{
			for (int y=0; y<m; y++)
			{
				if (w[x]>tab[x][y] && k[y]>tab[x][y])
				{
					tak=false;
					break;
				}
			}
		}
		
		(tak) ? printf ("YES\n") : printf ("NO\n");
		
		for (int x=0; x<n; x++) w[x]=0;
		for (int y=0; y<m; y++) k[y]=0;
	}
	
	return 0;
}
