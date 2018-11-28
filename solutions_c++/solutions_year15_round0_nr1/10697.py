#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main(void)
{
	int t=0,smax,sum=0,cases=0,count[100]={0};
	cin>>t;
	
	while(t--)// 5 110003
	{
		cin>>smax;
		char s[1000];
		gets(s);
		
		sum=0;
		for(int i=1;i<=strlen(s);i++)
		{
				if(sum<i)
				{
					sum++;
					count[cases]++;
				}
				sum+=(int)(s[i]-'0');
		}
		cases++;
	}
	for(int i=0;i<cases;i++)
	cout<<"Case #"<<i+1<<": "<<--count[i]<<endl;
}
		
