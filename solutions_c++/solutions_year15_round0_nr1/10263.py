#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile("A-small-attempt2.in");
	ofstream outfile("output.txt");
	long long int t,p=1;
	infile>>t;
	while(t--)
	{
		long long int n;
		infile>>n;
		char a[n+1];
		long long int b[n+1],i;
		infile>>a;
		for(i=0;i<=n;i++)
		{
			b[i] = a[i] - '0';
		}
		long long int count=0,add=0;
		for(i=0;i<=n;i++)
		{
			if(i > count)
			{
				add = add + i - count;
				count = i; 
			}
			count = count + b[i];
		}
		outfile<<"Case #"<<p<<": "<<add<<endl;
		p++;
	}
	return 0;
}

