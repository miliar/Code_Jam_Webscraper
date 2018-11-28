#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;

	FILE *fin2 =fopen("AAA.out","w");

int prl(unsigned long long  a,int i)
{
	if(a==0)
	{
		fprintf(fin2,"Case #%d: INSOMNIA\n",i);
		return 0;
	}

	vector<bool>f(10,false);

	int y;
	int j=1, k=0;
	while(k!=10)
	{
		unsigned long long r= a*j;

		while(r!=0)
		{
			y=r%10;
			if(!f[y])
			{
				f[y]=true;
				k++;
			}
			r/=10;
		}
		j++;
	}
	
	j--;

	fprintf(fin2,"Case #%d: %Ld\n",i,j*a);
	
	return 0;
}

int main()
{
	int n=0,m=0,k=0;
	FILE *fin =fopen("txt.txt","r");

	fscanf(fin,"%d",&n);

	unsigned long long  a=0;
	int i=1;

	while(n-->0)
	{
		fscanf(fin,"%Ld",&a);
		prl(a,i++);
	}

    return 0;
}