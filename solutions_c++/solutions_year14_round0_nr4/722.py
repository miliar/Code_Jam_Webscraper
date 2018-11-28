#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


//------------------------------------------------------------------------------

void sort(int);

//------------------------------------------------------------------------------

float a[1002],b[1002];

int main()
{

FILE * f, * g;
f=fopen("D-large.in","r");
g=fopen("OUT.out","w");
int T,contor,N,M;
int poz_a,poz_b,sf_a,sf_b,scor_a,scor_b,scor_WARS,scor_DWARS;


fscanf (f,"%d",&T); 

for (contor=1;contor<=T;contor++)
    {
    fscanf (f,"%d",&N); // printf("\n%d\n",N);

    for (int k=1;k<=N;k++)
        {
        fscanf (f,"%f",&a[k]); //printf("%f ",a[k]);    
        }
    //printf("\n");
    for (int k=1;k<=N;k++)
        {
        fscanf (f,"%f",&b[k]); //printf("%f ",b[k]);  
        }
    //printf("\n");
        
    
    sort(N);
    
    /*
    for (int i=1;i<=N;i++)
        {
        printf("%f ",a[i]);
        }
    printf("\n");
    for (int i=1;i<=N;i++)
        {
        printf("%f ",b[i]);
        }    
    */
    
    //EU incep de la MIN WARS
    
    poz_a=1;
    poz_b=1;
    
    scor_a=0;
    scor_b=0;
    
    while (poz_a<=N && poz_b<=N)
          {
          if (a[poz_a]>b[poz_b]) 
             {
             poz_b++;
             scor_a++;
             }
          else 
               {
               poz_a++;
               poz_b++;
               scor_b++;                  
               }
          }        
    
    //printf("a: %d   b: %d\n",scor_a,scor_b);
    
    scor_WARS=scor_a;
        
    // EU incep de la MAX WARS
    
    poz_a=N;
    poz_b=N;
    
    scor_a=0;
    scor_b=0;
    
    sf_a=1;
    sf_b=1;
    
    while (poz_a>=sf_a && poz_b>=sf_b)
          {
          if (a[poz_a]>b[poz_b]) 
             {
              poz_a--;
              poz_b--;
              scor_a++;                     
             }
          else 
               {
                poz_b--;
                scor_b++; 
                sf_a++;              
               }
          }        
      
    
    //printf("a: %d   b: %d\n",scor_a,scor_b);    
    
    scor_DWARS=scor_a;

    fprintf(g,"Case #%d: ",contor);
 
    fprintf(g,"%d %d",scor_DWARS,scor_WARS);
    
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
