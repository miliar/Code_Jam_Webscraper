#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


//------------------------------------------------------------------------------

int minim(int,int);

//------------------------------------------------------------------------------

int main()
{

FILE * f, * g;
f=fopen("A-small-attempt0.in","r");
g=fopen("OUT.out","w");
int T,contor,N,M;
int a[4][4],b[4][4];
int count,poz;

fscanf (f,"%d",&T); 

for (contor=1;contor<=T;contor++)
    {
    count=0;
    fscanf (f,"%d",&N); 
    for (int i=0;i<4;i++)
        {
        for (int j=0;j<4;j++)
            {
            fscanf (f,"%d",&a[i][j]);
            //printf("%d ",a[i][j]);
            }     
        //printf("\n");
        }
    //printf("\n");
    fscanf (f,"%d",&M); 
    for (int i=0;i<4;i++)
        {
        for (int j=0;j<4;j++)
            {
            fscanf (f,"%d ",&b[i][j]);
            //printf("%d ",b[i][j]);
            }     
        //printf("\n");
        }
    //printf("\n");
    for (int i=0;i<4;i++)
        {
        for (int j=0;j<4;j++)
            {
            //printf("%d: %d >< %d\n",count,a[N-1][i],b[M-1][j]); 
            if (a[N-1][i]==b[M-1][j]) 
               {
               count++; 
               poz=i;             
               }    
            }     
        }
    fprintf(g,"Case #%d: ",contor);
    if (count==1) fprintf(g,"%d",a[N-1][poz]);
    else if (count>1) fprintf(g,"Bad magician!");
    else if (count==0) fprintf(g,"Volunteer cheated!");
    
    if (contor<T) fprintf(g,"\n");  

    }

//getch();
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
