#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

char input[1005];

int ex(char a)
{
	if(a=='0') return 0;
	if(a=='1') return 1;
	if(a=='2') return 2;
	if(a=='3') return 3;
	if(a=='4') return 4;
	if(a=='5') return 5;
	if(a=='6') return 6;
	if(a=='7') return 7;
	if(a=='8') return 8;
	if(a=='9') return 9;
}

int main()
{
	int test,num;
	scanf("%d",&test);
	for(int a=1;a<=test;a++)
	{
		int ans=0,count;
		scanf("%d %s",&num,input);
		count=ex(input[0]);
		for(int b=1;b<=num;b++)
		{
			if(b>count) 
			{
				ans=ans+b-count;
				count=count+b-count+ex(input[b]);	
			}
			else count+=ex(input[b]);
		}
		printf("Case #%d: %d\n",a,ans);
	}
}
