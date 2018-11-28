#include<iostream>
#include<fstream>
#include<math.h>
#include<string.h>
#include <sstream>
#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

using namespace std;

bool pandrome(string s)
{
	int length = s.length();
	if(length%2==0)
	{
		for(int i=0;i<length;i++)
		{
			if(s[i]!=s[length-i-1])
			{
				return false;
			}
		}
	}
	else
	{
		for(int i=0;i<length;i++)
		{
			if(s[i]!=s[length-i-1])
			{
				return false;
			}
		}
	}
	return true;
}

void main()
{

	int T=0;
	ifstream in("C-small-attempt0.in");
	ofstream save("r3.txt");
	in >> T;

	for(int p=0 ; p<T;p++)
	{
		int low = 0;
		int high = 0;
		in >> low;
		in >> high;
		int l = (int)ceil(sqrt(low+0.0));
		int h = (int)floor(sqrt(high+0.0));
		int count = 0;
		for(int i=l;i<h+1;i++)
		{
			int k = i;
			string str = SSTR(k);
			string s = SSTR(k*k);
			//std::string s = std::to_string(i*i);
			if(pandrome(str))
			{
				if(pandrome(s))
				{
					count++;
				}
			}

		}
	
		save << "Case #"<<p+1<<": "<<count << "\n";

	}
	in.close();
	save.close();
}
