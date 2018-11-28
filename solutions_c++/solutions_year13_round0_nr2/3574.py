#include<stdio.h>
int main()
{
    
    int t,y=1;
    FILE *fp=fopen("input.txt","r");
    FILE *f2=fopen("output.txt","w");
    //FILE *f2=fopen("output1.txt","r");
    fscanf(fp,"%d",&t);
    while(t--)
    {
       fprintf(f2,"Case #%d: ",y);y++;
       int i,j,flag=0,x,x1,m,n;
       int A[200][200];
       fscanf(fp,"%d",&m);
       fscanf(fp,"%d",&n);
       for(i=0;i<m;i++)
       for(j=0;j<n;j++)
       fscanf(fp,"%d",&A[i][j]);      
       for(i=0;i<m;i++)
       {
        
        for(j=0;j<n;j++)
        {
              flag=0;
              for(x=0;x<n;x++)
              if(A[i][x]>A[i][j])
              break;               
              for(x1=0;x1<m;x1++)
              if(A[x1][j]>A[i][j])
              break;
              if(x<n&&x1<m)
              {
                           flag=-1;
                           break;
              }
             
             
             
             
        }
        if(flag==-1)
        break;
       }
       if(flag==-1)
       fprintf(f2,"NO\n");
       else          
       fprintf(f2,"YES\n");
    }
    
    return 0;
}    
