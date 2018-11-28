#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;
int square(int n)
{
	double g=n;
	float x=sqrt(g);
	int c=x;
	if(c*c==n)return 1;
	return 0;
}
int pallin(int n)
{
     int num, digit, rev = 0;
    num=n;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
     if (n == rev)
       return 1;
    return 0;  
}
int main()
{
	freopen("test.txt","w",stdout);
	int t;
	cin>>t;
	int i,j,k,a,b;
	for(i=1;i<=t;i++)
	{
		int count=0;
		cin>>a>>b;
		for(j=a;j<=b;j++)
		if(square(j))if(pallin(j))if(pallin(sqrt(j))){count++;}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}
