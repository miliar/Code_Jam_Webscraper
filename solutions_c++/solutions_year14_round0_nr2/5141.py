#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int T;
	cin>>T;
	double C,F,X,c;
	int t=1;
	double cur,tym;
	while(t<=T)
	{
		cur = tym =0;
		cin>>C>>F>>X;
		c = 2;
		cur = C/c;
		while((cur+X/(c+F))<X/c)
		{
		    tym = tym + cur;
			c = c+F;
			cur = C/c;
			
		}
		tym = tym + X/c;
		printf("Case #%d: %lf\n",t,tym);
		t++;
		
	}
	return 0;
	
}
