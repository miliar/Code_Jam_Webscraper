#include <iostream>
#include <stdio.h>
using namespace std;

int ans,fix[60][60],i,j,n,m,a[60][60],b[60][60],vsio,avi,t,t1,f,k,u,l;

void dfs(int x,int y)
{
   fix[x][y]=1;
    if (x==0 || x==n+1 || y==0 || y==m+1) return;
     ans++;		
	if (b[x][y]>0) return;
	
	
	if (fix[x-1][y-1]==0)  dfs(x-1,y-1);
	if (fix[x-1][y]==0)    dfs(x-1,y);
	if (fix[x-1][y+1]==0)  dfs(x-1,y+1);
	if (fix[x][y-1]==0)    dfs(x,y-1);
	if (fix[x][y+1]==0)    dfs(x,y+1);
	if (fix[x+1][y-1]==0)  dfs(x+1,y-1);
	if (fix[x+1][y]==0)    dfs(x+1,y);
	if (fix[x+1][y+1]==0)  dfs(x+1,y+1);
	
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
        fix[u][l]=0;
  
	
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
	
	
	freopen ("mine.in","r",stdin);
	freopen ("mine.out","w",stdout);
	
	 cin>>t;
	  t1=t;
	   
	    
	    while (t--)
	     {
	      cin>>n>>m>>k;
	       avi=0;
	       vsio=0;
	       
	       
	       f=n*m-k;
	        
	        if (n==1 || m==1 || f==1)
	         {
	          cout<<"Case #"<<t1-t<<":"<<endl;	
	           for (i=1;i<=n;i++)
			    {
			      for (j=1;j<=m;j++)
				   if (i+j==2) cout<<'c'; else
				   if (i+j<=f+1) cout<<'.'; else
				    cout<<'*';
				    cout<<endl;
				}
				   	
	           continue;	
	         }
	        
	        go(1,1,0);
	         cout<<"Case #"<<t1-t<<":"<<endl;
	         
	        if (vsio==0)
	        {
	         cout<<"Impossible"<<endl;
	     	 continue;
	        }
	        
	        
     	 for (i=1;i<=n;i++)
    	   {
		     for (j=1;j<=m;j++)
			  if (a[i][j]==0)
			   {
			   	 if (avi==0 && b[i][j]==0) {cout<<'c'; avi=1;} else
					cout<<'.'; 
			   } else cout<<'*';
			 
			    cout<<endl;
           }
	        
	     }
	
	
	
	
}
