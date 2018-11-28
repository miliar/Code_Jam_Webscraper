#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


//------------------------------------------------------------------------------

int minim(int,int);

//------------------------------------------------------------------------------

int main()
{

FILE * f, * g;
f=fopen("B-large.in","r");
g=fopen("OUT.out","w");
int T,contor,N,M;

int a[120][120],i,j,row[120],col[120],p,min;
bool flag;


fscanf (f,"%d",&T); 

for (contor=1;contor<=T;contor++)
    {
    fscanf (f,"%d",&N); 
    fscanf (f,"%d",&M); 
    
    flag=true;
    
    for (i=0;i<N;i++)
        for (j=0;j<M;j++)
            fscanf(f,"%d",&a[i][j]);
    
    for (i=0;i<N;i++)
        {
        p=0;
        for (j=0;j<M;j++)
            {
            if (a[i][j]>a[i][p])
               {
               p=j;                 
               }
            }
        row[i]=a[i][p];
        }
     
    for (j=0;j<M;j++)
        {
        p=0;
        for (i=0;i<N;i++)
            {
            if (a[i][j]>a[p][j])
               {
               p=i;
               }             
            }
        col[j]=a[p][j];             
        }
    
    for (i=0;i<N;i++)
        {
        for (j=0;j<M;j++)
            {
            min=minim(row[i],col[j]);
            if (a[i][j]!=min) flag=false;           
            }
        }    
    
    fprintf(g,"Case #%d: ",contor);
    
    if (flag==true) fprintf(g,"YES");
    else fprintf(g,"NO");
    
    if (contor<T) fprintf(g,"\n");  

    }

return 0;
}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

int minim(int a,int b)
    {
    if (a<b) return a;
    else return b;    
    }




//------------------------------------------------------------------------------
//------------------------------------------------------------------------------





//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
