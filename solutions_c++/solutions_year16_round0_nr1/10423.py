#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	long long int n,m,n1,i,j,flag,b,a[15],c,t;
	ifstream ifile;
	ofstream ofile;
	ifile.open("A-large.in");
	ofile.open("output.txt");
	ifile>>t;
	
	for(j=1;j<=t;j++)
	{	
		ifile>>n;
		for(i=0;i<10;i++)
		{
			a[i]=0;
		}
		if(n==0)
		{
			ofile<<"Case #"<<j<<": INSOMNIA\n";
		}
		else
		{
			flag=0;c=0;n1=n;
			while(flag==0)
			{
				m=n;
				while(n>0)
				{
					b=n%10;
					if(a[b]==0)
					{
						c++;
						a[b]=1;
					}
					n=n/10;
				}
				if(c==10)
				{
					flag=1;
				}
				n=m+n1;
			}
			//cout<<"CASE #"<<j<<": "<<m<<"\n";
			ofile<<"Case #"<<j<<": "<<m<<"\n";
		}
	}
	ifile.close();
	ofile.close();	
}
