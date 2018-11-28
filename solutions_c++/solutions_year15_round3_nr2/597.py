#include "stdafx.h"


#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>
#include <string>
#include <bitset>

using namespace std;

int K,L,S;
string sK,sL, sS;

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

void getStringFromPos(vector<int>& pos)
{
	for( int i = 0; i < pos.size(); ++i)
	{
		sS[i] = sK[pos[i]];
	}
}

int nrOcc()
{
	int qt = 0;
	int i = -1;
	do 
	{
		i = sS.find(sL, i + 1);
		if ( i != string::npos )
		{
			qt++;
		}
	} while ( i != string::npos);
	return qt;
}

double testcase()
{
	cin >> K >> L >> S;
	cin >> sK;
	cin >> sL;
	if ( S < L )
		return 0.0;
	sS.resize(S);
	for( auto it = sL.begin(); it != sL.end() ; ++it)
	{
		if (sK.find(*it) == string::npos)
		{
			return 0.0;
		}
	}
	vector<int> cur(S,0);
	int totOcc = 0;
	int totStr = 0;
	int max = 0;
	do
	{
		getStringFromPos(cur);
		int b = nrOcc();
		if ( b > max )
		{
			max = b;
		}
		totOcc += b;
		totStr++;
	} while( getNextPos(cur));

	return (double)max - (double)totOcc/(double)totStr;

}

int main()
{
	int n;
	std::cin >> n;
	cout.precision(7);
	for (int i = 0; i < n; i++)
	{
		double r = testcase();
		std::cout << "Case #" << i+1 << ": " << r << std::endl;
	}
	
	return 0;
}