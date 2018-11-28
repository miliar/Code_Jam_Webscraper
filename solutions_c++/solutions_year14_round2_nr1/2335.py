#include <map>
#include <vector>
#include <list>
#include <array>
#include <string>
#include <iostream>
#include <array>
#include <algorithm>
#include <stdio.h>
#include <stack>
#include <float.h>
#include <cmath>
using namespace std;

//#include <boost/tokenizer.hpp>
//#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
//#include <boost/format.hpp>
//#include <boost/multiprecision/cpp_int.hpp>
using namespace boost;
//using namespace boost::multiprecision;

#define X first
#define Y second


static bool isFeglaWon(int n, vector<string> s)
{
	s[0].erase(unique(s[0].begin(), s[0].end()), s[0].end());
	for (int i = 1; i < n; ++i)
	{
		s[i].erase(unique(s[i].begin(), s[i].end()), s[i].end());
		if (s[0] != s[i])
			return true;
	}
	return false;
}

static auto solve = [](int n, vector<string>& s)
{
	map<char, int> base;
	vector<map<char, int> > m(n);
	vector<string> temp;
	if (isFeglaWon(n, s))
		return string("Fegla Won");
	int result = 0;
	int i = 0;
	int j = 0;
	char c = s[0][0];
	while (s[0][i] != '\0' || s[1][j] != '\0')
	{
		if (s[0][i] == c && s[1][j] == c)
			++i, ++j;
		else if (s[0][i] != c)
		{
			c = s[0][i];
			while (s[1][j] != c)++j, ++result;
		}
		else if (s[1][j] != c)
		{
			c = s[1][j];
			while (s[0][i] != c)++i, ++result;
		}
	}
#if 0
	for (int i = 0; i < n; ++i)
	{
		for (auto v2 : s[i])
		{
			++m[i][v2];
			++base[v2];
		}
	}
	for (auto& v : base)
		v.second /= n;
	for (int i = 0; i < n; ++i)
	{
		for (auto v : m[i])
		{
			result += abs(base[v.first] - v.second);
		}
	}
#endif
	return lexical_cast<string>(result);
};

int main(int argv, char* argc[])
{
	int caseNum;
	cin >> caseNum;
	for (int i = 0; i < caseNum; ++i)
	{
		int n;
		cin >> n;
		vector<string> s(n);
		for (auto &v : s)
			cin >> v;
		cout << "Case #" << i + 1 << ": " << solve(n, s) << endl;

	}
	return 0;
}