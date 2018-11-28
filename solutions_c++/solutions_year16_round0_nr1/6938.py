#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
	ofstream out("outputA_large_1.txt");
	ifstream in("A-large.in");
	int t;
	in>>t;
	int m=t;
	while(t--)
	{
		long long int n,j=2;
		in>>n;
		if(!n)
		{
			out<<"Case #"<<m-t<<": INSOMNIA"<<"\n";
			continue;
		}
		int a[10]={0};
		long long int k=n,l=n;
		long long int f=1;
		while(f)
		{
			while(k)
		{
			int d=k%10;
			a[d]=1;
			k/=10;
		}
		for(int i=0;i<10;i++)
		{
			if(a[i])
			{
				f=0;
			}
			else
			{
				f=1;
				break;
			}
		}
		if(f)
		{
			k=n*(j++);
			l=k;
			continue;
		}
		else
		{
			out<<"Case #"<<m-t<<": "<<l<<"\n";
		}
		}
	}
}
