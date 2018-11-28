#include<stdio.h>
#include<iostream>
#include<math.h>
#include<conio.h>
using namespace std;

long long check(long long n)
{	
	long long rem,rev=0,temp=n;
	while(temp)
	{
		rem=temp%10;
		rev = rev * 10 + rem;
		temp = temp/10;

	}
	if(rev==n)
		return 1;
	else
		return 0;
}
int main()
{
	long long n,a,b,count,c=1,i,temp;
	cin >> n;
	while(n--)
	{
		count=0;
		cin>>a>>b;
		for(i=a;i<=b;i++)
		{
			if(check(i))
			{
			temp=sqrtl(i);
			if(temp*temp==i)
				if(check(temp))
					count++;
			}
		}
		cout<<"Case #"<<c++<<": "<<count<<endl;
		
	}
	return 0 ;
	
}