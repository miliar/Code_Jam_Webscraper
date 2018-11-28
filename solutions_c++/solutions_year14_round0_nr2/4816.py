#include<iostream>
#include<fstream.h>
#include <iomanip.h>
#include<stdlib.h>

int main()
{
	int n,N,i,j;
	long double C,F,X,T,sum,temp;
	ifstream fin("B-small-attempt1.in",ios::in);
	FILE* fp=fopen("o8.txt","w");
	fin>>N;
	for(n=0;n<N;n++)
	{
		fin>>C;
		
		fin>>F;
		
		fin>>X;
		
		temp=(double)(X/2.0);
		for(i=0;i<X;i++)
		{
			sum=0;
			for(j=0;j<i;j++)
			{
				sum+=(double)(1/(2+j*F));
			}
			T=C*sum+(double)(X/(2+j*F));
			if(temp>T)
			{     
				temp=T;
			}
		}
		fprintf(fp,"Case #%d: %.8f\n",n+1,temp);//<<": "<<setprecision(12)<<temp<<"\n";
	}
	return 0;

}