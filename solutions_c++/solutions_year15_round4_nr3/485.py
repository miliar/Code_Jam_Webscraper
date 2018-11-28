#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
#include <functional>


#define INF 2147483647
#define PI acos(-1.0)

using namespace std;

int GO[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
map<char, int> M = {{'^', 0}, {'>', 1}, {'v', 2}, {'<', 3}};
std::hash<std::string> str_hash;

std::vector<size_t> &split(const std::string &s, char delim, std::vector<size_t> &elems) {
	std::stringstream ss(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		elems.push_back(str_hash(item));
	}
	return elems;
}

set <size_t> eng, fr;
vector < vector <size_t> > S;
size_t pred;

size_t count(set <size_t> const & A, set <size_t> const & B)
{
	size_t ans = 0;
	for(auto item : B)
		ans += A.count(item);
	return ans;
}

int rec(int i)
{
	if(i == S.size())
		return pred;

	int ans = INF;

	vector<size_t> tmp;
	tmp.reserve(10);

	int cur = 0;
	for(size_t j = 0; j < S[i].size(); ++j)
	{
		if(eng.count(S[i][j]) == 0)
		{
			eng.insert(S[i][j]);
			tmp.push_back(S[i][j]);
			if(fr.count(S[i][j]) != 0)
				++cur;
		}
	}
	pred += cur;
	ans = min(ans, rec(i+1));
	pred -= cur;
	for(int j = 0; j < tmp.size(); ++j)
		eng.erase(tmp[j]);

	tmp.clear();
	tmp.reserve(10);
	cur = 0;
	for(size_t j = 0; j < S[i].size(); ++j)
	{
		if(fr.count(S[i][j]) == 0)
		{
			fr.insert(S[i][j]);
			tmp.push_back(S[i][j]);
			if(eng.count(S[i][j]) != 0)
				++cur;
		}
	}
	pred += cur;
	ans = min(ans, rec(i+1));
	pred -= cur;
	for(int j = 0; j < tmp.size(); ++j)
		fr.erase(tmp[j]);

	return ans;
}

int main(int argc, const char ** argv)
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for(int _t = 1; _t <= tests; ++_t)
	{
		eng.clear();
		fr.clear();
		S.clear();
		int n;
		cin >> n;
		S.resize(n);
		string s;
		getline(cin, s);
		for(int i = 0; i < n; ++i)
		{
			getline(cin, s);
			split(s, ' ', S[i]);
		}

		eng.insert(S[0].begin(), S[0].end());
		fr.insert(S[1].begin(), S[1].end());

		pred = count(eng, fr);

		int ans = rec(2);

		printf("Case #%d: %d\n", _t, ans);
	}

	return 0;
}
