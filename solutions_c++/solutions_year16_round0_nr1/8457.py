#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	long long t1,n;
	ifstream inp("input.txt");
	ofstream out("output.txt");
	string line;
	inp>>t1;
	for(long long it=1;it<=t1;it++)
	{
		int a,hash[10]={0},done=0;
		inp>>a;
		if(a==0)
		out<<"Case #"<<it<<": "<<"INSOMNIA\n";
		else
		{
			int n=0;
			int f;
			for(int i=1;done<10;i++)
			{
				n=i*a;
				while(n!=0)
				{
					int l=n%10;
				//	cout<<n<<"\t"<<l<<"\t"<<done<<"\n";
					n=n/10;
					if(hash[l]==0)
					{
						done++;
						hash[l]=1;	
					}
				}
				f=i*a;
			}
			out<<"Case #"<<it<<": "<<f<<endl;	
		}	
	}
	out.close();
}
