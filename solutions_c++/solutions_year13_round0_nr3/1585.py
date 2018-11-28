#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


//------------------------------------------------------------------------------

bool pal_1(int);
bool pal(int);
void write_p(int,int,int);
void multiply(int);

bool biggerthanA();
bool smallerthanB();

void write_invect(int);

//------------------------------------------------------------------------------

int s[100],vect[100],A,B,lengthA,lengthB,intA[100],intB[100],XXX,YYY;

//------------------------------------------------------------------------------

int main()
{

FILE * f, * g;
f=fopen("C-large-1.in","r");
g=fopen("OUT.out","w");
int T,contor,nr_pal,ia,ib,i;
char charA[110],charB[110],temp;
    
    

fscanf (f,"%d",&T); 
fscanf (f,"%c",&temp);
fscanf (f,"%c",&temp);

for (contor=1;contor<=T;contor++)
    {

    nr_pal=0;
    ia=0;ib=0;
    
    while(temp>='0' && temp<='9')
    {
     charA[ia]=temp;   
     fscanf(f,"%c",&temp);   
     ia++;   
    } 
    
   // for (i=0;i<ia;i++)
    //    {
     //   printf("%d",charA[i]);              
      //  }
    
    
    
    fscanf (f,"%c",&temp);
    
    while(temp>='0' && temp<='9')
    {
     charB[ib]=temp;
     fscanf (f,"%c",&temp);  
     ib++;      
    }    
    
    
    
    
    
    fscanf (f,"%c",&temp);
    
    lengthA=ia;      
    
    lengthB=ib; 
    
    for (i=0;i<ia;i++)
        {
        intA[i]=charA[i]-'0';              
        }
    
    for (i=0;i<ib;i++)
        {
        intB[i]=charB[i]-'0';              
        }  

       
  //start ALGO  
            
            
            
          
                    
           int nr,nr2,i;
                  
           char a[100];


          
            
            
            
            for (nr=1;nr<10000;nr++)
                {
                
                //printf("test");                    
                
                if (pal_1(nr)==true)
                   {
                   nr2=nr*nr;

                   for (i=0;i<100;i++) vect[i]=0; 

                   write_invect(nr2);
                   
                   
                   
                   if (biggerthanA()==true && smallerthanB()==true)
                      {
                      if (pal_1(nr2)==true)
                         {
                         nr_pal++;
                         //printf("%d\n\n",nr2);
                         
                         }        
                      }
                  
              
                   }                      
                }
           

            
            
            for (nr=100;nr<999;nr++) //de la 10001 la 999999   5/6 cifre =>     9 / 11
                    {
                    
                    for (i=0;i<100;i++) vect[i]=0; // init vect de produs
                    
                    write_p(nr,0,3); // generat palindrom in s
            
                    multiply(6);  // generat s patrat
                    
                    
                    //printf("\nT:%d",contor);
                    
                    
                    if (pal(12)==true)
                       {
                       if (biggerthanA()==true && smallerthanB()==true) nr_pal++; //printf("\n\n%d par  ESTEEEEEEE\n\n",nr);
                 
                       }
                   
                    
                    for (i=0;i<100;i++) vect[i]=0; // init vect de produs
                    
                    write_p(nr,1,3); // generat palindrom in s
            
                    multiply(5);  // generat s patrat
                    
                    if (pal(10)==true)
                       {
                       if (biggerthanA()==true && smallerthanB()==true) nr_pal++; //printf("\n\n%d  impar ESTEEEEEEE\n\n",nr);
                       }
                    }
            
            
            for (nr=1000;nr<9999;nr++) //de la 1000001 la 99999999   7/8 cifre => 
                    {
                    
                    for (i=0;i<100;i++) vect[i]=0; // init vect de produs
                    
                    write_p(nr,0,4); // generat palindrom in s
            
                    multiply(8);  // generat s patrat
                    
                    if (pal(16)==true)
                       {
                       if (biggerthanA()==true && smallerthanB()==true) nr_pal++; //printf("\n\n%d par  ESTEEEEEEE\n\n",nr);
              
                       }
                  
                    
                    for (i=0;i<100;i++) vect[i]=0; // init vect de produs
                    
                    write_p(nr,1,4); // generat palindrom in s
            
                    multiply(7);  // generat s patrat
                    
                    if (pal(14)==true)
                       {
                       if (biggerthanA()==true && smallerthanB()==true) nr_pal++; //printf("\n\n%d impar  ESTEEEEEEE\n\n",nr);
                  
                       }
                    }
                    
          


fprintf(g,"Case #%d: %d",contor,nr_pal);


if (contor<T) fprintf(g,"\n"); 


}

//printf("end");



return 0;
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void write_invect(int nr2)
{
int start=16,cif;     

YYY=16;

while (nr2>0)
      {
      cif=nr2%10;
      vect[start]=cif;
      nr2=nr2/10;
      start--;       
      }
XXX=start+1;

}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

bool biggerthanA()
{
int i;
int l=YYY-XXX+1;
int start=XXX;
     
if (lengthA>l) return false;

if (lengthA<l) return true;

for (i=0;i<lengthA;i++)
    {
    if (intA[i]>vect[start]) return false;
    if (intA[i]<vect[start]) return true;
    start++;                    
    }
return true;

}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

bool smallerthanB()
{
int i;
int l=YYY-XXX+1;
int start=XXX;
     
if (lengthB<l) return false;

if (lengthB>l) return true;

for (i=0;i<lengthB;i++)
    {
    if (intB[i]<vect[start]) return false;
    if (intB[i]>vect[start]) return true;
    start++;                    
    }
return true;

}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------


void multiply(int l)
{
int m[10][10],i,j,t[11],car=0,x,y,sumind,suma,poz,numar,cif;

for (i=0;i<l;i++)
    {
    for (j=0;j<l;j++)
        {
        m[i][j]=s[i]*s[j];               
        }             
    }


for (x=1;x<=l;x++) //l sume pana la jumate inclusiv 
    {
    sumind=(l-1)*2-x+1;
    suma=0;
    for (y=(l-x);y<=(l-1);y++) //x elemente de adunat
        {
        suma+= m[y][sumind-y];                                
        }

    vect[l*2-x]=suma;    
    }
  
    

    
for (x=1;x<=(l-1);x++) //l-1 sume in continuare 
    {
    sumind=l-x;
    suma=0;
    for (y=(l-x-1);y>=0;y--) //x elemente de adunat
        {
        suma+= m[y][sumind-y-1];                                
        }

    vect[l-x]=suma;    
    
//    printf("\n\n check: %d \n\n",suma);
    }    


    
    
/*    
printf("\n\n produsul ");

for (i=0;i<(2*l);i++)
    printf("%d ",vect[i]);

 printf("\n\n ");   
*/




for (i=(l*2-1);i>=0;i--)
    {
    if (vect[i]>9)
        {
        numar=vect[i];
        vect[i]=0;
        poz=i;
            
        while (numar>0)
              {
              cif=numar%10;
              vect[poz]=vect[poz]+cif;
              poz--;
              numar=numar/10;       
              }                    
        }
    }

/*
printf("\n\n produsul ");

for (i=0;i<(2*l);i++)
    printf("%d ",vect[i]);

printf("\n\n ");   
*/






/*    
for (i=0;i<l;i++)
    {
    for (j=0;j<l;j++)
        {
        printf("%d\t",m[i][j]);              
        } 
    printf("\n\n");            
    }
*/


}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void write_p(int nr, int parity, int l)
{
int poz,cif,i;

 

if (parity==0)     
   {
   poz=l-1;
   while (nr>0)
         {
         cif=nr%10;
         s[poz]=cif;
         s[2*l-1-poz]=cif;      
         nr=nr/10;
         poz--;
         }    
/*
   printf("\n\n palindromul : ");
   
   for (i=0;i<(l*2);i++)
      {
      printf("%d",s[i]);
      }
 */  

 
 
 }
 
 
 
   
if (parity==1)     
   {
   poz=l-1;
   while (nr>0)
         {
         cif=nr%10;
         s[poz]=cif;
         s[(l-1)*2-poz]=cif;      
         nr=nr/10;
         poz--;
         }    
 /*
 printf("\n\n palindromul : ");
   
  for (i=0;i<(l*2-1);i++)
       {
       printf("%d",s[i]);
       }
*/      
       
   }
   
return;
}




//------------------------------------------------------------------------------
//------------------------------------------------------------------------------



bool pal(int l)
{
int i, poz ,length, x,y;
bool flag=true;


for (i=0;i<l;i++) 
     {
     if (vect[i]!=0) 
        {
        poz=1;
        break;                        
        }     
     }

x=poz;
y=l-1;

XXX=x;
YYY=y;
     
while(x<y)
          {
          if (vect[x]!=vect[y]) 
             {
             flag=false;
             break;
          
             
             }
          x++;
          y--;    
          }
/*
if (flag==true)
   {
   for (i=poz;i<l;i++)
       printf("%d",vect[i]);            
   }
*/
return flag;

}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------


bool pal_1(int a)
{
    int cif,length=0,s[10],i,x,y;
    
    bool flag=true; 
    
    while (a>0)
          {
          cif=a%10;
          a=a/10;
          s[length]=cif;
          length++;
          }
    

    x=0;
    y=length-1;
    
    while (x<y)
    {
    if (s[x]!=s[y]) 
        {
        flag=false;
        break;
       
        }    

    x++;
    y--;
    }

return flag;

}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
