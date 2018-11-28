#include "stdafx.h"
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

struct bignum
{
	bignum() : odd(false) {}

	bool odd;
	vector<int> value;
	friend istream& operator >> (istream& in, bignum& bn);
	friend ostream& operator << (istream& in, const bignum& bn);

	bool operator <(const bignum& other) const
	{
		if(value.size() < other.value.size())
			return true;
		if(value.size() == other.value.size())
			return lexicographical_compare(value.begin(), value.end(), other.value.begin(), other.value.end());
		else
			return false;
	}

	bignum toNum() const
	{
		bignum r;
		r.value.resize(value.size() * 2 - (odd ? 1 : 0));

		for(int i=0; i<value.size();++i)
			r.value[i] = value[i];
		int k = value.size();
		for(int i=value.size()- (odd ? 2 : 1); i>=0;--i, ++k)
			r.value[k] = value[i];
		return r;
	}
	
	unsigned long long toLong() const
	{
		unsigned long long v = 0;
		for(int i=0; i<value.size();++i)
		{
			unsigned long long c = value[i];
			v = v * 10ULL + c;
		}
		return v;
	}
};

set<unsigned long long> alls;

istream& operator >> (istream& in, bignum& bn)
{
	string s;
	in >> s;
	bn.value.resize(s.length());
	for(int i=s.length()-1;i>=0; --i)
		bn.value[i] = s[i]-'0';
	return in;
}

ostream& operator << (ostream& out, const bignum& bn)
{
	for(int i=0; i<bn.value.size();++i)
		out << bn.value[i];
	for(int i=bn.value.size()- (bn.odd ? 2 : 1); i>=0;--i)
		out << bn.value[i];
	return out;
}

int countPal(int upto, int dig, int limit, bignum& calc)
{
	if(dig == upto)
	{
		unsigned long long ll =calc.toNum().toLong();
		unsigned long long sq = ll * ll;
		alls.insert(sq);
		return 1;
	}
	int counter = 0;
	int start = dig == 0 ? 1 : 0;
	for(int i=start; 2 * i * i <= limit; ++i)
	{
		calc.value[dig] = i;
		counter += countPal(upto, dig + 1, limit - 2 * i * i, calc);
	}
	if(dig == upto-1)
	{
		calc.odd = true;
		for(int i=start; i * i <= limit; ++i)
		{
			calc.value[dig] = i;
			counter += countPal(upto, dig + 1, 0, calc);
		}
		calc.odd = false;
	}
	return counter;
}

int _tmain(int argc, _TCHAR* argv[])
{
	alls.insert(1);
	alls.insert(4);
	alls.insert(9);
	for(int i=1; i<6; ++i)
	{
		bignum calc;
		calc.value.resize(i);
		countPal(i, 0, 9, calc);
	}
	int T;
	cin >> T;
	for(int t=0; t<T; ++t)
	{
		unsigned long long A, B;
		cin >> A >> B;
		auto itA = alls.lower_bound(A);
		auto itB = alls.upper_bound(B);
		int n = distance(itA, itB);
		cout << "Case #" << t+1 << ": " << n << endl;
	}
	return 0;
}

