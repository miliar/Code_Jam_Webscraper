#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


//------------------------------------------------------------------------------

void sort(int);

//------------------------------------------------------------------------------

float a[2002],b[2002];

int main()
{

FILE * f, * g;
f=fopen("B-large.in","r");
g=fopen("OUT.out","w");
int T,contor,N,M;
float A,B,C,F,X;
bool flag;
 double suma;



fscanf (f,"%d",&T); 

for (contor=1;contor<=T;contor++)
    {
    fscanf (f,"%f",&C); 
    fscanf (f,"%f",&F); 
    fscanf (f,"%f",&X); 
    
    //printf("%f, %f, %f\n",C,F,X);
    
    flag=true;
    N=0;
    
    while (flag)
          {
          A=X/(N*F+2);
          B=C/(N*F+2)+X/((N+1)*F+2);
          //printf("%d : %f %f\n",N,A,B);
          //getch();
          if (A<B) 
             {
             break;      
             }
          N++;
          }
    
    suma=0;
    
    for (int i=0;i<N;i++)
        {
        suma=suma+C/(i*F+2);
        //printf("%f ",C/(i*F+2));  
        }
    
    suma=suma+X/(N*F+2);
    //printf("%f ",X/(N*F+2)); 
    //printf("\n%f \n",suma);
    
    
    //printf("%d : %f %f\n",N,A,B);
    
    
    
    fprintf(g,"Case #%d: ",contor);
 
    fprintf(g,"%f",suma);
    
    if (contor<T) fprintf(g,"\n");  

    }

//getch();
return 0;
}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void sort(int n)
{
int min1,min2;
float aux;
for (int i=1;i<=n;i++)
    {
    min1=i;
    min2=i;
    for (int j=i+1;j<=n;j++)
        {
        if (a[j]<a[min1]) min1=j;     
        if (b[j]<b[min2]) min2=j; 
        }
    aux=a[i];
    a[i]=a[min1];
    a[min1]=aux;
    aux=b[i];
    b[i]=b[min2];
    b[min2]=aux;
    }
}



//------------------------------------------------------------------------------
//------------------------------------------------------------------------------





//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
