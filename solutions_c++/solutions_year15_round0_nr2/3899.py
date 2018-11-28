//Google Codejam
//2015 Qualification Round
//Alan Richards - alarobric

//Problem B
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <array>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <limits.h>
using namespace std;

#define FOR(i, n) for(ull i=0; i<n; i++)
#define FOREACH(c, iter) for(auto iter=c.begin(); iter!=c.end(); iter++)

#ifdef DEBUG
#define Debug(x) std::cerr << x << endl
#else
#define Debug(x)
#endif

typedef unsigned long long ull;
typedef vector<vector<int> > vvi;
typedef vector<int> vi;

template <class T>
string ContainerPrint(T a)
{
	stringstream ss;
	FOREACH(a, iter)
		ss << *iter << " ";
	return ss.str();
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int Choice(std::array<int, 1001> P, int i, int moves, int bestMoves)
{
	while (P[i] == 0 && i>0)
		i--;

	bestMoves = min(i+moves, bestMoves);

	if (i>3 and P[i] + moves < bestMoves)
	{ 
		if (i==9)	//special case
		{ 
			auto P2 = P;
			auto moves2 = moves;
			while (P2[i] > 0)
			{
				P2[3] += 3;
				moves2 += 2;
				P2[i]--; 
			}
			bestMoves = min(bestMoves, Choice(P2, i-1, moves2, bestMoves));
		}
		while (P[i] > 0)
		{
			P[i/2]++;
			P[i-i/2]++;
			P[i]--;
			moves++;
		}
		bestMoves = min(bestMoves, Choice(P, i-1, moves, bestMoves));
	}
	return bestMoves;
}

int Solve(int i_case)
{
	int D;
	std::cin >> D;
	std::array<int, 1001> P;
	memset(&P, 0, sizeof(int)*1001);
	FOR(i, D)
	{
		int p;
		std::cin >> p;
		//std::cout << p << " ";
		P[p]++;
	}
	//std::cout << endl;
	
	for(ull i=1000; i>0; --i)
	{
		if (P[i] > 0)
		{ 
			return Choice(P, i, 0, i);
		}
	}
	return -1;
	//if 1, 2, or 3 pancakes, fastest just to eat them. No need to move them
	//4=3, 5=4, 6=4, 7=5, 8=5, 9=5
}

int main()
{
	std::cerr << "GCJ 2015 Round - B" << std::endl;
	int numCases;
	std::cin >> numCases;
	for (int i=1; i<=numCases; i++)
	{
		std::cout << "Case #" << i << ": " << Solve(i) << std::endl;
	}
	return 0;
}