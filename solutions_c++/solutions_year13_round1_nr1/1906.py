#include <iostream>
#include <vector>
#include "myLib.hpp"
#include <boost/algorithm/string.hpp>

using namespace std;

typedef unsigned __int64 ULONG64;

void main(void)
{
	char numcase[10];
	cin.getline(numcase, 10);

	int casecnt = atoi(numcase);

	for(int i = 0; i < casecnt; i++)
	{
		char oneline[1000];

		cin.getline(oneline, 1000);

		vector<string> a;
		a = mylib::StringSplit(oneline);
		
		double r = atof(a[0].c_str());
		double t = atof(a[1].c_str());

		double n;
		n = 1;

		ULONG64 lCnt = 0;

		while(1)
		{
			double tt = 2*r + 2*n - 1;

			if (tt > t)
				break;
			 t-=tt;
			 lCnt++;

			n +=2;
		}

		cout<<"Case #"<<i+1<<": "<<lCnt<<"\n";
	}
}