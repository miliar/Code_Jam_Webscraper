#include <fstream>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <algorithm>
#include <math.h>
using namespace std;

int war(set<double> Naomi , set<double> Ken)
{
	int ret = 0;
	set<double> :: iterator Nit;
	set<double> :: iterator Kit;
	while(!Naomi.empty())
	{
		Nit = Naomi.begin();
		Kit = Ken.upper_bound(*Nit);
		if(Kit != Ken.end())
		{
			Ken.erase(Kit);
		}
		else
		{
			Ken.erase(Ken.begin());
			ret ++;
		}
		Naomi.erase(Nit);
	}
	return ret;
}

int cheatWar(set<double> Naomi , set<double> Ken)
{
	int ret = 0;
	set<double> ::reverse_iterator rNit;
	set<double> :: iterator Nit;
	set<double> :: iterator Kit;
	while(!Naomi.empty())
	{
		rNit = Naomi.rbegin();
		Kit = Ken.upper_bound(*rNit);
		if(Kit!=Ken.end())
		{
			Ken.erase(Kit);
			Naomi.erase(Naomi.begin());
		}
		else
		{
			Kit = Ken.begin();
			Nit = Naomi.upper_bound(*Kit);
			Ken.erase(Kit);
			Naomi.erase(Nit);
			ret ++;
		}
	}
	return ret;

}

int main()
{
	ifstream curFile("D-large.in");
	vector<pair<int , int> > result;
	set<double>	Naomi;
	set<double>	Ken;
	int T; // testcases count
	int N;
	double temp;
	pair<int , int> cur;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
			curFile >> N;
			Naomi.clear();
			Ken.clear();
			for(int i = 0 ; i < N ; i++)
			{
				curFile >> temp;
				Naomi.insert(temp);
			}
			for(int i = 0 ; i < N ; i++)
			{
				curFile >> temp;
				Ken.insert(temp);
			}
			cur.first = cheatWar(Naomi, Ken);
			cur.second = war(Naomi, Ken);
			result.push_back(cur);
		}	
	}
	curFile.close();
	ofstream outfile;
	outfile.open("result.txt");
	if(outfile.is_open())
	{
		for(int i = 0; i < result.size() ; i++)
			outfile << "Case #" << i + 1<< ": " <<result[i].first<<' '<<result[i].second << endl;
	}
	outfile.close();
	return 0;
}
