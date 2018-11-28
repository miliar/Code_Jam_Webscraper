//Google Codejam
//2015 Qualification Round
//Alan Richards - alarobric

//Problem A
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

int Solve(int i_case)
{
	int Smax;
	string S;
	std::cin >> Smax >> S;

  int numStanding = 0;
  int numNeeded = 0;
	for (int i = 0; i <= Smax; ++i)
	{
		if (numStanding < i)
		{
			numNeeded++;
			numStanding++;
		}
		int Si = S[i] - '0';
		numStanding += Si;
	}
	
	return numNeeded;
}

int main()
{
	std::cerr << "GCJ 2015 Round Q-A" << std::endl;
	int numCases;
	std::cin >> numCases;
	for (int i=1; i<=numCases; i++)
	{
		std::cout << "Case #" << i << ": " << Solve(i) << std::endl;
	}
	return 0;
}