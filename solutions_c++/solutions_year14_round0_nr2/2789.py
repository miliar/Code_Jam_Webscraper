#include<iostream>
#include<limits.h>
#include<cstdio>
using namespace std;
int main()
{
	int test,i;
	cin>>test;
	for( i=1;i<=test;i++ ){
		double c,f,x,a,b,time,flag,count;
		cin>>c>>f>>x;
		time = 2;
		count = x/time;
		flag = 0;
		while(1){
			flag+= c/time;
			time=time+f;
			a= x/time;
			if(count>flag+a)
			count = flag+a;
			else
			break;
		}
		printf("Case #%d: %0.7lf\n",i,count);
	}
	return 0;
}
