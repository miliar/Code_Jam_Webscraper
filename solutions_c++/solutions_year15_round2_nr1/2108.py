#include<cstdio>
#include<climits>
#include<iostream>

using namespace std;

inline int Read()
{
	register int c=getchar();
	int x=0;
	for(;(c<48 || c>57);c=getchar());
	for(;c>47 && c<58;c=getchar())
		x=(x<<1)+(x<<3)+c-48;
	return x;
}

int rev(int n)
{
	int reverse=0,number=n;
	for(;number!= 0 ;)
	{
		reverse = reverse * 10;
		reverse = reverse + number%10;
		number = number/10;
	}
	return reverse;
}

int a[1000002];

int main()
{
	for(int i=0;i<1000002;i++)
		a[i]=INT_MAX;
	a[1]=1;
	for(int i=1;i<=1000000;i++)
	{
		a[i+1]=min(a[i+1],a[i]+1);
		int r=rev(i);
		a[r]=min(a[r],a[i]+1);
	}
	freopen("A-small-attempt1.in","r",stdin);
	freopen("1small.txt","w",stdout);
	int t=Read();
	for(int l=1;l<=t;l++)
	{
		int n=Read();
		printf("Case #%d: %d\n",l,a[n]);
	}
	return 0;
}
