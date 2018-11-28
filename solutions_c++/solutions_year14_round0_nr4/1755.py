#include <iostream>
#include <set>
#include <cstdio>
#include <list>
#include <algorithm>

using namespace std;

int main()
{
	int nrOfCases;
	cin >> nrOfCases;
	list<double> naomi;
	list<double> naomicopy;
	list<double> ken;
	list<double> kencopy;
	
	for (int c = 1; c <= nrOfCases; c++)
	{
		naomi.clear();
		naomicopy.clear();
		ken.clear();
		kencopy.clear();
		
		int N;
		cin >> N;
		
		for (int i = 0; i < N; i++)
		{
			double d;
			cin >> d;
			naomi.push_back(d);
		}
		naomi.sort();
		naomicopy.assign(naomi.begin(), naomi.end());
		
		for (int i = 0; i < N; i++)
		{
			double d;
			cin >> d;
			ken.push_back(d);
		}
		ken.sort();
		kencopy.assign(ken.begin(), ken.end());
		
		int score1 = 0;
		while (naomi.size() > 0)
		{
			if (naomi.front() < ken.front())
			{
				naomi.pop_front();
				ken.pop_back();
			}
			else
			{
				naomi.pop_front();
				ken.pop_front();
				score1++;
			}
		}
		
		int score2 = 0;
		
		while (naomicopy.size() > 0)
		{
			for (list<double>::iterator it = kencopy.begin(); it != kencopy.end(); ++it)
			{
				if (*it > naomicopy.front())
				{
					naomicopy.pop_front();
					kencopy.erase(it);
					break;
				} 
				else
				{
					kencopy.pop_front();
					it--;
					naomicopy.pop_back();
					score2++;
				}
			}
		}
		
		printf("Case #%d: %d %d\n", c, score1, score2);
	}
}
