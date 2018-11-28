#include <iostream>
using namespace std;

int main() 
{
	long t = 0, sMax;
	char s[1024];
	
	cin>>t;
	
	for(long i = 0; i < t; i++) 
	{
		cin>>sMax;
		cin>>s;
		
		long total = 0;
		long totalInv = 0;
		for(int level = 0; level <= sMax; level++)
		{
			int count = s[level] - 48;
//			cout<<"i="<<i<<" level="<<level<<" count="<<count<<" total="<<total<<endl;
			int inv = 0;
			if(level > total)
			{
				inv = level - total;
			}
			
			totalInv += inv;
			total += count + inv;
		}
		
		cout<<"Case #"<<(i+1)<<": "<<totalInv<<endl;
	}

	return 0;	
}
