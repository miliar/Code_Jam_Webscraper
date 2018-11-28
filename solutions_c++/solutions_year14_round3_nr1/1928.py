#include <fstream>
#include <iomanip>
#include <list>
#include <set>
#include <sstream>
#include <string>
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

	template<typename T>
	std::string toString(const T& value)
	{
		std::stringstream stream;
		stream << value;
		return stream.str();
	}

	struct CaseData
	{
		long long numerator;
		long long denominator;
	};

	struct ResultData
	{
		int generations;
	};

	CaseData readCaseData(std::istream& input)
	{
		CaseData data;

		std::string fraction;
		input >> fraction;

		int dividerIndex = fraction.find("/");

		std::stringstream numerator(fraction.substr(0, dividerIndex));
		numerator >> data.numerator;

		std::stringstream denominator(fraction.substr(dividerIndex + 1));
		denominator >> data.denominator;

		return data;
	}

	int calculate(const CaseData& data)
	{
		long long numerator = data.numerator;
		long long denominator = data.denominator;

		while (numerator > 1)
		{
			if (denominator % 2 != 0)
				return 0;

			numerator /= 2;
			denominator /= 2;
		}

		long long product = 2;
		for (int generation = 1; generation < 40; ++generation)
		{
			if (denominator == product)
				return generation;

			product *= 2;
		}

		return 0;
	}

	ResultData processData(const CaseData& data)
	{
		ResultData result;

		result.generations = calculate(data);

		return result;
	}

	std::string writeResultData(const ResultData& result)
	{
		if (result.generations == 0)
			return "impossible";

		return toString(result.generations);
	}
}

int main(int argc, char** argv)
{
	std::ifstream input("a.in");
	std::ofstream output("a.out");

	unsigned cases = getValue<unsigned>(input);

	for (unsigned caseIndex = 0; caseIndex < cases; ++caseIndex)
		output << "Case #" << caseIndex + 1 << ": " << writeResultData(processData(readCaseData(input))) << std::endl;

	input.close();
	output.close();

	return 0;
}

