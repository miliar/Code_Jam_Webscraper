#include<iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <utility>

using namespace std;

pair<int, int> solve(vector<double> &naomi, vector<double> &ken);

void main()
{
	cout << fixed;
	cout << setprecision(7);
	
	int cases;
	cin >> cases;
	
	for(int c = 1; c <= cases; c++)
	{
		int blocks;
		
		cin >> blocks;
		
		vector<double> naomi;
		vector<double> ken;
		double dummy;
		
		for(int i = 0; i < blocks; i++)
		{
			cin >> dummy;
			naomi.push_back(dummy);
		}
		
		for(int i = 0; i < blocks; i++)
		{
			cin >> dummy;
			ken.push_back(dummy);
		}
		
		pair<int, int> ans = solve(naomi, ken);
		
		cout << "Case #" << c << ": " << ans.first << " " << ans.second << endl;		
	}
}

int solveDeceitfulWar(set<double> naomi, set<double> ken)
{
	int wins = 0;
	
	while (!naomi.empty())
	{
		double choosenNaomi, choosenKen;
		set<double>::iterator kenIter = ken.end();
		--kenIter;
		
		set<double>::iterator naomiIter = naomi.upper_bound(*kenIter);
		
		if (naomiIter != naomi.end())
		{
			kenIter = ken.lower_bound(*naomiIter);
			
			if (kenIter == ken.end())
			{
				kenIter--;
			}			
		}
		else
		{
			naomiIter = naomi.begin();
		}

		choosenNaomi = *naomiIter;
		naomi.erase(naomiIter);
		
		choosenKen = *kenIter;
		ken.erase(kenIter);
				
		if (choosenNaomi > choosenKen)
		{
			wins++;
		}	
	}
	
	return wins;
}

int solveWar(set<double> naomi, set<double> ken)
{
	int wins = 0;
	
	while (!naomi.empty())
	{
		double choosenNaomi = *naomi.begin();
		double choosenKen = -1;
		
		naomi.erase(naomi.begin());
		
		set<double>::iterator iter = ken.upper_bound(choosenNaomi);
		
		if (iter == ken.end())
		{
			iter = ken.begin();			
		}
		
		choosenKen = *iter;
		ken.erase(iter);
		
		if (choosenNaomi > choosenKen)
		{
			wins++;
		}	
	}
	
	return wins;
}

pair<int, int> solve(vector<double> &naomi, vector<double> &ken)
{
	set<double> naomiSet(naomi.begin(), naomi.end());
	set<double> kenSet(ken.begin(), ken.end());
		
	return make_pair(solveDeceitfulWar(naomiSet, kenSet), solveWar(naomiSet, kenSet));
}