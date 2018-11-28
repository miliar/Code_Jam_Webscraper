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

static auto solve = [](int a, int b, int k)
{
	int result = 0;
	for (int i = 0; i < a; ++i)
	{
		for (int j = 0; j < b; ++j)
		{
			result += (i&j) < k;
		}
	}
	return result;
};

int main(int argv, char* argc[])
{
	int caseNum;
	cin >> caseNum;
	for (int i = 0; i < caseNum; ++i)
	{
		int a, k, b;
		cin >> a >> b >> k;
		cout << "Case #" << i + 1 << ": " << solve(a, b, k) << endl;

	}
	return 0;
}