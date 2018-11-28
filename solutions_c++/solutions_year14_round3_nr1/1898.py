#include<iostream>
using namespace std;
//#include<stdio.h>
int main()
{
int t,ti;
scanf("%d",&t);
for(ti=1;ti<=t;ti++)
   {
   int p,q,gen=0;
   scanf("%d/%d",&p,&q);
   //x=p/q;


   while(p<q)
	{
	gen++;
	p*=2;
	}
   while(q%2==0)
	 q/=2;
   if(p%q!=0)
      gen=41;
   printf("Case #%d: ",ti);
   if(gen>40)
     printf("impossible");
   else
     printf("%d",gen);
   printf("\n");
   }
return 0;
}