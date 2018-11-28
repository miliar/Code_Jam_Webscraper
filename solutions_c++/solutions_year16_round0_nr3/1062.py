#include<iostream>
using namespace std;
#define ull unsigned long long
#define al 10000001
ull arr[al];
void pre()
{
	for(ull i=2;i<al;i++)
	{
		if(!arr[i])
		{
			for(ull j=i*2;j<al;j+=i)
			arr[j]=i;
		}
	}
}
ull isprime(ull x)
{
	if(x<al)
	{
		return arr[x];
	}
	for(ull j=3;j*j<=x;j+=2)
	{
		if(x%j==0)
		return j;
	}
	return 0;
}
void disp_bin(ull x)
{
	if(x)
	{
		disp_bin(x/2);
		cout<<x%2;
	}
}
int sol(ull x)
{
	int arr[10];
	for(int i=2;i<=10;i++)
	{
		ull bx=0;
		ull mul=1;
		ull temp=x;
		while(temp)
		{
			bx+=(temp%2)*mul;
			temp/=2;
			mul*=i;
		}
//		cout<<"i"<<i<<" "<<bx<<endl;
		arr[i-1]=isprime(bx);
	//	cout<<"got "<<x<<" "<<bx<<" "<<arr[i-1]<<endl;
		if(arr[i-1]==0)
		{
			return -1;
		}
	}
	disp_bin(x);
	for(int i=2;i<=10;i++)
		cout<<" "<<arr[i-1];
	cout<<endl;
}
int main()
{
	int test;
	cin>>test;
	cout<<"Case #1:"<<endl;
		pre();
		ull n,j;
		cin>>n>>j;
		ull start=(((ull)1)<<(n-1));
		while(j)
		{
			if(start%2==0)
			{
				start++;
				continue;
			}
//			disp_bin(start);cout<<endl;
			if(sol(start)!=-1)
			j--;
			start++;
			
		}
	return 0;
}
