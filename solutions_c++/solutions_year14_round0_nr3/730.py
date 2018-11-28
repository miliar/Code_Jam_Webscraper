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
f=fopen("C-large.in","r");
g=fopen("OUT.out","w");
int T,contor,N;
int R,C,M,A,inca,poz_r,poz_c;
bool flag;



fscanf (f,"%d",&T); 

for (contor=1;contor<=T;contor++)
    {
    
    
    
    
    fscanf (f,"%d",&R); 
    fscanf (f,"%d",&C); 
    fscanf (f,"%d",&M); 

    //-------------------------------------------
    
    
    flag=true;
    
    //M=0;
    
    A=R*C-M;

    
    char mat[R][C];
    
    //printf("\n%d %d %d\n",R,C,A);
    //getch();
    if (R*C<=A) flag=false;
    if ((R==2 && C>=2)||(C==2 && R>=2)) 
       {
       if (A==2 || (A%2==1 && A>1))
          {
          flag=false;      
          }       
       }
    if ((R>=3 && C>=3)||(C>=3 && R>=3))
       {
       if (A==2 || A==3 || A==5 || A==7)
          {
          flag=false;      
          }        
       }
    
    if (M==0)
       {
        for (int i=0;i<R;i++)
            {
            for (int j=0;j<C;j++) 
                {
                mat[i][j]='.';     
                }             
            }
       mat[R-1][C-1]='c';
       }
       
    if (M==R*C-1)
       {
        for (int i=0;i<R;i++)
            {
            for (int j=0;j<C;j++) 
                {
                mat[i][j]='*';     
                }             
            }
       mat[R-1][C-1]='c';
       flag=false;
       }   
    
    if (flag)
       {
        
       
       if (R==1)
          { 
          for (int i=0;i<M;i++)
              {
              mat[0][i]='*';     
              }
          for (int i=M;i<C;i++)
              {
              mat[0][i]='.';     
              }
             mat[R-1][C-1]='c';
          }
          
       else if (C==1)
            {
             for (int i=0;i<M;i++)
              {
              mat[i][0]='*';     
              }  
             for (int i=M;i<R;i++)
              {
              mat[i][0]='.';     
              }  
              mat[R-1][C-1]='c';    
            }
       else
           {

           if (A==9 && C>=3 && R>=3)
              {
              for (int i=0;i<R;i++)
                    {
                    for (int j=0;j<C;j++)
                        {
                        mat[i][j]='*';
                        }
                    }
              
              for (int i=R-3;i<R;i++)
                    {
                    for (int j=C-3;j<C;j++)
                        {
                        mat[i][j]='.';
                        }
                    }
              mat[R-1][C-1]='c';  
              }
           else //cazul general
               {      
               inca=M;
               
               for (int i=0;i<R;i++)
                {
                for (int j=0;j<C;j++)
                    {
                    mat[i][j]='.';
                    }     
                }
               
               for (int i=0;i<(R-2);i++)
                    {
                    for (int j=0;j<C;j++)
                        {
                        if (inca) 
                           {
                           mat[i][j]='*';
                           inca--;
                           }
                        else 
                             {
                             //poz_r=i;
                             //poz_c=j-1;     
                             }   
                        
                        }
                    }   
                
                
                if (inca==0)
                {
                
                poz_c=C-2;
                for (int i=0;i<R;i++)
                    {
                    if (mat[i][poz_c]=='.') 
                       {
                       poz_r=i-1;
                       break;                     
                       }     
                    }
                
                if (A%C==1)
                   {
                   mat[poz_r][poz_c]='.';//.
                   //if (mat[poz_r][0]=='*') printf("PROBLEMA %d %d 1 !!\n",poz_r,poz_c);
                   mat[poz_r+1][0]='*'; //*
                   if (mat[R-2][0]=='*') ///////////*
                      {
                       mat[poz_r][poz_c-1]='.';   //.         
                       mat[poz_r+2][0]='*';//*
                      }
                   }            
                }
                else
                {
                if (inca%2==0)
                   {     
                    for (int j=0;j<=C;j++)
                        {
                        for (int i=R-2;i<R;i++) 
                            {
                            if (inca) 
                               {
                               mat[i][j]='*';
                               inca--;
                               }    
                            }    
                        }     
                   }  
                else 
                     {
                     mat[R-3][C-1]='.';
                     mat[R-3][C-2]='.';
                     mat[R-3][C-3]='.';
                     inca+=3;
                     for (int j=0;j<=C;j++)
                        {
                        for (int i=R-2;i<R;i++) 
                            {
                            if (inca) 
                               {
                               mat[i][j]='*';
                               inca--;
                               }    
                            }    
                        }         
                     }
                  }   
                mat[R-1][C-1]='c';
                }   
           }    
                   
       }
    
    int suma=0;
    
    fprintf(g,"Case #%d: \n",contor);
    
    if ((!flag) && M!=0 && M!=(R*C-1))
       {
       fprintf(g,"Impossible"); 
       //if (A!=2 && A!=3 && A!=5) printf("Impossible %d*%d=%d  -  %d = %d\n\n",R,C,R*C,M,A);     
       }
    else
       {
       for (int i=0;i<R;i++)
            {
            for (int j=0;j<C;j++)
                {
                fprintf(g,"%c",mat[i][j]);
                if (mat[i][j]=='*') suma++;
                }     
            if (i<R-1) fprintf(g,"\n");
            }                             
       /*
       if (suma!=M )
        {
        printf("\n\nATENTIE : loc: %d | mine : %d | stele : %d\n",R*C,M,suma);
        for (int i=0;i<R;i++)
            {
            for (int j=0;j<C;j++)
                {
                printf("%c ",mat[i][j]);
                }     
            if (i<R-1) printf("\n");
            }
        
        }*/
       
       //if (mat[R-1][C-1]!='c') printf("NU");
       }
    /*
     
    */
 
    //fprintf(g,"%f",suma);
    
    if (contor<T) fprintf(g,"\n");  



    //-------------------

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
