#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int i,n;
  	long long int r1,r2,r3,p,count;
  	scanf("%d",&n);
  	for(i=0;i<n;i++)
    {
      	count=0;
      	scanf("%lld%lld",&r1,&p);
      	r2=r1+1;
      	r3=(r2*r2)-(r1*r1);
      	p=p-r3;
      	if(p>=0)
          count++;
      	while(p>0)
        {
          r1=r2+1;
          r2=r1+1;
          r3=(r2*r2)-(r1*r1);
          p=p-r3;
          if(p>=0)
            count=count+1;
      	}
      	printf("Case #%d: %lld\n",i+1,count);
    }  
}
   