#include <iostream>
#include <vector>
#include <algorithm>
#include <istream>
#include <fstream>
#include <iomanip>

using namespace std;

int optimalwar(vector<double>nami,vector<double>kan)
{
	int namiCount =0;
	int len = nami.size();
	vector<double>::iterator namiItr;
	vector<double>::iterator kanItr;
	for(int i=0;i<len;i++)
	{
		namiItr = nami.end()-1;
		kanItr = kan.end()-1;
		if(*namiItr > *kanItr)
		{
			nami.erase(namiItr);
			kan.erase(kan.begin());
			namiCount++;
		}
		else
		{
			nami.erase(namiItr);
			kan.erase(kanItr);
		}
	}
	return namiCount;
}
int decivewar(vector<double>nami,vector<double>kan)
{
	int len = nami.size();
	int i = 0;
	int namiCount = 0;
	vector<double>::iterator namiItr;
	vector<double>::iterator kanItr;
	for(i=0;i<len;i++)
	{
		namiItr = nami.begin();
		kanItr = kan.begin();
		if(*namiItr < *kanItr)
		{
			nami.erase(namiItr);
			kan.erase(kan.end()-1);
		}
		else
		{
			nami.erase(nami.begin());
			kan.erase(kan.begin());
			namiCount++;
		}
	}
	return namiCount;
}
int main(void)
{
	int numB;
	int T;
	vector<double>nami;
	vector<double>kan;
	ifstream read("input.txt");
	ofstream write("output.txt");
	read>>T;

	for(int j=0;j<T;j++)
	{
		read>>numB;
		double val;
		for(int i=0;i<numB;i++)
		{
			read>>val;
			nami.push_back(val);
		}
		for(int i=0;i<numB;i++)
		{
			read>>val;
			kan.push_back(val);
		}
		sort(nami.begin(),nami.end());
		sort(kan.begin(),kan.end());
		int namiCount1 = decivewar(nami,kan);
		int namiCount2 = optimalwar(nami,kan);
		write<<"Case #"<<j+1<<": "<<namiCount1<<" "<<namiCount2<<endl;
		nami.clear();
		kan.clear();
	}
	return 0;
}

