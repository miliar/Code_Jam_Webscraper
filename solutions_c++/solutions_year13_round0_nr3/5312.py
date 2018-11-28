#include<stdio.h>
#include<string>
#include<iostream>
#include<math.h>
#include<stdlib.h>


using namespace std;
FILE *fp1,*fp2;
inline bool isPrime(long i)
{
	int j,k;
	char c;
	string str;
	while(i!=0)
	{
		c=i%10+'0';
		i/=10;
		str+=c;
	}
	for(k=0,j=str.length()-1;k<str.length()/2;--j,++k)
	{
		if(str[k]!=str[j]) return false;
	}
	return true;
}

int main()
{
	int T,flag;
	fp1=fopen("A-large.in","r");
	fp2=fopen("A-large.out","w");
	fscanf(fp1,"%d",&T);
	for(flag=1;flag<=T;++flag)
	{
		int result=0;
		long A,B,a,b,i;
		fscanf(fp1,"%ld %ld",&A,&B);
		a = sqrt(A)+0.001;
		if(a*a<A) ++a;  
		b = sqrt(B)+0.001;
		for(i=a;i<=b;++i)
		{
			if(isPrime(i)&&isPrime(i*i)) ++result;
		}
		fprintf(fp2,"Case #%d: %d\n",flag,result);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}
