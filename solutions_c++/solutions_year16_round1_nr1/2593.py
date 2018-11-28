#include <iostream>
#include <vector>
#include <string>
#include <ostream>
#include <algorithm>
#include <iterator>
#include <array>
// #include <discreture/discreture.hpp>

using namespace std;
// using namespace dscr;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& rhs)
{
	for (const auto& x : rhs)
		os << x << " ";
	return os;
}

using ullong = unsigned long long int;

template <class IntType>
IntType InterpretBaseK(int k, const vector<int>& bla)
{
	IntType suma = 0;
	IntType power = 1;
	for (auto it = bla.rbegin(); it != bla.rend(); ++it)
	{
		suma += power*static_cast<IntType>(*it);
		power *= k;
	}
	return suma;
}

vector<unsigned short> NumberBaseB(unsigned int n, short b)
{
	vector<unsigned short> toReturn;
	while (n != 0)
	{
		toReturn.push_back(n%b);
		n /= b;
	}
	std::reverse(toReturn.begin(), toReturn.end());
	return toReturn;
}

int gcd(int a,int b)
{
	if (b == 0) return a;
	return gcd(b,a%b);
}

int lcm(int a, int b)
{
	return a*b/gcd(a,b);
}

int gcd(vector<int> A)
{
	auto a = A.back();
	if (A.size() == 1)
		return a;
	A.pop_back();
	auto b = A.back();
	A.back() = gcd(a,b);
	return gcd(A);
}

int lcm(vector<int> A)
{
	auto a = A.back();
	if (A.size() == 1)
		return a;
	A.pop_back();
	auto b = A.back();
	A.back() = lcm(a,b);
	return lcm(A);
}

void Solve(const string& s)
{
	string b(1,s[0]);
	for (int i = 1; i < s.size(); ++i)
	{
		if (s[i] >= b[0])
			b.insert(b.begin(), s[i]);
		else
			b.push_back(s[i]);
	}
	cout << b;
}


int main() 
{
	int Total;
	cin >> Total;
	for (int i = 0; i < Total; ++i)
	{
		string s;
		cin >> s;
		
		cout << "Case #" << i+1 << ": ";
		Solve(s);
		cout << endl;
	}
	
	
	return 0;
}
