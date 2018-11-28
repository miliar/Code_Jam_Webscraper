#include <cstdio>
using namespace std;

int cas=1,t,p,n,i,j,k,m,val;
bool colFound,rowFound,possible;
int mat[200][200];

int main()
{
  scanf("%d",&t);
  p=t;
  while(p--)
  {
    
    if(cas<=t&&cas>1)
      printf("\n");
    
    scanf("%d %d",&m,&n);
    
    for(i=0;i<m;i++)
      for(j=0;j<n;j++)
        scanf("%d",&mat[i][j]);
    
    possible=true;
    
    for(i=0;i<m&&possible;i++)
      for(j=0;j<n;j++)
      {
     	val=mat[i][j]; 
      	colFound=false;
        for(k=0;k<m;k++)
          if(val<mat[k][j])
            colFound=true;
        
        rowFound=false;
      
        for(k=0;k<n;k++)
          if(val<mat[i][k])
            rowFound=true;
        if(colFound && rowFound)
        { possible=false; break;}
      }
    
    if(possible)
      printf("Case #%d: YES",cas++);
    else
   	  printf("Case #%d: NO",cas++);
    
  }
  return 0;
}	