#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>
#pragma comment(linker, "/STACK:10000000") 
#define md 1000000007

using namespace std;

int k,n,m,i,t,test,j,a[105][105],p[105][105];
bool b[105][105],w[105],h[105],ok;

FILE* f,*g;

int main()
{
	f = fopen("input.txt","r");
	g = fopen("output.txt","w");
	fscanf(f,"%d\n",&t);
	
	for (test=1;test<=t;test++)
	{
		fscanf(f,"%d %d",&n,&m);
		for (i=1;i<=n;i++)
		 for (j=1;j<=m;j++) a[i][j] = 100;
		 ok = true;
		 
		for (i=1;i<=n;i++)
		 for (j=1;j<=m;j++) fscanf(f,"%d",&p[i][j]);	
		for (k=1;k<=100;k++)
		{
		 	for (i=1;i<=n;i++)
		 	 for (j=1;j<=m;j++) b[i][j]=false;
		 	 
		 	 for (i=1;i<=n;i++)
		 	  for (j=1;j<=m;j++) if (a[i][j]>p[i][j])
		 	  {
				a[i][j]--;
				b[i][j]=true;		
			  }
			 for (i=1;i<=n;i++) w[i] = b[i][1];
			 for (j=1;j<=m;j++) h[j] = b[1][j];
			 for (i=1;i<=n;i++)
			  for (j=1;j<=m;j++)
			  {
				if (j>1) w[i] = (w[i] && b[i][j]);
				if (i>1) h[j] = (h[j] && b[i][j]);		
			  } 
			  for (i=1;i<=n;i++)
			   for (j=1;j<=m;j++) ok = (ok && (!b[i][j] || (b[i][j] && (w[i] || h[j]))));
			  if (!ok) break;
		} 
		 
		if (ok) fprintf(g,"Case #%d: YES\n",test); else fprintf(g,"Case #%d: NO\n",test);
/*		for (i=1;i<=n;i++)
		{
			for (j=1;j<=m;j++) fprintf(g,"%d ",p[i][j]);
			fprintf(g,"\n");	
		}*/
	}	
}
