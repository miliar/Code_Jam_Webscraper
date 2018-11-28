#include <stdio.h>
void check(int ,int);
int fl,flag,count;
main()
{
 int t,i=1;
 int num,den;
 char dumm;;
 scanf("%d",&t);
 for(;i<=t;i++)
 {
  count=0;
  fl=1;
  flag=0;
  scanf("%d",&num);
  scanf("%c",&dumm);
  scanf("%d",&den);
  //int ch=check(den);
  check(num,den);
  if(flag==0)
  printf("case #%d: %d\n",i,count);
  else
   printf("case #%d: Impossible\n",i);
  
}
}
void check(int num,int den)
{
 if(num!=den){
 int ch=1;
  if(num>den)ch=0;
  if(ch==1)
  {
           while(den > 1)
           {
                
                
                 if(num>=den)
                 {if(fl==1){fl=2;check(num-den,den);}}
                 
                 if(den%2==1)
                 {
                flag=1;break;
                 }
                 
                 den/=2;
                 if(fl==1)
                 count++;     
           }
           
           
  }             
  
 
 }         
}
