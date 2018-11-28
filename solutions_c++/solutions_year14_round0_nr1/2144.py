#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <sstream>

unsigned getValue(std::istream& input)
{
	unsigned value;
	input >> value;
	return value;
}

struct CardSet
{
	unsigned rows[4][4];
};

CardSet getCardSet(std::istream& input)
{
	CardSet cardSet;

	for (size_t rowIndex = 0; rowIndex < 4; ++rowIndex)
		for (size_t columnIndex = 0; columnIndex < 4; ++columnIndex)
			cardSet.rows[rowIndex][columnIndex] = getValue(input);

	return cardSet;
}

std::string toString(const unsigned value)
{
	std::stringstream stream;
	stream << value;
	return stream.str();
}

std::string findCard(const unsigned row1, const CardSet& cardSet1, const unsigned row2, const CardSet& cardSet2)
{
	std::set<unsigned> possibles;
	for (unsigned columnIndex1 = 0; columnIndex1 < 4; ++columnIndex1)
		possibles.insert(cardSet1.rows[row1 - 1][columnIndex1]);

	unsigned value = 0;
	unsigned count = 0;
	for (unsigned columnIndex2 = 0; columnIndex2 < 4; ++columnIndex2)
	{
		std::set<unsigned>::iterator possible = possibles.find(cardSet2.rows[row2 - 1][columnIndex2]);
		if (possible != possibles.end())
		{
			++count;
			value = *possible;
		}
	}

	switch (count)
	{
	case 0:
		return "Volunteer cheated!";
	case 1:
		return toString(value);
	default:
		return "Bad magician!";
	}
}

int main(int argc, char** argv)
{
	std::ifstream input("a.in");
	std::ofstream output("a.out");

	unsigned cases = getValue(input);

	for (unsigned caseIndex = 0; caseIndex < cases; ++caseIndex)
	{
		unsigned row1 = getValue(input);
		CardSet cardSet1 = getCardSet(input);
		unsigned row2 = getValue(input);
		CardSet cardSet2 = getCardSet(input);

		output << "Case #" << caseIndex + 1 << ": " << findCard(row1, cardSet1, row2, cardSet2).c_str() << std::endl;
	}

	return 0;
}

