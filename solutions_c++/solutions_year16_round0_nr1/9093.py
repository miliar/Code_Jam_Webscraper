#include <bits/stdc++.h>
using namespace std;

long long n, n2,t2,k;
int main()
{
	long long t,l[10],count=0,in;
	bool flag;
	ifstream filei;
	filei.open("A-large.in");
	ofstream fileo;
	fileo.open("lsheepout.txt");
	filei>>t;
	for(int i=1; i<=t ; i++)
	{
		flag=0;
		filei>>n;
		for(int j=0;j<10;j++)
		{
			l[j] = 0;
		}
		k=1;
		count = 0;
		while(count<=9)
		{
			if( (k*n) == (k+1)*n )
			{
				flag= 1;
				break;
			}
			n2 = n*k;
			//cout<<"n2 = "<<n2<<endl;
			for(t2=n2; t2!=0; t2=t2/10)
			{
				in = t2 % 10;
				//cout<<"index== "<<in<<endl;
				l[in] = 1;
			}
			count = 0;
			for(int j=0;j<10 ; j++)
			{
				//cout<<"count== "<<count<<"\t";
				count = count + l[j];
			}
			//cout<<"count== "<<count<<endl;
			k++;
		}
		if(flag==1)
		{
			fileo<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else
		{
			fileo<<"Case #"<<i<<": "<<n2<<endl;
		}
	}
	filei.close();
	fileo.close();
	return 0;
}