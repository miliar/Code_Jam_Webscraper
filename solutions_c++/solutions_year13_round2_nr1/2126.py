#pragma once

#include <cmath>
#include <list>
#include "CodeJamLib.h"
using namespace std;


#define FORIN(a,b) int a; infile >> a; for(int b = 0; b < a; b++)

int limit(int n, int m)
{
	if(n > m)
		n = m;
	return n;
}

void problemA(ifstream& infile, ofstream& outfile)
{
	int a;
	infile >> a;
	vector<int> motes;
	FORIN(n, i)
	{
		int x;
		infile >> x;
		motes.push_back(x);
	}
	sort(motes.begin(), motes.end());
	vector<int> best; // best[i] = given a = i+1, best[1000000] = given a = 1000001 or larger
	for(int i = 0; i < 1000001; i++)
	{
		best.push_back((i >= motes[n-1]) ? 0 : 1);
		if(best[i] == 0)
			break;
	}
	for(int i = n-2; i >= 0; i--)
	{
		for(int j = 0; j < best.size(); j++)
		{
			if(motes[i] <= j)
			{
				best[j] = best[limit(j + motes[i], best.size() - 1)];
				continue;
			}
			int ans = 0;
			int val = j;
			if(val > 0)
			{
				while(motes[i] > val)
				{
					val *= 2;
					ans++;
				}
				ans += best[limit(val + motes[i], best.size() - 1)];
				if(ans < (n - i))
				{
					best[j] = ans;
					continue;
				}
			}
			best[j] = (n - i);
			
		}
	}
	outfile << " " << best[limit(a-1, best.size() - 1)] << endl;
}

void problemB(ifstream& infile, ofstream& outfile)
{

}

void problemC(ifstream& infile, ofstream& outfile)
{
	
}