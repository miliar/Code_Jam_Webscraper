#include <stdio.h>
#include <conio.h>
#include <math.h>

int main()
{
freopen("C-small-attempt1.in","r",stdin);
freopen("Res.in","w",stdout);
float c;
int g,f,una=0,e,j,d,i,a,b,t,s=1;
scanf("%d",&t);
for(j=0;j<t;j++)
{
una=0;
scanf("%d %d",&a,&b);
//printf("%d %d",a,b);}
for(i=a;i<=b;i++)
{
c=floor(sqrt(i));
if((fmod(sqrt(i),c))==0)
{
e=i;
d=0;
      while(e>0)
      {
             d=(d*10)+(e%10);
             e=e/10;   
      }            
      //printf("%d \n",i);
      g=sqrt(i);
      f=0;
      while(g>0)
      {
          f=(f*10)+fmod(g,10);
          g=g/10;      
      }
      //printf("%d \n",f);
      if((d==i)&&(f==(sqrt(i))))
      una++;     
}              
}
printf("Case #%d: %d \n",s,una);
s++;
}
getch();
return 0;    
}
