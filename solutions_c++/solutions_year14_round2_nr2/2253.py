#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
using namespace std;

vector<long long> ans;
string as_binary( unsigned num )
{
	unsigned mask = 1 << numeric_limits<unsigned>::digits-1 ;

	while ( (mask & num) == 0 )
		mask >>= 1 ;

	string result ;
	while ( mask )
	{
		result.push_back( (mask&num ? '1' : '0') ) ;
		mask >>= 1 ;
	}

	return result ;
}

int main()
{
	ifstream in("B-small-attempt0.in");
	ofstream out("out.txt");
	int k;
	in>>k;
	ans.resize(k);
	for(int z = 0;z<k;z++)
	{
		int a, b, k;
		in>>a>>b>>k;
		int counter = 0;
		for(int i =0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					counter++;
				}
			}
		}
		ans[z] = counter;
	}
	for(int i=0;i<k;i++)
	{
		out<<"Case #"<<i+1<<": "<<ans[i]<<endl;
	}
	return 0;
}