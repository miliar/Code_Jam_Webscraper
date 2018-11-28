/*
* C++11 code template for contests.
* @author: Andrey Kalendarov
* @e-mail: andreykalendarov@gmail.com
*/

/*______ DEFINES _______*/

#define _SCL_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
//#define ANDREIKKAA_TOPCODER
#define ANDREIKKAA_ALLOCATOR
//#define ANDREIKKAA_UNSAFE_VECTOR

#define ANDREIKKAA_CLASS Solution
#define ANDREIKKAA_METHOD solve
#define ANDREIKKAA_PARAMETERS void
#define ANDREIKKAA_CALL
#define ANDREIKKAA_RETURN_TYPE void

#ifdef ANDREIKKAA_UNSAFE_VECTOR
#define vec vector
#endif // ANDREIKKAA_UNSAFE_VECTOR

typedef long long ll;
typedef long double ld;

const int MEMORY_LIMIT_MB = 500;
const int TIME_LIMIT_S = 1;

const char input_filename[] =
#ifdef ANDREIKKAA
"input.txt"
#else
""
#endif
;
const char output_filename[] =
#ifdef ANDREIKKAA
"lol.txt"
#else
""
#endif
;

/* ______ INCLUDES ______ */

#include <cassert>
#include <ciso646>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <ctgmath>
#include <array>
#include <bitset>
#include <deque>
#include <forward_list>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <complex>
#include <functional>
#include <initializer_list>
#include <iterator>
#include <limits>
#include <locale>
#include <numeric>
#include <regex>
#include <string>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

/* _____ ALLOCATION _____ */

#ifdef ANDREIKKAA_ALLOCATOR
char alloc_memory[MEMORY_LIMIT_MB * 1000 * 1000];
size_t alloc_pointer = 0;
inline void* operator new(size_t x)
{
	alloc_pointer += x;
return alloc_memory + alloc_pointer - x;
}
inline void operator delete(void*)
{

}
#endif

/*_______ TYPES ________*/

#ifndef ANDREIKKAA_UNSAFE_VECTOR
template<typename T>
class vec : public vector<T>
{
public:
	using vector<T>::vector;
	inline const T operator[](size_t x) const
	{
		return this->at(x);
	}
	inline T& operator[](size_t x)
	{
		return this->at(x);
	}
};

template<>
class vec<bool> : public vector<bool>
{
	using vector<bool>::vector;
public:
	inline const_reference operator[](size_t x) const
	{
		return this->at(x);
	}
	inline reference operator[](size_t x)
	{
		return this->at(x);
	}
};
#endif // !ANDREIKKAA_UNSAFE_VECTOR

/*____ I-O OPERATORS ____*/

template<typename T, typename U>
inline ostream &operator<<(ostream &out, const pair<T, U> &p)
{
	out << p.first << ' ' << p.second;
	return out;
}

template<typename T, typename U>
inline istream &operator>>(istream &in, pair<T, U> &p)
{
	in >> p.first >> p.second;
	return in;
}

#ifndef ANDREIKKAA_UNSAFE_VECTOR
template<typename T>
inline ostream &operator<<(ostream &out, const vec<T> &v)
{
	if (v.empty())
		return out;
	out << v.front();
	for (auto it = ++v.begin(); it != v.end(); ++it)
		out << ' ' << *it;
	return out;
}

template<typename T>
inline istream &operator>>(istream &in, vec<T> &v)
{
	for (auto &i : v)
		in >> i;
	return in;
}
#endif // !ANDREIKKAA_UNSAFE_VECTOR

template<typename T>
inline ostream &operator<<(ostream &out, const vector<T> &v)
{
	if (v.empty())
		return out;
	out << v.front();
	for (auto it = ++v.begin(); it != v.end(); ++it)
		out << ' ' << *it;
	return out;
}

template<typename T>
inline istream &operator>>(istream &in, vector<T> &v)
{
	for (auto &i : v)
		in >> i;
	return in;
}

/* _______ INPUT _________*/

class Reader
{
public:
	inline Reader(const string &filename)
	{
		cin.tie(nullptr);
		ios_base::sync_with_stdio(false);
		if (not filename.empty())
			assert(freopen(filename.c_str(), "r", stdin) != nullptr);
	}

	template<typename T>
	inline void operator()(T &x)
	{
		cin >> x;
	}

	template<typename T, typename... Args>
	inline void operator()(T &x, Args &... args)
	{
		operator()(x), operator()(args...);
	}
};
Reader rd(input_filename);

/* _______ OUTPUT ________*/

class Printer
{
public:
	inline Printer(const string &filename)
	{
		//cout.precision(20);
		//cout << fixed;
		if (not filename.empty())
			assert(freopen(filename.c_str(), "w", stdout) != nullptr);
	}

	template<typename T>
	inline void out(const T x)
	{
		cout << x;
	}

	template<typename T, typename... Args>
	inline void out(const T x, const Args... args)
	{
		out(x), out(args...);
	}

	inline void operator()()
	{
		out('\n');
	}

	template<typename T>
	inline void operator()(const T x)
	{
		out(x), out('\n');
	}

	template<typename T, typename... Args>
	inline void operator()(const T x, const Args... args)
	{
		out(x), out(' '), operator()(args...);
	};
};
Printer pr(output_filename);

/* ________ CODE ________ */

void f()
{
	int n;
	rd(n);
	vec<string> v(n, string(n, ' '));
	rd(v);

	int msk = 0;
	for (int i = n - 1; i >= 0; --i)
	{
		for (int j = n - 1; j >= 0; --j)
		{
			msk <<= 1;
			msk |= (v[i][j] == '1');
		}
	}

	int cur[4][4];
	int gl_ans = 228;
	for (int i = 0; i < (1 << (n * n)); ++i)
	{
		int cst = 0;
		for (int j = 0; j < n * n; ++j)
		{
			cur[j / n][j % n] = ((i >> j) & 1);
			if ((i >> j) & 1)
			{
				if ((msk >> j) & 1)
				{
					continue;
				}
				else
				{
					++cst;
				}
			}
			else
			{
				if ((msk >> j) & 1)
				{
					cst = 228;
					break;
				}
				else
				{
					continue;
				}
			}
		}
		if (cst == 228)
			continue;

		vec<int> peop(n);
		iota(peop.begin(), peop.end(), 0);
		vec<int> mach(n);
		iota(mach.begin(), mach.end(), 0);
		do
		{
			do
			{
				bool badtest = false;

				vec<bool> used(n);
				for (int i = 0; i < n; ++i)
				{
					if (not cur[peop[i]][mach[i]] or used[mach[i]])
					{
						for (int j = 0; j < n; ++j)
						{
							if (cur[peop[i]][j] and not used[j])
							{
								badtest = true;
								break;
							}
						}
						if (!badtest)
						{
							goto hui;
						}
						break;
					}
					else
					{
						used[mach[i]] = true;
					}
				}
			} while (next_permutation(mach.begin(), mach.end()));
		} while (next_permutation(peop.begin(), peop.end()));
		gl_ans = min(gl_ans, cst);
		hui:;
	}
	pr(gl_ans);
}

ANDREIKKAA_RETURN_TYPE mainFunction(ANDREIKKAA_PARAMETERS)
{
	int t;
	rd(t);

	for (int i = 1; i <= t; ++i)
	{
		cerr << i << endl;
		pr.out("Case #", i, ": ");
		f();
	}
}

class ANDREIKKAA_CLASS
{
public:
	ANDREIKKAA_RETURN_TYPE ANDREIKKAA_METHOD(ANDREIKKAA_PARAMETERS) { return mainFunction(ANDREIKKAA_CALL); }
#ifdef ANDREIKKAA
	ANDREIKKAA_CLASS() { _start = clock(); }
	~ANDREIKKAA_CLASS() { /*cerr << "Time: " << (clock() - _start) / (ld)CLOCKS_PER_SEC << endl;*/ }
private:
	time_t _start;
#endif
};

#if defined(ANDREIKKAA) || !defined(ANDREIKKAA_TOPCODER)
int main()
{
	auto _s = new ANDREIKKAA_CLASS;
	_s->ANDREIKKAA_METHOD(ANDREIKKAA_CALL);
	delete _s;
#ifdef ANDREIKKAA
#ifdef _WIN32
	while (true);
#endif // _WIN32
#endif // ANDREIKKAA
}
#endif