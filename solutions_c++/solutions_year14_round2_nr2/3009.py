// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <tchar.h>
#include <SDKDDKVer.h>
#include <iostream>
#include <conio.h>
#include <cstdio>
#include <math.h>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <algorithm>


using namespace std;

void main() {
	
freopen("C:\\Users\\veer\\Desktop\\B-small-attempt1.in" , "r" , stdin);
freopen("C:\\Users\\veer\\Desktop\\B-small-attemp1-output.in" , "w" , stdout);
long long int T,A,B,K;
cin>>T;

for (long int c=0;c<T;c++)
{
	cin>>A>>B>>K;
	long int ct=0;

	for(long int il=0;il<A;il++)
	{
		for(long int jl=0;jl<B;jl++)
		{

long long int dec,dec2,rem,rem2,i=1,i2=1,sum=0,sum2=0;

    dec=il;
    do
    {
        rem=dec%2;
        sum=sum + (i*rem);
        dec=dec/2;
        i=i*10;
    }while(dec>0);
    ///cout<<"The binary of the given number is:"<<sum<<endl;

	/*cout<<"Enter the second decimal to be converted:";
    cin>>dec2;*/
	dec2=jl;
    do
    {
        rem2=dec2%2;
        sum2=sum2 + (i2*rem2);
        dec2=dec2/2;
        i2=i2*10;
    }while(dec2>0);
    //cout<<"The binary of the given number is:"<<sum2<<endl;

	long long int resrem1,resrem2,resrem,ressum=0,resi=1;
	while(sum>0&&sum2>0)
	{
		resrem1=sum%10;
		resrem2=sum2%10;
		resrem=resrem1&resrem2;
		ressum=ressum+(resi*resrem);
		sum=sum/10;
		sum2=sum2/10;
		resi=resi*10;
	}
	//cout<<"and"<<ressum;

	 long long int bin, decb = 0, remb, num, base = 1;
 
	 bin=ressum;
    num = ressum;
    while (num > 0)
    {
        remb = num % 10;
        decb = decb + remb * base;
        base = base * 2;
        num = num / 10;
    }
    //cout << "The decimal equivalent of " << bin << " : " << decb << endl;

	if(decb<K)
	{
		ct=ct+1;
	}
		}
	}
	cout<<"Case #"<<c+1<<": "<<ct<<endl;
}
getch();
}
