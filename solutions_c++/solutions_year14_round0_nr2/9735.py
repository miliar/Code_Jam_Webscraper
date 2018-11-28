#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{	int test_cases;
    double cost,inc,target;
	double dd,A,B,go;
    cin>>test_cases;
	for(int i=1;i<=test_cases;i++)
	{	cin>>cost>>inc>>target;
		dd =2.0;
		A= target/2.0;
		go = cost/dd;
		dd=dd+inc;
		B= go+target/dd;
		for(;A>B;)
		{
			A=B;
			go +=cost/dd;
			dd=dd+inc;
			B = go+target/dd;
		}
		printf("Case #%d: %.7f\n",i,A);	
	}	
}
