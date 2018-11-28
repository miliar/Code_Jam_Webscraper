#include <iostream>
#include <fstream>
using namespace std;

main()
{
	long long int t,i,j,n,a[11],count,x,dig;
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("codejam_q1.out");
	in>>t;
	for(i=1;i<=t;i++)
	{
		for(j=0;j<10;j++)
			a[j]=0;
		in>>n;
		cout<<n<<" "<<endl;
		count=10;
		j=1;
		x=n;
		if(n==0)
		{
			out<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else
		{
			while(count>0)
			{
				n=x*j;
				while(n>0)
				{
					dig=n%10;
					if(a[dig]==0)
					{
						a[dig]++;
						count--;
					}
					n=n/10;
				}
				j++;
			}
			j--;
			out<<"Case #"<<i<<": "<<x*j<<endl;
		}
	}
	in.close();
	out.close();
}
