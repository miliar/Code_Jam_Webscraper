#include<stdio.h>
void input()
{
	int i,j,bit;
	long a,b,k,d=0;
 scanf("%ld",&a);
 scanf("%ld",&b);
 scanf("%ld",&k);
 for(i=0;i<a;i++)
 {
 	 for(j=0;j<b;j++)
 	 {
 	 	bit=i&j; 
 	 	if(bit<k)
 	 	d++;
 	 }
 }
 printf("%ld\n",d);

}
int main()
{
 int t,x=0;
 scanf("%d",&t);
 while(t--)
 {
  printf("Case #%d: ",++x);
  input();
  }
 return 0;
 }



