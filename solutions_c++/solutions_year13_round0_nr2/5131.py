#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	int t;
	freopen("B-large.in", "r", stdin);
	freopen("blarge.txt", "w", stdout);
	scanf("%d\n",&t);
//	printf("\n scanning ::  %d",t);
	for(int tc = 1; tc <= t; tc++)
    {
		printf("Case #%d: ", tc);
		int n,m;
		int pass=1;
		int lawn[100][100]={0};
		int maxr[100]={0}, maxc[100]={0};
	          scanf("%d %d\n", &n ,&m);
	          for( int i=0; i<n; i++)
	          {
                
	            for( int j=0; j<m; j++)
                 {
                     scanf("%d", &lawn[i][j]);
                     if(maxr[i]<lawn[i][j])
                     maxr[i]=lawn[i][j];
                     if(maxc[j]<lawn[i][j])
                     maxc[j]=lawn[i][j];
                    
                     
                 }
                 scanf("\n");
                }
              
              scanf("\n");
              for( int i=0; i<n; i++)  
              for( int j=0; j<m; j++)
               if( lawn[i][j] != maxr[i] && lawn[i][j] !=maxc[j])
                  pass=0;
              
             
                     
              
              if(pass==0)
              printf("NO\n");
              else
              printf("YES\n");
   }  
                
       return 0;          
                }
                     
    
