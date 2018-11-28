#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
#include<bitset>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define mp make_pair

namespace
{
	string intToString(int x) { ostringstream ss; ss<<x; return ss.str(); }
	string longToString(ll x) { ostringstream ss; ss<<x; return ss.str(); }

	struct MyStringSort
	{
		bool operator()(const string& s1, const string& s2) const
		{
			int ret = s1.size() - s2.size();
			if (ret == 0)
				return s1 < s2;
			return ret < 0;
		}
	};

	bool isPal(const string& s)
	{
		for (size_t i=0; i<s.size()/2; ++i)
			if (s[i] != s[s.size()-1-i])
				return false;

		return true;
	}

	bool isPal(ll x)
	{
		static string s;
		s = longToString(x);
		return isPal(s);
	}

	vector<int> v;

	bool can(const string& s, string& nextResult)
	{
		v.assign(s.size() * 2 - 1, 0);
		for (int i=0; i<s.size(); ++i)
		{
			for (int j=0; j<s.size(); ++j)
			{
				int add = int(s[i] - '0') * int(s[j] - '0');
				if ((v[i+j] += add) > 9)
					return false;
			}
		}

		nextResult.resize(v.size());
		for (int i=0; i<v.size(); ++i)
			nextResult[i] = v[i] + '0';

		return isPal(nextResult);
	}
}

int main()
{
	ifstream fin("C-large-2.in");
	ofstream fout("C-large-2.out");

	vector<string> pals;
	pals.push_back("1");
	pals.push_back("4");
	pals.push_back("9");

	int maxOnes(0);
	string s1, s2, s, forVector;
	for (int mask=1; mask < (1<<25); ++mask) // should be up to 25 characters, as that doubles
	{
		if (bitset<32>(mask).count() > 5) continue;

		s2.clear();
		int x(mask);

		int numOnes(0);
		while (x)
		{
			s2 += (x%2) ? '1' : '0';
			numOnes += (x%2) ? 1 : 0;
			x /= 2;
		}

		s1 = s2; reverse(s1.begin(), s1.end());
		s = s1 + s2;
		if (can(s, forVector))
		{
			pals.push_back(forVector);
			if (numOnes > maxOnes)
			{
				cout << numOnes << endl;
				maxOnes = numOnes;
			}
		}

		for (char c = '0'; c <= '2'; ++c)
		{
			s = s1 + c + s2;
			if (can(s, forVector))
			{
				pals.push_back(forVector);
				if (numOnes > maxOnes)
				{
					cout << numOnes << endl;
					maxOnes = numOnes;
				}
			}
		}
	}

	string twos;
	for (int len = 2; len <= 50; ++len) // should be up to 50 as it's the whole word
	{
		twos.assign(len, '0');
		twos[0] = twos.back() = '2';

		if (can(twos, forVector))
			pals.push_back(forVector);

		if (len % 2)
		{
			twos[len/2] = '1';
			if (can(twos, forVector))
				pals.push_back(forVector);
		}
	}

	sort(pals.begin(), pals.end(), MyStringSort());

	unsigned int numberOfCases;
	fin >> numberOfCases;

	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		string A, B;
		fin >> A >> B;

		auto it1 = lower_bound(pals.begin(), pals.end(), A, MyStringSort());
		auto it2 = upper_bound(pals.begin(), pals.end(), B, MyStringSort());
		int result = distance(it1, it2);
		//for (size_t i=0; i<pals.size(); ++i)
		//	if (pals[i] >= A && pals[i] <= B)
		//		++result;
		
		fout << "Case #" << zz << ": " << result << endl;
	}

	return 0;
}