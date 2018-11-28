#include <iostream>
#include<cstdio>
using namespace std;
int main()
{
    int a;
    cin>>a;
    for(int k=1;k<=a;k++)
    {
    	float c,f,x,t=0,t1,t2,h,d=2;
    	scanf("%f%f%f",&c,&f,&x);
    	
    	do
		{
    		t1=x/d;
			h=c/d;
			t2=h+x/(d+f);
			d=d+f;
			if(t2>=t1)
				t=t+t1;
			else
				t=t+h;
			//printf("t1: %.07f t2: %.07f t: %.07f h: %.07f \n ",t1,t2,t,h);
    	}while(t2<t1);
    	
    	printf("Case #%d: %.07f\n",k,t);
	}
}


