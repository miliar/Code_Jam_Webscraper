

#include "stdafx.h"
#include "string.h"
#include<iostream>
#include "fstream"
#include <math.h>
using namespace std;
int palindrom,square,T,j,nr,cfr;
int tn[100000000],tmpnum,i;
int  palindrome(int number)
{   cfr=0;
	tmpnum=floor(number);
		while(tmpnum>0)
		{tn[cfr]=tmpnum%10;
	
		tmpnum/=10;
		cfr=cfr+1;
		}

	if(number<10)
			palindrom=1;
		else
		{
			palindrom=1;
			for(j=0;j<(cfr/2);j++)
				if(tn[j]!=tn[cfr-j-1])
					palindrom=0;
		}
	return palindrom;
}
int _tmain(int argc, _TCHAR* argv[])
{
	fstream f("C-small-attempt0.in",ios::in);	
	fstream g("C-output.out",ios::out);


	long double a,b;
	f>>T;
	for(int t=1;t<=T;t++)
	{
	
	
	
	f>>a>>b;
	nr=0;
	
	for(i=floor(a);i<=b;i=i+1)
	{
		square=0;
		palindrom=0;
		cfr=0;
	
		if(((floor(sqrt(i))*floor(sqrt(i)))==i)&&((palindrome(sqrt(i))==1)))
			square=1;
		
		int pi=palindrome(i);
	int ps=palindrome(sqrt(i));
	;
		
	
		
		palindrom=palindrome(i);
		
		
		
		if((palindrom==1)&&(square==1))
	nr++;
	
	}
	g<<"Case #"<<t<<": "<<nr<<endl;
	}
	
	return 0;
}