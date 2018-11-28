#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int a[110][110];
int row[110];
int col[110];
int main()
{
 	freopen("B-small-attempt0.in","r",stdin);
 	freopen("output.txt","w",stdout);
 	int T;
 	scanf("%d",&T);
 	for(int cas=1;cas<=T;cas++)
 	{
        int N,M;
        scanf("%d%d",&N,&M);
        for(int i=0;i<N;i++)
         for(int j=0;j<M;j++)
           scanf("%d",&a[i][j]);
        if(N==1||M==1)
        {
         printf("Case #%d: YES\n",cas);
         continue;
		 }
        for(int i=0;i<N;i++)
        {
 		  int minx=1000;
 		  for(int j=0;j<M;j++)
 		  {
	        if(a[i][j]<minx)
	        {
 				minx=a[i][j];
			}
		  }
		  row[i]=minx;
	   }
	   for(int i=0;i<M;i++)
	   {
	     int minx=1000;
	     for(int j=0;j<N;j++)
	     {
 		   if(a[j][i]<minx)
 		   {
	          minx=a[j][i];
		   }
	     }
	     col[i]=minx;
	    }
	    int flagRes=1;
	    for(int i=0;i<N&&flagRes;i++)
	     for(int j=0;j<M&&flagRes;j++)
	     {
  		   if(a[i][j]==row[i]&&a[i][j]!=col[j])
  		   {
			  for(int k=0;k<M;k++)
			  {
                 if(a[i][k]!=a[i][j])
                 {
                   flagRes=0;
                   break;
		         }
		       }
		    }
		    if(a[i][j]!=row[i]&&a[i][j]==col[j])
		    {
			     for(int k=0;k<N;k++)
			     {
	  		        if(a[k][j]!=a[i][j])
 		            {
 					   flagRes=0;
 					   break;
			        }
				}
			}
			if(a[i][j]==row[i]&&a[i][j]==col[j])
			{
			   int flag1=1,flag2=1;
			   for(int k=0;k<M;k++)
			  {
                 if(a[i][k]!=a[i][j])
                 {
                   flag1=0;
                   break;
		         }
		       }
		        for(int k=0;k<N;k++)
			     {
	  		        if(a[k][j]!=a[i][j])
 		            {
 					   flag2=0;
 					   break;
			        }
				}
				if(!flag1&&!flag2)
				{
                  flagRes=0;
                  break;
		       } 
	         }//endo of if
		 }//endo of for
		 if(flagRes==1)
	     {
           printf("Case #%d: YES\n",cas);
         }
         else
         {
 	       printf("Case #%d: NO\n",cas);
          }
      }
      return 0;
}
