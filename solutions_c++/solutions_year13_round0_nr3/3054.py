#include<iostream>
#include<math.h>

#define FOR(i,n) for(i=0;i<n;i++)
using namespace std;

int i,j,t,a,b,temp=1,root;

int square(int x)
{
	double rt;
	rt=sqrt(x);
	if(rt==int(rt))
		return 1;
	return 0;
}

int palindrome(int x)
{
	int i,reverse=0,temp=10,xx=x;
	do
	{
		reverse = reverse*10 + x%10;
		x/=10;
	} while(x!=0);
	if(reverse==xx)
		return 1;
	return 0;
}

int main()
{
	cin>>t;
	int count=0;
	while(t--)
	{
		count=0;
		cin>>a>>b;
		for(i=a;i<=b;i++)
		{
			if(square(i)&&palindrome(i)&&palindrome(int(sqrt(i))))
				count++;
		}
		cout<<"Case #"<<temp++<<": "<<count;
		if(t!=0)
			cout<<endl;
	}
	return 0;
}
