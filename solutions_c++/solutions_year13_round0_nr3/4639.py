// Fair_and_Square.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <math.h>
#include "stdio.h"
using namespace std;

__int64 make(int a,int t)
{
	__int64 result=a;
	int b=0;
	int tmp=1;

	while(a)
	{
		b*=10;
		b+=a%10;
		a/=10;
		result*=10;
		tmp*=10;
	}
	if (t<0)
	{
		result+=b;
	}
	else
	{
		result=result*10+tmp*t+b;
	}
	
	return result;

}
int valid(__int64 input)
{
	__int64 rvs=0,tmp=input;

	while(input)
	{
		rvs*=10;
		rvs+=input%10;
		input/=10;
	}
	if (tmp==rvs)
	{
		return 1;
	}
	else
		return 0;
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* input;
	
	fstream outfile;
	input=fopen("c:\\C-large-1.in","r");
	outfile.open("c:\\C-large-out.txt",ios::out|ios::trunc );
	int T;
	fscanf(input,"%d",&T);

	for (int t=0;t<T;t++)
	{
		__int64 A,B;
		fscanf(input,"%I64d",&A);
		fscanf(input,"%I64d",&B);
		long double a=A;
		long double b=B;
		int c=sqrtl(a);
		int d=sqrtl(b);
		__int64 tmp=c;
		if (tmp*tmp<A)
		{
			c++;
		}
		tmp=d+1;
		if (tmp*tmp<=B)
		{
			d++;
		}

		tmp=c;
		int count=0;
		while(tmp)
		{
			tmp/=10;
			count++;
		}

		tmp=c;
		
		for (int i=0;i<(count+1)/2;i++)
		{
			tmp/=10;		
		}
		count=0;
		__int64 init=tmp;
		__int64 hc= make(tmp,-1);

		for (;(hc=make(tmp,-1))<=d;tmp++)
		{
			if (hc*hc>=A&&valid(hc*hc))
			{
				count++;
			}
		}

		tmp=init;
		int t1=0;

		for (;true;tmp++)
		{
			int flag=0;
			for (t1=0;t1<10;t1++)
			{
				hc=make(tmp,t1);
				if (hc>d)
				{
					flag=1;
					break;
				}
				if (hc*hc>=A&&valid(hc*hc))
				{
					count++;
				}
			}
			if (flag==1)
			{
				break;
			}
		}



		outfile<<"Case #"<<t+1<<": ";
		outfile<<count;
		cout<<count<<endl;

		outfile<<endl;



	}



	fclose(input);
	outfile.close();
	return 0;
}

