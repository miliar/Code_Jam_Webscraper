#include <stdio.h>
#include <fstream>
using namespace std;
int main()
{
	long n;
	ifstream myfile;
	ofstream myfile1;
	myfile.open ("A-large.in");
	myfile>>n;
	myfile1.open("Output1");
	int i,j;
	for(i=0;i<n;i++)
	{
		long int t;
		myfile>>t;
		if(t==0)
		{
			myfile1<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
		}
		else
		{
			long arra[10]={0};
			int q = t;
			while(true)
			{
				int flag = 1;
				int p = t;
				while(t)
				{
					arra[t%10]++;
					t=t/10;
				}
				for(j=0;j<10;j++)
				{
					if(arra[j]==0)
					{
						flag = 0;
					}
				}
				if(flag==0)
				{	
					t = p+q;
				}
				else
				{
					myfile1<<"Case #"<<(i+1)<<": "<<p<<endl;
					break;
				}
			}
		}
	}
	myfile1.close();
	myfile.close();
}