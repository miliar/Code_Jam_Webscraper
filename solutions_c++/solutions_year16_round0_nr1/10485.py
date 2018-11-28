#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int t;
	long long int sum,n,ch=1;
	ifstream fin("aIn.txt");
	ofstream fout("aOut.txt");
	if(fin.is_open())
	{
		fin>>t;
	}
	while(t)
	{
		int a[10];
		for(int i=0;i<10;++i)
			a[i]=0;

		fin>>n;
		if(n==0)
			fout<<"Case #"<<ch<<": INSOMNIA\n";
		else
		{	

			int x=n,i=0;
			sum = 0;
			while(sum!=10)
			{
				++i;
				x=n*i;
				int temp=x,rem;
				while(temp !=0)
				{	
					rem=temp%10;
					if(a[rem]==0)
					{
						++a[rem];
						++sum;
					}
					temp=temp/10;
				}
				
			}
			fout<<"Case #"<<ch<<": "<<x<<"\n";
		}
		++ch;
		--t;
	}
	fin.close();
	fout.close();
	return 0;
	
}