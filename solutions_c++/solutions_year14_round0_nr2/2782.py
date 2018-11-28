#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;

int t;

double c,f,x;
	
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B2.txt", "w", stdout);
	scanf("%d", &t);
	int files;
	for(files=1; files<=t; files++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		
		double time=0;
		double now_p=2;
		
		while(true)
		{
			double time1 = x/now_p;
			double time2 = c/now_p + x/(now_p+f);
			if(time1>time2)
			{
				time += c/now_p;
				now_p+=f;
			}
			else
			{
				time+=x/now_p;
				break;
			}
		}
		
		printf("Case #%d: %.7lf\n", files, time);
	}
	//system("pause");
	return 0;
	
}