//Google Codejam
//2015 Qualification Round
//Alan Richards - alarobric

//Problem C
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

char mult(char a, char b)
{ 
	if (a == '1')
	{
		if (b == '1')
			return '1';
		else if (b == 'i')
			return 'i';
		else if (b == 'j')
			return 'j';
		else if (b == 'k')
			return 'k';
	}
	else if (a == '-')
	{
		if (b == '1')
			return '-';
		else if (b == 'i')
			return 'I';
		else if (b == 'j')
			return 'J';
		else if (b == 'k')
			return 'K';
	}
	else if (a == 'i')
	{
		if (b == '1')
			return 'i';
		else if (b == 'i')
			return '-';
		else if (b == 'j')
			return 'k';
		else if (b == 'k')
			return 'J';
	}
	else if (a == 'I')
	{
		if (b == '1')
			return 'I';
		else if (b == 'i')
			return '1';
		else if (b == 'j')
			return 'K';
		else if (b == 'k')
			return 'j';
	}
	else if (a == 'j')
	{
		if (b == '1')
			return 'j';
		else if (b == 'i')
			return 'K';
		else if (b == 'j')
			return '-';
		else if (b == 'k')
			return 'i';
	}
	else if (a == 'J')
	{
		if (b == '1')
			return 'J';
		else if (b == 'i')
			return 'k';
		else if (b == 'j')
			return '1';
		else if (b == 'k')
			return 'I';
	}
	else if (a == 'k')
	{
		if (b == '1')
			return 'k';
		else if (b == 'i')
			return 'j';
		else if (b == 'j')
			return 'I';
		else if (b == 'k')
			return '-';
	}
	else if (a == 'K')
	{
		if (b == '1')
			return 'K';
		else if (b == 'i')
			return 'J';
		else if (b == 'j')
			return 'i';
		else if (b == 'k')
			return '1';
	}
	return '0';
}

string Solve(int i_case)
{
	int L, X;
	std::string x;
	std::cin >> L >> X;
	std::cin >> x;

	std::string input;
	input.resize(L*X);
	FOR(i, X)
	{
		input.replace(i*L, (i+1)*L, x);
	}
	//cout << input << endl;

	char lookingFor = 'i';
	char current = '1';
	for(int i=0; i<L*X; i++)
	{
		current = mult(current, input[i]);
		//cout << "Current: " << current << " " << input[i] << " L" << lookingFor << "    ";
		if (current == lookingFor)
		{ 
			if (lookingFor == 'i') lookingFor = 'j';
			else if (lookingFor == 'j') lookingFor = 'k';
			else if (lookingFor == 'k') lookingFor = '1';
			current = '1';
		}
	}
	if (lookingFor == '1' && current == '1') return "YES";
	
	return "NO";
}

int main()
{
	std::cerr << "GCJ 2015 Qualification Round" << std::endl;
	int numCases;
	std::cin >> numCases;
	for (int i=1; i<=numCases; i++)
	{
		std::cout << "Case #" << i << ": " << Solve(i) << std::endl;
	}
	return 0;
}