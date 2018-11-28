#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <fstream>
#include <cstdint>
#include <cmath>
#include <algorithm>
#include <map>
#include <iterator>
#include <numeric>

std::ofstream out;

typedef std::vector<size_t> Keys;

struct Chest
{
	size_t key;
	Keys inside;
};

typedef std::map<size_t, Chest> Chests;

struct Test
{
	Keys start;
	Chests chests;
	size_t maxKey;
	Test() : maxKey(0) {};
};

typedef std::vector<Test> Tests;

Tests readInput(const char* fn)
{
	std::ifstream ifs(fn);
	assert(ifs.is_open());


	size_t nTests;
	ifs >> nTests;

	Tests tests;

	for (int t = 0; t < nTests; ++t)
	{
		size_t nKeys, nChests;
		ifs >> nKeys >> nChests;

		Test test;
		for (int i = 0; i < nKeys; ++i)
		{
			size_t sk;
			ifs >> sk; 
			test.start.push_back(sk);
			test.maxKey = std::max(test.maxKey, sk);
		}

		for (size_t c = 0;  c < nChests; ++c)
		{
			Chest chest;
			size_t nInside;
			ifs >> chest.key >> nInside;
			for (size_t i = 0; i < nInside; ++i)
			{
				size_t keyInside;
				ifs >> keyInside;
				chest.inside.push_back(keyInside);
				test.maxKey = std::max(test.maxKey, keyInside);
			}
			test.chests[c + 1] = chest;
		}// end of chest cycle
		tests.push_back(test);

	} // end of test cycle
	return tests;
}

typedef std::vector<size_t> Order;
typedef std::vector<int> Hand;




bool preCheck(Hand hand, const Chests &chests)
{
	int sum = std::accumulate(hand.begin(), hand.end(), 0);
	if (sum <= 0)
		return false;


	int nLocked = 0;
	int nUnlocked = 0;

	for (Chests::const_iterator it  = chests.begin(), end = chests.end(); it != end; ++it)
	{
		const Chest &chest = it->second;
		size_t in = chest.inside.size();

		--hand[chest.key];
		
		if (in == 0)
			++nLocked;

		for (int i = 0; i < in; ++i)
		{
			++hand[chest.inside[i]];

			if ( in == 1 && chest.key == chest.inside[i] )
				++nLocked;
				
			/*
			if ( (in == 0) || (in == 1 && chest.key == chest.inside.front() ))
				++nLocked;
			else
				++nUnlocked;
			*/
		}
		

		
	}
	/*
	if (nLocked > sum + nUnlocked)
		return false;
	*/
	
	for (int i = 0; i < hand.size(); ++i)
		if (hand[i] < 0)
			return false;
	
	return true;
}

bool canBeeFreed(const Hand &hand, const Chests &chests, int k)
{
	for (Chests::const_iterator it  = chests.begin(), end = chests.end(); it != end; ++it)
	{
		int freed = 0;
		for (int i  = 0; i < it->second.inside.size(); ++i)
			if (it->second.inside[i] == k)
				++freed;
		if (it->second.key == k)
			--freed;
		if (freed > 0)
			return true;
	}
	return false;
}




bool canDrop(const Hand &hand, const Chests &chests)
{
	int n = 0;
	for (Chests::const_iterator it  = chests.begin(), end = chests.end(); it != end; ++it)
	{
		if (it->second.inside.size() == 0 && hand[it->second.key] == 1 && !canBeeFreed(hand, chests, it->second.key))
			++n;
	}

	int freed = 0;


	return n < chests.size();
}

bool canOpen(const Hand &hand, const Chests &chests, Chests::const_iterator k)
{
	//chests.erase(k);
	bool blocks = true;
	bool freed = false;

	for (Chests::const_iterator it  = chests.begin(), end = chests.end(); it != end; ++it)
	{
		if (it != k)
		{
			if (it->second.key == k->second.key)
				blocks &= false;
			size_t nFreed = std::count(it->second.inside.begin(), it->second.inside.end(), k->second.key);
			if (it->second.key == k->second.key)
				--nFreed;
			if (nFreed > 0)
				freed |= true;

		}
	}
	return blocks || freed;
}

Order open(const Hand &hand, const Chests &chests)
{
	size_t size = chests.size();

	assert(size);

	Order order;

	
	if (!preCheck(hand, chests))
		return order;
	
	if (size == 1)
	{
		if (hand[chests.begin()->second.key] > 0)
			order.push_back(chests.begin()->first);
	}
	else
	{
		for (Chests::const_iterator it  = chests.begin(), end = chests.end(); it != end; ++it)
		{
			const Chest &chest = it->second;
			size_t in = chest.inside.size();
			if (hand[chest.key] > 0)
			{
				if ( in == 0 && hand[chest.key] == 1 /*&& canDrop(hand, chests)*/ && !canOpen(hand, chests, it))
				{
					continue;
				}
				
				Hand leftHand = hand;
				Chests leftChests = chests;
				--leftHand[chest.key];
				for (int i = 0; i < in; ++i )
					++leftHand[chest.inside[i]];
				leftChests.erase(it->first);
								
				Order left = open(leftHand, leftChests);
				if (left.size() > 0)
				{
					order.push_back(it->first);
					order.insert(order.end(), left.begin(), left.end());
					break;
				}
			}
		}

	}

	return order;
}



Order solve(Test &test)
{
	assert(test.maxKey);
	Order order;

	Hand hand(test.maxKey + 1);
	for (int i = 0; i < test.start.size(); ++i)
		++hand[test.start[i]];

	return open(hand, test.chests);
}

int main(int argc, char *argv[])
{
	assert(argc > 1);

	std::string in = argv[1];

	out.open(in + ".out", std::ios_base::out | std::ios_base::trunc );

	Tests tests = readInput(in.c_str());

	for (int i = 0; i < tests.size(); ++i)
	{
		std::cout << i << std::endl;
		Order order = solve(tests[i]);
		out << "Case #" << i + 1 << ":";
		if (order.empty())
			out << " IMPOSSIBLE";
		else
			for (Order::const_iterator it = order.begin(), end = order.end(); it != end; ++it)
				out << ' ' << *it;
		out << std::endl;
	}


	return 0;
}