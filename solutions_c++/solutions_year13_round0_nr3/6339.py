/*
BHARATHKUMAR
13-4-13
C++
*/
#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;

class B
{
	long long int a,b;
public: 
void process()
{
	int result=0;
	cin>>a>>b;
	for(int i=a;i<=b;i++)
		if(palindrome(i) && persqr(i))
			result++;
	cout<<result<<endl;

}

int palindrome(int x)
{
	int rev=0,dig;
	int temp=x;
	while(x)
	{
		dig=x%10;
		rev=rev*10+dig;
		x/=10;
	}
	if(rev==temp)
		return 1;
	return 0;
}

int persqr(int x)
{
	float a;
	int b;
	a=sqrt(x);
	b=sqrt(x);
	if(float(b)==a && palindrome(b))
		return 1;
	else
		return 0;
}
};

int main()
{
int T;
B b;
cin>>T;
for(int i=0;i<T;i++)
{
cout<<"Case #"<<i+1<<": ";
b.process();
}
}
