#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
   //char a[4][5];
   int t,i,j,k,f=0,s;
   //scanf("%d",&t);
   cin>>t;
   for(k=1;k<=t;k++)
   {
	f=0;
    cin>>i>>j;
	if(i<=1&&j>=1)
	f++;
	if(i<=4&&j>=4)
	f++;
	if(i<=9&&j>=9)
	f++;
	if(i<=121&&j>=121)
	f++;
	if(i<=484&&j>=484)
	f++;
	printf("Case #%d: %d\n",k,f);  
}


return 0;
}
