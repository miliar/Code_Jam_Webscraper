#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

typedef unsigned long long uint64;

inline uint64 palindrome14(uint64 a, uint64 b, uint64 c, uint64 d, uint64 e, uint64 f, uint64 g)
{
	//return a*10000000000000 + b*1000000000000 + c*100000000000 + d*10000000000 + e*1000000000 + f*100000000 + g*10000000 + g*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a;
	//return a*10000000000001 + b*1000000000010 + c*100000000100 + d*10000001000 + e*1000010000 + f*100100000 + g*11000000;
	return 11 * (a*909090909091 + b*90909090910 + c*9090909100 + d*909091000 + e*90910000 + f*9100000 + g*1000000);
}

inline uint64 palindrome13(uint64 a, uint64 b, uint64 c, uint64 d, uint64 e, uint64 f, uint64 g)
{
	return a*1000000000000 + b*100000000000 + c*10000000000 + d*1000000000 + e*100000000 + f*10000000 + g*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome12(uint64 a, uint64 b, uint64 c, uint64 d, uint64 e, uint64 f)
{
	return a*100000000000 + b*10000000000 + c*1000000000 + d*100000000 + e*10000000 + f*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome11(uint64 a, uint64 b, uint64 c, uint64 d, uint64 e, uint64 f)
{
	return a*10000000000 + b*1000000000 + c*100000000 + d*10000000 + e*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome10(uint64 a, uint64 b, uint64 c, uint64 d, uint64 e)
{
	return a*1000000000 + b*100000000 + c*10000000 + d*1000000 + e*100000 + e*10000 + d*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome9(uint64 a, uint64 b, uint64 c, uint64 d, uint64 e)
{
	return a*100000000 + b*10000000 + c*1000000 + d*100000 + e*10000 + d*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome8(uint64 a, uint64 b, uint64 c, uint64 d)
{
	return a*10000000 + b*1000000 + c*100000 + d*10000 + d*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome7(uint64 a, uint64 b, uint64 c, uint64 d)
{
	return a*1000000 + b*100000 + c*10000 + d*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome6(uint64 a, uint64 b, uint64 c)
{
	return a*100000 + b*10000 + c*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome5(uint64 a, uint64 b, uint64 c)
{
	return a*10000 + b*1000 + c*100 + b*10 + a;
}

inline uint64 palindrome4(uint64 a, uint64 b)
{
	return a*1000 + b*100 + b*10 + a;
}

inline uint64 palindrome3(uint64 a, uint64 b)
{
	return a*100 + b*10 + a;
}

inline uint64 palindrome2(uint64 a)
{
	return a*10 + a;
}

inline uint64 palindrome1(uint64 a)
{
	return a;
}

void fill_palindromes(vector<uint64>& p)
{
	for (uint64 a = 1; a <= 9; ++a)
	{
		p.push_back(palindrome1(a));
		p.push_back(palindrome2(a));
		for (uint64 b = 0; b <= 9; ++b)
		{
			p.push_back(palindrome3(a, b));
			p.push_back(palindrome4(a, b));
			for (uint64 c = 0; c <= 9; ++c)
			{
				p.push_back(palindrome5(a, b, c));
				p.push_back(palindrome6(a, b, c));
				for (uint64 d = 0; d <= 9; ++d)
				{
					p.push_back(palindrome7(a, b, c, d));
					p.push_back(palindrome8(a, b, c, d));
					for (uint64 e = 0; e <= 9; ++e)
					{
						p.push_back(palindrome9(a, b, c, d, e));
						p.push_back(palindrome10(a, b, c, d, e));
						for (uint64 f = 0; f <= 9; ++f)
						{
							p.push_back(palindrome11(a, b, c, d, e, f));
							p.push_back(palindrome12(a, b, c, d, e, f));
							for (uint64 g = 0; g <= 9; ++g)
							{
								p.push_back(palindrome13(a, b, c, d, e, f, g));
								p.push_back(palindrome14(a, b, c, d, e, f, g));
							}
						}
					}
				}
			}
		}
	}
}

size_t count_palindromes(vector<uint64>& p, unordered_set<uint64>& squares, uint64 A, uint64 B)
{
	size_t n = 0;
	vector<uint64>::const_iterator beg = lower_bound(p.begin(), p.end(), A);
	vector<uint64>::const_iterator end = upper_bound(p.begin(), p.end(), B);

	while (beg != end)
	{
		if (squares.find(*beg) != squares.end())
			++n;
		++beg;
	}

	return n;
}

int main()
{
	vector<uint64> p;
	p.reserve(20000000);
	fill_palindromes(p);
	sort(p.begin(), p.end());

	unordered_set<uint64> squares;
	for (size_t i = 0; i < p.size() && p[i] <= 10000000; ++i)
		squares.insert(p[i]*p[i]);

	size_t T = 0;
	cin >> T;
	for (size_t i = 0; i < T; ++i)
	{
		uint64 A = 0, B = 0;
		cin >> A >> B;
		cout << "Case #" << i+1 << ": " << count_palindromes(p, squares, A, B) << endl;
	}

	return 0;
}