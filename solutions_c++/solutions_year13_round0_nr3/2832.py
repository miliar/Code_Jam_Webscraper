#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include <string>
#include <sstream>

using namespace std;
class BigInteger
{
public:
	BigInteger(){};
	bool is_pad(unsigned long& data)
	{
		ostringstream con_str;
		con_str<<data;
		size_t len = con_str.str().length();

		for(int i=0; i<len/2; i++)
		{
			if(con_str.str()[i] != con_str.str()[len-i-1])
				return false;
		}
		return true;
	}
	bool is_sqaure(unsigned long& data, unsigned long& mid)
	{
		unsigned long begin = 0;
		unsigned long end = data;
		if(data == 1)
			return true;
		while(begin+1 < end)
		{
			mid = (begin + end) / 2;
			unsigned long sqr_mid = mid * mid;
			if(sqr_mid == data)
				return true;
			else if(sqr_mid > data)
			{
				end = mid;
			}
			else
			{
				begin = mid;
			} 
		}	
		return false;	 
	}
	virtual ~BigInteger(){};
};

int main(int argc, char* argv[])
{
	ifstream inf(argv[1]);
	assert(inf.is_open());
	string line;

	getline(inf, line);
	int T = atoi(line.c_str());
	unsigned long A, B;
	for(int t=0; t<T; t++)
	{
		unsigned long num_count = 0;
		unsigned long sqr_mid = 0;
		getline(inf, line);
		sscanf((char*) line.c_str(),"%lu %lu\n", &A, &B);
		for(unsigned long i = A; i<=B; i++)
		{
			BigInteger bint;
			if(!bint.is_pad(i))
				continue;
			
			if(!bint.is_sqaure(i, sqr_mid))
				continue;
		
			if(!bint.is_pad(sqr_mid))
				continue;
			
			num_count++;
		}
		cout<<"Case #"<<t+1<<": "<<num_count<<endl;

	}
	inf.close();	
	return 0;
}

