#include <iostream>
#include <vector>
#include <algorithm>
#include<boost/lexical_cast.hpp>

struct Output
{
	unsigned additionalFriends = 0;
};

void resolve(std::vector<Output>& output) {
	Output o;
	unsigned maximumShynessLevel;
	std::string shynessLevel;

	std::cin >> maximumShynessLevel;
	std::cin >> shynessLevel;

	unsigned counter = 0;

	for (unsigned i = 0; i <= maximumShynessLevel; ++i)
	{
		while (counter < i) {
			++o.additionalFriends;
			++counter;
		}

		unsigned convertedShy = boost::lexical_cast<unsigned>(shynessLevel[i]);
		counter += convertedShy;
	}

	output.push_back(o);
}

int main(int argc, char const *argv[])
{
	std::vector<Output> output;
	unsigned testCases;

	std::cin >> testCases;

	for (unsigned i = 0; i < testCases; ++i) {
		resolve(output);
	}

	for (unsigned i = 0; i < testCases; ++i) {
		std::cout << "Case #" << (i+1) << ": " << output[i].additionalFriends << std::endl;
	}

	return 0;
}