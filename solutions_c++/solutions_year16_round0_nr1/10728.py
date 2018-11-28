#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream in("A-large.in");
	ofstream out("output_large.txt");
	int t,a[10];
	long long int f=1;
	in>>t;
	int u=1;
	long long int n,n1,l;
	while(t--)
	{
		long long int i=2;
		
		in>>n;
		if(n==0)
		{
			out<<"Case #"<<u<<": INSOMNIA"<<endl;
			u+=1;
			continue;
		}
		for(int i=0;i<10;i++)
			a[i]=0;
		n1=n; l=n;
		f=1;
		while(f)
		{
			while(n1)
			{
				int x=n1%10;
				a[x]=1;
				n1=n1/10;
			}
		
			for(int j=0;j<10;j++)
			{
				if(a[j])
					f=0;
				else 
				{
					f=1;
					break;
				}
			}
			if(f)
			{
				n1=n*(i++);
				l=n1;
				continue;
			}
			else
			{
				out<<"Case #"<<u<<": "<<l<<endl;
			}
		}
		u+=1;
	}
}
