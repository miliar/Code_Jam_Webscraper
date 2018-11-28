#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
int er[20];
void to_er(int d)
{
	for(int i=0;i<16;i++)
	{
		er[i]=d%2;
		d/=2;
	}
}
int divi[20];
long long jj[20];
int to_jinzhi(int th)
{
	long long sum=0;
	for(int i=15;i>=0;i--)
	{
		sum=sum*th+er[i];
	}
	jj[th]=sum;
	for(int j=2;j<10;j++)
	{
		if(sum%j==0)
		{
			divi[th]=j;
			return 1;
		}
	}
	return 0;
}
int main()
{//for small
	int T;
//	scanf("%d",&T);
	int s=0;
	freopen("c-small.out","w",stdout);
	int d=(1<<15);
	d++;
	printf("Case #1:\n");
	while(s<50)
	{
		
		to_er(d);
		int t=0;
		for(int i=2;i<=10;i++)
		t+=to_jinzhi(i);
		if(t==9){
			for(int i=15;i>=0;i--)printf("%d",er[i]);
			printf(" ");
			for(int i=2;i<=10;i++){
				printf("%d",divi[i]);
		//		printf(" %lld||",jj[i]);
				if(i==10)printf("\n");
				else printf(" ");
			}
			s++;
		}
		d+=2;
	}
}