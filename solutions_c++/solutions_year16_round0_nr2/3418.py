#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <functional>
#include <iterator>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <vector>
#include <cmath>

typedef unsigned long long int ulli;
typedef   signed long long int slli;
const ulli MAX_ULLI = 0xFFFFFFFFFFFFFFFF;
const ulli MIN_ULLI = 0x0000000000000000;
const slli MAX_SLLI = 0x7FFFFFFFFFFFFFFF;
const slli MIN_SLLI = 0x8000000000000000;
const ulli MOD = 1e9 + 7;

#ifdef __USE_REAL__
typedef long double real;
const real MATH_PI =  3.141592653589793238462643383279502884197169399375105820974944;
const real MATH_E  =  2.718281828459045235360287471352662497757247093699959574966967;
const real eps = 1e-14;
#endif /* __USE_REAL__ */

#ifdef __DEBUG__
template<typename T>
const std::function<T(T)> IdentityFunction = [](const T& v){ return v; };

template<typename T, typename U=T>
std::string to_string(
	const std::list<T> &l, 
	std::function<U(T)> conv = IdentityFunction<T>,
	const std::string delim = ","
)
{
	std::stringstream ss;
	auto itr = l.begin();
	while(itr != l.end())
	{
		ss << conv(*itr);
		++itr;
		if(itr != l.end()) ss << delim;
	}
	return ss.str();
}

template<typename T>
std::ostream& operator<<(std::ostream &os, const std::list<T> &l)
{
	os << to_string(l);
	return os;
}

template<typename T, typename U=T>
std::string to_string(
	const std::vector<T> &v, 
	std::function<U(T)> conv = IdentityFunction<T>,
	const std::string delim = ","
)
{
	std::stringstream ss;
	for(ulli i=0; i<v.size(); ++i)
	{
		ss << conv(v[i]);
		if((i + 1) < v.size()) ss << delim;
	}
	return ss.str();
}

template<typename T>
std::ostream& operator<<(std::ostream &os, const std::vector<T> &v)
{
	os << to_string(v);
	return os;
}

template<typename T, typename U=T>
std::string to_string(
	const std::set<T> &s, 
	std::function<U(T)> conv = IdentityFunction<T>,
	const std::string delim = ","
)
{
	std::stringstream ss;
	auto itr = s.begin();
	while(itr != s.end())
	{
		ss << conv(*itr);
		++itr;
		if(itr != s.end()) ss << delim;
	}
	return ss.str();
}

template<typename T>
std::ostream& operator<<(std::ostream &os, const std::set<T> &s)
{
	os << to_string(s);
	return os;
}
#endif /* __DEBUG__ */

template<typename T, class InputIterator>
inline bool have(
	InputIterator first, 
	InputIterator last, 
	const T &val
)
{
	return std::find(first, last, val) != last;
}

template<class InputIterator, class UnaryPred>
inline bool have_if(
	InputIterator first, 
	InputIterator last, 
	UnaryPred pred
)
{
	return std::find_if(first, last, pred) != last;
}

long solve(const std::string &S)
{
	std::bitset<100> bs(0);
	
	const std::string::size_type N = S.size();
	for(std::string::size_type i=0; i<N; ++i)
	{
		bs[i] = (S[(N-1)-i] == '+') ? 1 : 0;
	}
	
	unsigned C = 0;
	for(unsigned i=0; i<N; ++i)
	{
		if(bs[0] == 0) { bs.flip(); ++C; }
		bs >>= 1;
	}
	return C;
}

int main()
{
	unsigned T;
	std::cin >> T;
	
	for(unsigned t=0; t<T; ++t)
	{
		std::string S;
		std::cin >> S;
		
		std::cout << "Case #" << (t + 1) << ": ";
		std::cout << solve(S) << std::endl;
	}
	
	return 0;
}