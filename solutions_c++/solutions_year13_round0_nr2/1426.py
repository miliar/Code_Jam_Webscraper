#include <iostream>
#include<cstdio>
int lawn[101][101];

int checkrow(int m,int i,int j)
{
  //   printf("%d %d\n",m,i);
    int temp;
    for(temp=0;temp<m;temp++)
     {
         if(lawn[i][temp]>lawn[i][j])
          return 0;
     }
     
    
     return 1;
}

int checkcol(int n,int j,int i)
{
    int temp;
  //  printf("%d %d\n",n,j);
    for(temp=0;temp<n;temp++)
     {
         if(lawn[temp][j]>lawn[i][j])
          return 0;
     }
     
    
     return 1;
}

using namespace std;

int main() {
    
    int t,k,n,m,cc,cr,i,j;
    FILE *fp,*fp1;
    fp=fopen("input.txt","r");
     fp1=fopen("output.txt","w");
    fscanf(fp,"%d",&t);
    for(k=1;k<=t;k++)
    {
         //int flag=0;
      
        fscanf(fp,"%d %d",&n,&m);
        for(i=0;i<n;i++)
         for(j=0;j<m;j++)
           fscanf(fp,"%d",&lawn[i][j]);
           
           
           
           for(i=0;i<n;i++)
           for(j=0;j<m;j++)
       {      // if(lawn[i][j]==1)
             
                 cr=checkrow(m,i,j);
                 cc=checkcol(n,j,i);
               if(cc==0&&cr==0) 
               {  fprintf(fp1,"Case #%d: NO\n",k);
                    goto abc; }
                    
       }     
           
          
            fprintf(fp1,"Case #%d: YES\n",k);
            
          abc:
            continue; 
          
    }
    
    
	return 0;
}
