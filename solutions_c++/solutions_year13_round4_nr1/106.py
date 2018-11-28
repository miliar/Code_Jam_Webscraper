#include <iostream>
#include <gmpxx.h>
#include <vector>
#include <algorithm>

using namespace std;

void doCase()
{
	int N, M;
	
	cin >> N >> M;
	
	vector<pair<int, int> > events;
	
	mpz_class cityCost = 0;
	
	for (int i=0; i<M; i++)
	{
		int ei, oi, pi;
		cin >> oi >> ei >> pi;
		events.push_back(make_pair(oi, -pi));
		events.push_back(make_pair(ei, pi));
		
		mpz_class dist = ei-oi;
		cityCost = cityCost + (dist * mpz_class(N) - (dist * (dist-1))/mpz_class(2))*mpz_class(pi);
	}
	
	sort(events.begin(), events.end());
	
	vector<pair<int, int> > tickets;
	
	mpz_class optCost = 0;
	
	for (int i=0; i<2*M; i++)
	{
		int loc = events[i].first;
		int exit = events[i].second;
		
		//cout << loc << " " << exit << " " << optCost << endl;
		
		if (exit < 0)
		{
			tickets.push_back(make_pair(loc, -exit));
		}
		else
		{
			while (exit)
			{
				int tloc = tickets.back().first;
				int tamm = tickets.back().second;
				mpz_class dist = loc-tloc;
				//cout << dist << " " << tamm << " " << exit << endl;
				if (tamm > exit)
				{
					tickets.back().second -= exit;
					optCost = optCost + mpz_class(exit)*(dist * mpz_class(N) - (dist*(dist - 1))/2);
					exit = 0;
					//cout << "C1 ";
				}
				else
				{
					exit -= tamm;
					tickets.pop_back();
					optCost = optCost + mpz_class(tamm)*(dist * mpz_class(N) - (dist*(dist - 1))/2);
					// << "C2 ";
				}
				//cout << optCost << endl;
			}
		}
	}
	
	cout << (cityCost - optCost) << endl;
}

int main()
{
	int T;
	cin >> T;
	
	for (int i=1; i<=T; i++)
	{
		cout << "Case #" << i << ": ";
		doCase();
	}
	
	return 0;
}
