#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int t,count,a[10],j,r,k;
	long long int n,m,i,c;
	ifstream in;
	ofstream out;
	
	in.open("input.txt");
	out.open("output.txt");
	
	in>>t;
	for(k=0;k<t;k++)
	{
		count=0;
		in>>n;
		c=1;
		if(n==0)
		{
			out<<"Case #"<<k+1<<": INSOMNIA\n";
		}
		else
		{
		for(j=0;j<10;j++)
		{
			a[j]=0;
		}
		m=n;
		while(count<10)
		{
			c++;
			while(n>0)
			{
				r=n%10;
				n=n/10;
				if(a[r]==0)
				{
					count++;
					a[r]=1;
				}
			}
		    
		    if(count<10)
		    {
			  n=c*m;
			}
			else
			{
			  n=(c-1)*m;
			}
		
		}
		out<<"Case #"<<k+1<<": "<<n<<endl;
		}
		
	}
	in.close();
	out.close();
}
