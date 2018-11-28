#include<cstdio>
#include<algorithm>
using namespace std;
int a[101][101], l[101][101], g[101][101], p[101][101], d[101][101];

int main()
{
int t, res;
scanf("%d", &t);
for (int k=1; k<=t; k++)
{
	int n, m, i, j;
	scanf("%d%d", &n, &m);
	for (i=0; i<n; i++)
		for (j=0; j<m; j++)
			scanf("%d", &a[i][j]);
			
			
	for (i=0; i<n; i++)
		for (j=0; j<m; j++)
		{
			if(i==0) g[i][j] = a[i][j];
			else 
				g[i][j] = max(a[i][j], g[i-1][j]);
		}
			
	for (i=0; i<n; i++)
		for (j=0; j<m; j++)
		{
			if(j==0) l[i][j] = a[i][j];
			else 
				l[i][j] = max(a[i][j], l[i][j-1]);
		}
	
	///////////////////////
	
	for (i=n-1; i>=0; i--)
		for (j=m-1; j>=0; j--)
		{
			if(i==n-1) d[i][j] = a[i][j];
			else 
				d[i][j] = max(a[i][j], d[i+1][j]);
		}
		
		
	for (i=n-1; i>=0; i--)
		for (j=m-1; j>=0; j--)
		{
			if(j==m-1) p[i][j] = a[i][j];
			else 
				p[i][j] = max(a[i][j], p[i][j+1]);
		}
			
	
	//////////////////////////////////
	
	for (i=0; i<n; i++)
		for (j=0; j<m; j++)
			if((g[i][j] > a[i][j] || d[i][j] > a[i][j]) && (l[i][j] > a[i][j] || p[i][j] > a[i][j]))
				goto moskwa;
				
	
				
	printf("Case #%d: YES\n", k);
	continue;
	
	moskwa:;
				
	printf("Case #%d: NO\n", k);
}
return 0;
}			
			
			
			
