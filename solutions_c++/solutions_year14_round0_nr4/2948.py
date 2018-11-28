#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <algorithm>
#include <map>
#include <string>
#include <set>
using namespace std;

int N;
list<double> naomi, ken;


int solveY()
{
	int ret = 0;
	naomi.sort();
	ken.sort();
	list<double> naomi2(naomi.begin(), naomi.end());
	list<double> ken2(ken.begin(), ken.end());
	list<double>::iterator itnaomi = naomi2.begin();
	list<double>::iterator itken = ken2.begin();
	while(naomi2.size() > 0)
	{
		if(*itnaomi < *itken)
		{
			naomi2.pop_front();
			ken2.pop_back();
			itnaomi = naomi2.begin();
			itken = ken2.begin();
			continue;
		}
		++itnaomi;
		++itken;
		if(itken == ken2.end())
			break;
	}
	return ken2.size();
}

int solveZ()
{
	list<double> naomi3(naomi.rbegin(), naomi.rend());
	list<double> ken3(ken.rbegin(), ken.rend());
	
	while(naomi3.size() > 0)
	{
		list<double>::iterator itken = ken3.begin();
		list<double>::iterator itnaomi = naomi3.begin();
		while(itnaomi != naomi3.end())
		{
			if(*itken > *itnaomi)
			{
				itnaomi = naomi3.erase(itnaomi);
				ken3.erase(itken);
				break;
			}
			++itnaomi;
		}
		if(itnaomi == naomi3.end())
			break;
	}
	return naomi3.size();
}

int initdata()
{
	N = 0;
	naomi.clear();
	ken.clear();
	return 0;
}

int inputdata()
{
	cin >> N;
	double n, k;
	for(int i=0; i<N; i++)
	{
		cin >> n;
		naomi.push_back(n);
	}
	for(int j=0; j<N; j++)
	{
		cin >> k;
		ken.push_back(k);
	}
	return 0;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("D-large.in", "r", stdin);
	freopen("D-large.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=0; t<T; t++)
	{	
		initdata();
		inputdata();
		//int ret = solve();
		// output
		int y = solveY();
		int z = solveZ();
		printf("Case #%d: %d %d\n", t+1, y, z);
	}
	return 0;
}

