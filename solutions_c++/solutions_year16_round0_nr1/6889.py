#include <iostream>
#include <string.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

using namespace std;

int check(char qwerty[10])
	{
		
		int x;
		for(x=0;x<10;x++)
			{
				if(qwerty[x]!=x+65)
					return 0;
			}
		return 1;		
	}
int main()
{
	unsigned long long int n,n2,caseno;
	int i,j,t,flag, digit;
	char need[10];
	cin>>t;
	cin.get();
	for (i=1;i<=t;i++)//test case loop n times
	{
		cin>>n;
		cin.get();
		for(j=1;j<5000;j++)
			{
				caseno=j*n;
				n2=j*n;
				while(n2>0)
					{
						digit=n2%10;
						need[digit]=digit+65;
						n2/=10;
					}
				flag=check(need);
				if (flag)
					break;
			}
		if (flag)
			cout<<"Case #"<<i<<": "<<caseno<<endl;
		else
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		
		for (j=0;j<10;j++)
			need[j]='s';
	}
}