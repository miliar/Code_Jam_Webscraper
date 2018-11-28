#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;

FILE *fin =fopen("txt.txt","r");
FILE *fin2 =fopen("AAA.out","w");

int prl(int i)
{
	int n=0;
	char ch[101];
	vector<bool>f(101);

	fscanf(fin,"%s",&ch[0]);

	while(ch[n]=='-' || ch[n]=='+' )
	{
		f[n]=(ch[n]=='-')?false:true;
		n++;
	}

	n--;

	while(n>=0 && f[n])
	{
		n--;
	}

	int k=0;
	
	while(n>=0)
	{
		k++;

		if(f[0])
		{
			int i=0;
			while(f[i])
			{
				f[i++]=false;
			}
		}
		else
		{
			bool temp;
			int p = n>>1;
			for(int i=0;i<=p;i++)
			{
				temp=!f[i];
				f[i]=!f[n-i];
				f[n-i]=temp;
			}
			
			while(n>=0 && f[n])
			{
				n--;
			}
		}
	}

	fprintf(fin2,"Case #%d: %d\n",i,k);
	
	return 0;
}

int main()
{
	int n=0,m=0,k=0;

	fscanf(fin,"%d",&n);

	int i=1;

	while(n-->0)
	{
		prl(i++);
	}

    return 0;
}