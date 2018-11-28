// CoinJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <iterator>
#include <string>
#include <algorithm>
#include <cstdint>
#include <bitset>

const std::size_t primeCount = 32;
std::vector<uint32_t> prime;

uint32_t nextPrime(uint32_t v)
{
	for (v += 2; v < UINT32_MAX ; v += 2)
	{
		for (uint32_t n : prime)
		{
			if (v % n == 0)
				break;
			if (n > v / 2)
				return v;
		}
	}
	return 0;
}

uint32_t isPrime(uint64_t v)
{
	int min = 0;
	int max = (int)prime.size() - 1;
	while (min <= max)
	{
		const int mid = (min + max) / 2;
		uint32_t g = prime[mid];
		if (g > v)
			max = mid - 1;
		else if (g < v)
			min = mid + 1;
		else
			return 0;
	}

	for (uint32_t p : prime)
	{
		if (v % p == 0)
			return p;
	}

	//for (int i = 0; i < 1024; ++i)
	while (prime.size() < primeCount)
	{
		uint32_t p = nextPrime(prime.back());
		prime.push_back(p);

		if (v == p)
			return 0;
		if (v % p == 0)
			return p;
	}

	return 0;
}

uint64_t toBase(uint64_t v, uint32_t b)
{
	uint64_t vb = 0;
	for (int i = 31; i >= 0; --i)
	{
		vb *= b;
		vb += ((v >> i) & 1);
	}
	return vb;
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream file("D:/Dev/GoogleJam/CoinJam.in");

	//std::ostream& output = std::cout;
	std::ofstream outFile("D:/Dev/GoogleJam/CoinJam.out");
	std::ostream& output = outFile;

	unsigned int t;
	unsigned int n;
	unsigned int j;
	file >> t >> n >> j;

	prime.reserve(primeCount);
	prime.push_back(2);
	prime.push_back(3);

	output << "Case #1:" << std::endl;

	const uint64_t max = (UINT64_C(1) << n);
	for (uint64_t v = (UINT64_C(1) << (n - 1) | UINT64_C(1));
		v < max && j > 0;
		v += 2)
	{
		uint32_t divs[11];
		divs[2] = isPrime(v);
		if (divs[2] == 0)
			continue;
		bool next = false;
		for (uint32_t b = 3; b < 11; ++b)
		{
			divs[b] = isPrime(toBase(v, b));
			if (divs[b] == 0)
			{
				next = true;
				break;
			}
		}
		if (!next)
		{
			--j;
			for (int i = n - 1; i >= 0; --i)
			{
				output << ((v >> i) & 1);
			}
			for (uint32_t b = 2; b < 11; ++b)
				output << " " << divs[b];
			output << std::endl;
		}
	}

	return 0;
}

