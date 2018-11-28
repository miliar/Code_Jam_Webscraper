#ifndef INPUT_PARSER_H
#define INPUT_PARSER_H
/**
 * @file
 * @brief Parsers the input file to obtain a list of GameBoard objects
 * @author Benjamyn
 */

#include <vector>
#include <fstream>

struct Interval {
	uint64_t lowerBound, upperBound;

	void printInterval() const;
};

/**
 * @brief An interface for objects that can be drawn
 */
class InputParser {
	private:
		std::vector<Interval> *intervals;

	public:
		InputParser();

		~InputParser();

		void parseInputFile(std::istream& instream);

		int getNumberDataSets() const;

		const Interval getDataSet(int i) const;
};

#endif
