#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;


bool palindrome(long long int a)
{
long long int r=0;
 long long int n = a;
 long long int d;
 while (a > 0)
 {
      d = a % 10;
      r= r * 10 + d;
      a = a / 10;
 }	
	return n==r;
}
int main()
{
int test;
cin>>test;
for(int testno=1;testno<=test;testno++)
{
	cout<<"Case #"<<testno<<": ";
	long long int a;
	long long int b;
	cin>>a>>b;
	long long int as=sqrt(a);
	long long int bs=sqrt(b);
	if(as*as!=a)
	as++;
	
	int c=0;
	for(int i=as;i<=bs;i++)
	if(palindrome(i) && palindrome(i*i))
	c++;
	cout<<c<<endl;
}	
	
	
}
