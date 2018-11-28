#include<cstdio>
#include<cstdlib>
#include<stdint.h>
   using namespace std;

 int check(int **matrix,int N,int M)
 {
     int rmax,colmax,i,j,k,l;
     for(i=0;i<N;i++)
     {
         rmax=-1;
         for(j=0;j<M;j++)
         {
             if(matrix[i][j]>rmax) rmax=matrix[i][j];
         }
          for(k=0;k<M;k++)
          {   colmax=-1;
              for(l=0;l<N;l++)
              {
                     if(matrix[l][k]>colmax) colmax=matrix[l][k];
              }
              if(matrix[i][k]<rmax && matrix[i][k]<colmax) return -1;
          }

     }
     return 1;
 }

 int main()
 {   FILE *in,*out;
    in=fopen("F:\\inputs.txt","r");
    out=fopen("F:\\output.txt","w");
    int N,M,i,j,tc,x,**matrix;
     fscanf(in,"%d",&tc);
     for(x=0;x<tc;x++)
     {
         fscanf(in,"%d %d",&N,&M);
         matrix=(int **)malloc(N*sizeof(int*));
         for(i=0;i<N;i++) matrix[i]=(int*)malloc(M*sizeof(int));
         for(i=0;i<N;i++)
         {  for(j=0;j<M;j++)
            {
                fscanf(in,"%d",&matrix[i][j]);
            }
         }

         if(check(matrix,N,M)==1)fprintf(out,"Case #%d: %s\n",x+1,"YES");
         else fprintf(out,"Case #%d: %s\n",x+1,"NO");
     }
     return 0;
 }
