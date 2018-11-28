#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"





#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include<iostream>
using namespace std;





  int main()

  {

   freopen("B-large.in", "r", stdin);
   freopen("BB.out", "w", stdout);

	  int t;scanf("%d",&t);
	  int N[101][101];
	  int m,n;
	  int him[101];
	  int hin[101];
	  int yn;
	 
	  
	for (int cas=1;cas<=t;cas++)
{
		scanf("%d",&m);
		scanf("%d",&n);
	  
	 
	 
	  for (int i=0;i<=m-1;i++)

	  {
		  for (int i1=0;i1<=n-1;i1++)
		  {
			  scanf("%d",&N[i][i1]);
		      
		  }
		  
	  }
	  for (int j=0;j<=m-1;j++)

	  {
		  him[j]=0;
		  for (int k=0;k<=n-1;k++)
		  {
			  if (him[j]<=N[j][k])
			  him[j]=N[j][k];
		  }
		
	  }
	 
      for (int k1=0;k1<=n-1;k1++)
	  {
		  hin[k1]=0;
		  for (int j1=0;j1<=m-1;j1++)
		  {
			  if (hin[k1]<=N[j1][k1])
			  hin[k1]=N[j1][k1];
		  }
		 
	  }
	
	   yn=0;
	  	  for (int j2=0;j2<=m-1;j2++)
	  {
		  for (int k2=0;k2<=n-1;k2++)
		  {
			  if ((him[j2]!=N[j2][k2])&&(hin[k2]!=N[j2][k2]))
			  {  
				  yn=1;
				  break;
				 
			  }
			  
		  }
		  if (yn==1)
			  break;
	  }


		  if (yn==0)
			 cout<<"Case #"<<cas<<": YES"<<endl;
		  else if(yn==1)
			 cout<<"Case #"<<cas<<": NO"<<endl;


			  

	  
		  
}

	  
	  return 0;
  }
				
