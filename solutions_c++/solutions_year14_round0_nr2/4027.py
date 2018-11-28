#include <iostream>
#include <fstream>
#define _USE_MATH_DEFINES
#include <math.h>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>
#include <cstring>

using namespace std;

int main()
{
	int cases;
	string line,temp;
	double c,f,x,leftCookies,sec,lastRemain,incSec=2.0;
	int numTimes;
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	cin>>cases;
	getline(cin,line);
	for (int i=0; i < cases ; i++)
	{
		getline(cin,line);
		istringstream strstr(line);
		strstr>>temp;
		c=atof(temp.c_str());
		strstr>>temp;
		f=atof(temp.c_str());
		strstr>>temp;
		x=atof(temp.c_str());
		sec=0;
		incSec=2.0;
		double remaining=0;
		while (true)
		{
			remaining+=c;
			if(((x-remaining)/incSec)>(x/(incSec+f)))
			{
				sec+=c/incSec;
				incSec+=f;
				remaining=0;
			}
			else
			{
				sec+=x/incSec;
				break;
			}
		}
		cout.precision(7);
		cout<<"Case #"<<fixed<<i+1<<": "<<sec<<endl;
	}
	return 0;

}