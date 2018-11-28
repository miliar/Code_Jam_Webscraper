#include <iostream>
using namespace std;
#include<stdio.h>
int index=1;
int main()
{
int tcase,r;
long long n;
scanf("%d",&tcase);
while(tcase--)
{ int count=0,flag=0;
long long temp;
int look[10]={0};
scanf("%lld",&n);
for(int i=1;i<1000000;i++)
{	
	temp=i*n;
	while(temp)
	{
		r=temp%10;
		if(look[r]==0)
		{
			count++;
			look[r]=1;
			if(count==10)
			   {  flag=1;	  
			   	  printf("Case #%d: %lld\n",index++,i*n);
			      break;
			   }
	    }
	    temp=temp/10;
	}
	if(flag==1)
	break;
}
if(flag==0)
printf("Case #%d: INSOMNIA\n",index++);
}
	


}

