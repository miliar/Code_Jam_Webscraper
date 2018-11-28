#include<stdio.h>
#include<conio.h>
int n=0;long int multiply=1;
int a[10]={0,0,0,0,0,0,0,0,0,0};
void check(long int number,long int);
void mark(int x);
int filled();
void clear();
int main()
{ long int t; long int ele[1000000];
  scanf("%ld",&t);
  for(int i=0;i<t;i++)
  { scanf("%ld",&ele[i]);
  }
  
  for(int k=0;k<t;k++)
  {       if(ele[k]==0){printf("case #%d: INSOMNIA\n",k+1); continue;}
          else{
          printf("case #%d:",k+1);check(ele[k],ele[k]);printf("\n");
                    clear();
          }
          }
  getch();
  
}
void mark(int y)
{ a[y]=1;
 }
int filled()
{   int flag=0;
    for(int q=0;q<10;q++){ if(a[q]==0){flag=1; break;}}
    if(flag==1) return 0; else return 1;
}
void check(long int number,long int res)
{ 
   while(number!=0)
   { mark(number%10);
     number/=10;
   }
   
  
   if(!filled()){check((++multiply)*res,res);}
  
   else{printf(" %d",(multiply*res)); multiply=1;}
   
   
   
}
void clear(){for(int i=0;i<10;i++) 
              a[i]=0;
              }
