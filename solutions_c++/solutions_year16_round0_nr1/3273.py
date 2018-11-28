#include<iostream>
using namespace std;
long long digits;
void fill(long long number)
{
	while(number>0)
	{
		digits|=(1<<(number%10));
		number/=10;
	}
}
long long solve(long long n)
{
	long long mem=n;
	digits=0;
	while(digits<1023)
	{
		fill(n);
		n+=mem;
	}
	return n-mem;
}
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	long long t,n;
	cin>>t;
	for(long long i=0;i<t;i++)
	{
		cin>>n;
		cout<<"Case #"<<i+1<<": ";
		if(n!=0)
		{
			cout<<solve(n);
		}
		else
		{
			cout<<"INSOMNIA";
		}
		cout<<"\n";
	}
	return 0;
}
