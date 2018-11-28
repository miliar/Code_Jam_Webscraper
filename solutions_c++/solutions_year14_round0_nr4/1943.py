#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <set>
#include <string>
#include <sstream>
#include <vector>

namespace
{
	template<typename T>
	T getValue(std::istream& input)
	{
		T value;
		input >> value;
		return value;
	}
}

struct War
{
	std::vector<double> naomi;
	std::vector<double> ken;
};

War readWar(std::istream& input)
{
	unsigned blockCount = getValue<unsigned>(input);

	War war;

	std::list<double> naomi;
	std::list<double> ken;
	for (unsigned index = 0; index < blockCount; ++index)
		naomi.push_back(getValue<double>(input));
	for (unsigned index = 0; index < blockCount; ++index)
		ken.push_back(getValue<double>(input));

	naomi.sort();
	ken.sort();

	war.naomi.assign(naomi.begin(), naomi.end());
	war.ken.assign(ken.begin(), ken.end());

	return war;
}

unsigned calculateDeceitful(const War& war)
{
	unsigned deceitfulLosses = 0;

	size_t naomiBottom = 0;
	size_t naomiIndex = war.naomi.size();
	size_t kenIndex = war.ken.size();

	while (naomiIndex > naomiBottom)
	{
		if (war.naomi[naomiIndex - 1] > war.ken[kenIndex - 1])
		{
			--naomiIndex;
		}
		else
		{
			++deceitfulLosses;
			++naomiBottom;
		}
		--kenIndex;
	}

	return war.naomi.size() - deceitfulLosses;
}

unsigned calculateHonest(const War& war)
{
	unsigned honestWins = 0;

	size_t naomiIndex = 0;
	size_t kenIndex = 0;

	while (naomiIndex < war.naomi.size())
	{
		while (kenIndex < war.ken.size() && war.ken[kenIndex] < war.naomi[naomiIndex])
			++kenIndex;

		if (kenIndex >= war.ken.size())
			++honestWins;

		++naomiIndex;
		++kenIndex;
	}

	return honestWins;
}

int main(int argc, char** argv)
{
	std::ifstream input("d.in");
	std::ofstream output("d.out");

	unsigned cases = getValue<unsigned>(input);

	for (unsigned caseIndex = 0; caseIndex < cases; ++caseIndex)
	{
		War war = readWar(input);
		output << "Case #" << caseIndex + 1 << ": " << calculateDeceitful(war) << " " << calculateHonest(war) << std::endl;
	}

	return 0;
}

