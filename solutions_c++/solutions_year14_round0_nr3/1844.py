#include <stdio.h>
using namespace std;

int ans,fox[60][60],i,j,n,m,a[60][60],b[60][60],vsio,vig,t,tt,f,k,u,l;

void dfs(int x,int y)
{
   fox[x][y]=1;
    if (x==0 || x==n+1 || y==0 || y==m+1) return;
     ans++;		
	if (b[x][y]>0) return;
	
	
	if (fox[x-1][y-1]==0)  dfs(x-1,y-1);
	if (fox[x-1][y]==0)    dfs(x-1,y);
	if (fox[x-1][y+1]==0)  dfs(x-1,y+1);
	if (fox[x][y-1]==0)    dfs(x,y-1);
	if (fox[x][y+1]==0)    dfs(x,y+1);
	if (fox[x+1][y-1]==0)  dfs(x+1,y-1);
	if (fox[x+1][y]==0)    dfs(x+1,y);
	if (fox[x+1][y+1]==0)  dfs(x+1,y+1);
	
}

void check()
{
	int i,j;
	
	if (a[2][2]==1 && a[2][4]==1)
	 {
	 	i=1;
	 	j=1;
	 }
	
	
	 for (i=1;i<=n;i++)
	  for (j=1;j<=m;j++)
	   b[i][j]=a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j-1]+a[i][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1];
	   
	  
	 for (i=1;i<=n;i++)
	  for (j=1;j<=m;j++) 
	    if (b[i][j]==0 && a[i][j]==0)
	     {
	     	if (vsio==1) break;
	          ans=0;	
	          dfs(i,j);
               if (ans==f) vsio=1;		   	
	     }
	     
	     
   	 for (u=0;u<=n+1;u++)
	  for (l=0;l<=m+1;l++) 
        fox[u][l]=0;
  
	
}


void go(int x,int y,int z)
{
  if (x>n || y>m) return;
  
  if (vsio==1) return;
      
  	
    if (z<f)
	 {
	  a[x][y]=0;
      if (x+y==n+m && z==f-1) check(); else
      if (y==m) go(x+1,1,z+1); else
      go(x,y+1,z+1);
      
      if (vsio==1) return;
      
     } 
     
     a[x][y]=1;
      
      if (x+y==n+m && z==f) check(); else
      if (y==m) go(x+1,1,z); else
      go(x,y+1,z);
     
     
     if (vsio==1) return;
      
     
}


main()
{
	
	
	freopen ("minesweeper.in","r",stdin);
	freopen ("minesweeper.out","w",stdout);
	
	 scanf ("%d",&t);
	 
	  tt=t;
	   
	    
	    while (t--)
	     {
	 scanf ("%d%d%d",&n,&m,&k);
	 
	      
	       vig=0;
	       vsio=0;
	       
	       
	       f=n*m-k;
	        
	        if (n==1 || m==1 || f==1)
	         {
	         printf ("Case #%d:\n",tt-t);
	           for (i=1;i<=n;i++)
			    {
			      for (j=1;j<=m;j++)
				   if (i+j==2) printf ("c"); else
				   if (i+j<=f+1) printf ("."); else
				    printf ("*");
				    printf ("\n");
				}
				   	
	           continue;	
	         }
	        
	        go(1,1,0);
	        
	          printf ("Case #%d:\n",tt-t);
			   
	        if (vsio==0)
	        {
	       printf ("Impossible\n");
	       
	     	 continue;
	        }
	        
	        
     	 for (i=1;i<=n;i++)
    	   {
		     for (j=1;j<=m;j++)
			  if (a[i][j]==0)
			   {
			   	 if (vig==0 && b[i][j]==0) {printf ("c"); vig=1;} else
					printf ("."); 
			   } else printf ("*");
			 
			    printf ("\n");
           }
	        
	     }
	
	
	
	
}
