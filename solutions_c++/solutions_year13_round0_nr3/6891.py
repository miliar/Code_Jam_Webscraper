#include<stdio.h>
#include<conio.h>
#include<math.h>

int palindrome(int);

void main()
{
 FILE *fpw,*fpr;
 int count,k,i,num=100,a=1,b=1,x,y;
 double root;
 clrscr();

 fpr=fopen("d:\\input.txt","r");
 fpw=fopen("d:\\output.txt","w");
 for(i=1;i<=num;i++)
 {
  count=0;
  a=getw(fpr);
  b=getw(fpr);
  for(k=a;k<=b;k++)
  {
   x=palindrome(k);
   root=sqrt(k);
   if(root==int(root))
   y=palindrome(root);
    else
    y=0;
   if(x==1 && y==1)
   count++;
  }

  fprintf(fpw,"Case #%d: %d\n",i,count);
  fprintf(fpw,"\n");
 }
 getch();
}

int palindrome(int n)
{
 int t,s=0,num;
 num=n;
 while(n>0)
 {
  t=n%10;
  s=(s*10)+t;
  n=n/10;
 }

 if(num==s)
 return 1;
  else
  return 0;
 }