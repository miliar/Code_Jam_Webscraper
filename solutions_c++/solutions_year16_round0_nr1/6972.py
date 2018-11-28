#include<iostream>
#include<fstream>
using namespace std;
int T;
int count,H[10];
void solve(long long sayi)
{
	long long temp = sayi;
	while(temp)
	{
		int bol = temp%10;
		temp/=10;
		if(H[bol]==0)
		{
			count++;
			H[bol]=1;
		}
		if(count==10)
		{
			cout<<sayi<<endl;
			return;
		}			
	}
}
int main()
{
	long long x;
	ifstream in("A-large.in");
	in>>T;
	for(int k=1;k<=T;k++)
	{
		in>>x;
		cout<<"Case #"<<k<<": ";
		if(x==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		count=0;
		for(int i=0;i<10;i++)H[i]=0;
		for(int i=1;;i++)
		{
			solve(x*i);
			if(count==10)break;
		}
	}
}
