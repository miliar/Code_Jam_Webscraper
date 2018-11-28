#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<queue>
#include<cmath>
using namespace std;
bool isPalindrome(long long n)
{
	int a[16];
	int i=0;
	while(n>0)
	{
		a[++i]=n%10;
	    n/=10;
	}
	for(int j=1;j<=i/2;j++)
	{
		if(a[j]!=a[i-j+1]) return false;
	}
	return true;
}

long long solveGame()
{
	long long a, b, br=0;
	cin>>a>>b;

	long long x=ceil(sqrt(a));
	for(long long i=ceil(sqrt(a));i<=floor(sqrt(b));i++)
	{
		if(isPalindrome(i)&& isPalindrome(i*i))  br++;
	}
	return br;
}
int main()
{
    long long n;
   cin>>n;
  for(int i=1;i<=n;i++)
    {
      cout<<"Case #"<<i<<": "<<solveGame()<<endl;
    }

return 0;
}

