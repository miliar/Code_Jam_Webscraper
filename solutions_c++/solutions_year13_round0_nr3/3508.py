#include<iostream>
#include<stdio.h>
#include <math.h>
using namespace std;

bool IsPalindrome(int);
int count=0;
int main()
{
	FILE* fin = fopen("C-small-attempt0.in","r");
	FILE* fout = fopen("output.txt","w+");
	int number_of_cases=0;
	fscanf(fin,"%d",&number_of_cases);
	for(int ncase = 0; ncase<number_of_cases;ncase++)
	{
		int count=0;
		int min = 0;
		int max = 0;
		fscanf(fin,"%d",&min);
		fscanf(fin,"%d",&max);
		float rl = min;
		float rh = max;
		float lp = sqrt(rl);
		float hp = sqrt(rh);
		for(int i = ceil(lp);i<=floor(hp);i++)
		{
			if(IsPalindrome(i))
			{
				if(IsPalindrome(i*i))
				{
					count++;
				}
			}
		}
		fprintf(fout,"Case #%d: %d\n",ncase+1,count);
	}

	return 0;

}
bool IsPalindrome(int num)
{
	int digits=0;
	int pal=0;
	while(1)
	{
		if((int)(num/10)==0)
		{
			digits=1;
			break;
		}
		if((int)(num/100)==0)
		{
			digits=2;
			break;
		}
		if((int)(num/1000)==0)
		{
			digits=3;
			break;
		}
		digits=4;
		return false;
	}
	for(int i =1;i<digits+1;i++)
	{
		if(i==1)
			pal=pal+num%10;
		if(i==2)
			pal=pal*10+(int)((num%100)/10);
		if(i==3)
		{
			pal = pal*10+(int)((num%1000)/100);
		}

	}
	if(num == pal)
	{
		return true;
	}
	else
		return false;
}