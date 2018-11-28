#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int T;
unsigned long long r,t,x,y,count;
cin>>T;
int it=0;
while(T--)
{
	scanf("%llu %llu\n",&r,&t);
	count=0;
	while(1)
	{	if(t>=2*r+1)
			t-=2*r+1;
		else
			break;
		count++;
		r+=2;
	}
	it++;
	printf("Case #%d: %llu\n",it,count);
}
}