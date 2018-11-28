#pragma once
#include <vector>
#include <set>
#include <map>

// boost library is used to handle the prime numbers
// ver: 1.60.0
// url: www.boost.org

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/miller_rabin.hpp>

template <typename NumType>
class PrimeBuffer
{
	std::set<NumType> primes;
	NumType lastCheckedNum;
public:
	PrimeBuffer()
	{
		generate(65537);
	}
	bool isPrime(const NumType& num)
	{
		if (hasDivisor(num))
			return false;
		/*
		if (num > lastCheckedNum)
		{
			generate(num);
		}

		return primes.find(num) != primes.end();
		*/
		return true;
	}

	void generate(const NumType& to)
	{		
		std::cout << "generating primes to: " << to << std::endl;
		boost::random::mt19937 gen(clock());

		NumType start = lastCheckedNum + 1;
		for (start; start <= to; start++)
		{
			if (boost::multiprecision::miller_rabin_test(start, 25, gen))
			{
				//if (boost::multiprecision::miller_rabin_test((start - 1) / 2, 25, gen))
				{
					primes.insert(start);
				}
			}
		}

		lastCheckedNum = to;
		std::cout << "generating primes done!" << std::endl;
	}
	
	bool hasDivisor(const NumType& num)
	{
		auto it = primes.cbegin();
		while (primes.cend() != it)
		{
			if (num < (*it))
			{
				break;
			}

			if ((num % *(it)) == 0)
				return num != (*it);
			++it;
		}		
		return false;
	}

	NumType getDivisor(const NumType& num)
	{
		auto it = primes.cbegin();
		while (primes.cend() != it)
		{
			if (num < (*it))
			{
				break;
			}

			if ((num % *(it)) == 0)
				return (*it);
			++it;
		}
		std::cout << num << "!!!!!!############ ERROR ###########!!!!!!!!!!!" << std::endl;
		return 0;
	}

};


class JamCoin
{	
public:
	typedef boost::multiprecision::cpp_int ResultNum;
	typedef int JamCoinNum;
	
private:
	PrimeBuffer<ResultNum> primes;


	void calcBases(const std::string& jamcoin, std::vector<ResultNum>& bases);

	std::string nextJamCoin(const int size, char* buff, const int& last);

public:

	std::map< std::string, std::vector<ResultNum> > result;

	void process(const unsigned int N, const unsigned int J);
};


extern void JamCoin_Start(std::string);
