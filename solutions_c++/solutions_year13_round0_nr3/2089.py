#include<stdio.h>
#include<iostream>
using namespace std;
bool panlindrome(long long n);
long long ans(long long a,long long b);

int main()
{
	int cas;
	long long a,b;
	scanf("%d",&cas);
	for(int q = 1 ;q<=cas ; q++)
	{
		cin>>a>>b;
		cout<<"Case #"<<q<<": "<<ans(a,b)<<endl;
	}
	return 0;
}
long long ans(long long a,long long b)
{
	long long cnt = 0;
	long long s = 1;
	while(s*s < a)s++;
	while(s*s <= b){if( panlindrome(s) && panlindrome(s*s)) cnt++;s++;}
	return cnt;
}
bool panlindrome(long long n)
{
	long long a= 0,b = n;
	while(n){a = a*10 + n%10; n/=10;}
	return a== b;
}
