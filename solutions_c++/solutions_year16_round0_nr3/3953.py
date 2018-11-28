#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <utility>
#include <bitset>

typedef uint32_t u32;
typedef int64_t i64;
typedef uint64_t u64;

namespace mik {

class sieve // heap rulz
{
public:
//  	static u32 const MAX = 960525907U;
//  	static u32 const SQRT = 30992U;

	static u32 const MAX = 9605259U;
 	static u32 const SQRT = 3100U;


	typedef std::vector<std::pair<u64, double> > primes;

	static sieve const & get()
	{
		if (!instance)
			instance = new sieve();
		return *instance;
	}

	inline bool is_prime(u64 n) const
	{
		if (n < MAX)
		{
			return s.test(n);
		}
		else
		{
			for (u32 i = 2; i < MAX; ++i)
				if (s.test(i) && 0 == n % i)
					return false;
			u32 const to = static_cast<u32>(sqrt(n));
			for (u32 i = MAX; i < to; i += 2) // paratlantu indujj (maxtol fugg, maxvaltasnal figyuzzad)
				if (0 == n % i)
					return false;
			return true;
		}
	}

	u32 get_divisor(u64 num) const
	{
		for (u64 i = 2; i < SQRT; ++i)
			if (s.test(i) && 0 == num % i)
				return i;
		return 0;
	}

	primes const & get_primes() const { return v; }

private:
	sieve()
	{
		v.reserve(static_cast<u64>(MAX / log(MAX - 1)));
		s.set();
		s.reset(0).reset(1).set(2);
		v.push_back(std::make_pair(2, log(static_cast<double>(2))));
		for (u32 i = 4; i < MAX; i += 2)
			s.reset(i);

		for (u32 i = 3; i < MAX; i += 2)
			if (s.test(i))
			{
				v.push_back(std::make_pair(i, log(static_cast<double>(i))));
				for (u32 j = i*i; j < MAX; j += i)
					s.reset(j);
			}
	}

	sieve(sieve const &);
	sieve & operator=(sieve const &) const;

	static sieve * instance;

	std::bitset<MAX> s;
	primes v;
};
sieve * sieve::instance = 0;
} // namespace mik

u64 conv(std::string const & num, u32 base)
{
	u64 res = 0;
	u64 pwr = 1;
	for (auto i = num.rbegin(); i != num.rend(); ++i, pwr *= base)
		res += (*i - '0') * pwr;
	return res;
}

int main()
{
	using namespace std;

	ifstream in("c.in");
	ofstream out("c.out");

	u32 T;
	in >> T;

	mik::sieve const & s = mik::sieve::get();
	cout << "sieve ready" << endl;

	for (u32 i = 0; i < T; ++i)
	{
		out << "Case #" << (i + 1) << ":" << endl;
		u32 N, J;
		in >> N >> J;

		// 6 db egyes
		string s6("1111100000000001");
		auto end = s6.begin();
		advance(end, s6.size() - 1);
		sort(s6.begin() + 1, end);

		u32 count = 0;
		do
		{
			u64 const n8 = conv(s6, 8);
			u64 const n6 = conv(s6, 6);
			u64 const n2 = conv(s6, 2);
			if (!s.is_prime(n8) && !s.is_prime(n6) && !s.is_prime(n2))
			{
				u32 const d2 = s.get_divisor(n2);
				u32 const d6 = s.get_divisor(n6);				
				u32 const d8 = s.get_divisor(n8);

				if (d2 && d6 && d8)
				{
					out << s6 << " " << d2 << " 2 3 2 " << d6 << " 2 " << d8 << " 2 3" << endl;
					++count;
				}
			}
		}
		while (count < J && next_permutation(s6.begin() + 1, end));
	}
	
	getchar();
	return 0;
}
