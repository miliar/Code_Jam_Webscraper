#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
using namespace std;

int pol(string s)
{
	int start = 0;
	int flag=1;
	int end = s.size()-1;
	while (end > start)
	{
		if (s[start]!=s[end])
		{
			flag=0;
			break;
		}
		start++;
		end--;
	}
	return flag;
}

void main () 
{
	std::stringstream strs;
	std::string str;


	ifstream infile ("infile.txt");
	ofstream outfile ("result.txt");
	int cases;

	long long p;
	int count=0;
	long long a,b, as, bs;
	double da, db;

	infile >> cases;
	for (int i=0;i<cases; i++)
	{
		count=0;
		infile >> a >> b;
		da = sqrt((double)a);
		as = ceil(da);
		db = sqrt((double)b);
		bs = floor(db);


		for (long long x=as; x<=bs; x++)
		{
			strs.str("");
			str.clear();
			strs << x;
			str=strs.str();
			if (pol(str))
			{
				p=x*x;
				strs.str("");
				str.clear();
				strs << p;
				str=strs.str();
				if (pol(str))
				{
				//	outfile << str << endl;
					count++;
				}
			}
		}
		outfile << "Case #" << i+1 << ": " << count << endl;
	}
	infile.close();
	outfile.close();
}