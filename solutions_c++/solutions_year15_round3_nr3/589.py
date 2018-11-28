#include "stdafx.h"

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;

int K = 2;

bool getNextPos(vector<int>& pos)
{
	for( int i = pos.size() - 1 ; i >= 0 ; --i)
	{
		if( pos[i] == K - 1)
		{
			i--;
			while ( i >= 0 && pos[i] == K - 1 )
				--i;
			if ( i < 0 )
				return false;
		}
		pos[i++]++;
		while ( i < pos.size() )
			pos[i++] = 0;
		return true;
	}
	throw "sss";
}

int getSum(vector<int>& cur, vector<int>& ex)
{
	int sum = 0;
	for( int i = 0 ; i < cur.size() ; ++i)
	{
		sum += cur[i] * ex[i];
	}
	return sum;
}

int getCoveredQt( int m, vector<bool>& poss)
{
	int qt = 0;
	for( int i = m ; i < poss.size() ; ++i)
	{
		if( !poss[i] && poss[i - m])
			qt++;
	}
	return qt;
}

int testcase()
{
	int ccc,d,v;
	cin >> ccc >> d >> v;
	vector<int> ex(d);
	vector<bool> poss(v + 1,false);
	poss[0] = true;
	vector<bool> exist(v + 1,false);
	for( int i = 0 ; i < d ;++i)
	{
		cin >> ex[i];
		exist[ex[i]] = true;
	}

	vector<int> cur(d, 0);
	while( getNextPos(cur) )
	{

		int sum = getSum(cur,ex);
		if ( sum < poss.size() )
			poss[sum] = true;
	}

	int res = 0;
	int it = 0;
	while( it < poss.size() && poss[it] )
		it++;
	while ( it < poss.size() )
	{
		int mon = it;
		int maxcov = 0, maxind = 0;
		for( int i = 1 ; i <= mon; ++i)
		{
			if ( exist[i] || !poss[mon - i] ) // must cover mon
				continue;
			int gc = getCoveredQt(i, poss);
			if ( gc > maxcov )
			{
				maxcov = gc;
				maxind = i;
			}
		}

		exist[maxind] = true;
		res++;
		for(int i = poss.size() - 1 ; i >= maxind ; --i)
		{
			if ( poss[i - maxind] )
				poss[i] = true;
		}
		it = 0;
		while( it < poss.size() && poss[it] )
			it++;
	}
	return res;
} 

int main()
{
	int n;
	std::cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		int r = testcase();
		std::cout << "Case #" << i+1 << ": " << r << std::endl;
	}
	
	return 0;
}