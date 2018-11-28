#include<iostream>
using namespace std;
int main()
{
int t,i,j,p;
double c,f,x,tt=0,k=0,l=0;
scanf("%d",&t);
p=t;
while(t--)
{
scanf(" %lf %lf %lf",&c,&f,&x);
tt=x/2.0;
k=0;
for(i=1;;i++)
{
k=k+c/(2+(f*(i-1)));
l=x/(2+(f*i));
if((k+l)<tt) 
{
tt=k+l;
}
else 
break;
}
printf("Case #%d: %lf \n",(p-t),tt);
}
return 0;
}

   
	
	


