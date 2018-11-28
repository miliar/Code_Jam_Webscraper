#include<stdio.h>
#include<stdlib.h>
int compare(const void *a,const void *b)
{
    return (*(int *)a - *(int *)b);
}
int main()
{
    int i,j,k,n,max,ans,t,d=0,c,r,x,p;
    k=1;
    scanf("%d",&t);
    while(t--)
    {
              scanf("%d %d %d",&x,&r,&c);
              
              if((r*c)%x !=0)
              p=0;
              else
              {
              	if(x<=2)
              p=1;
              else if(x==3)
              {
                   if((r*c) ==3)
                   p=0;
                   else
                   p=1;
              }
              else if(x==4)
              {
                   if((r*c)== 4 || (r*c)==8)
                   p=0;
                   else if((r*c)==12 || (r*c)==16)
                   p=1;
              }
              }
              
              if(p==0)
              printf("Case #%d: RICHARD\n",k);
              else if(p==1)
              printf("Case #%d: GABRIEL\n",k);
              k++;
              
              }
              
              return 0;
}
