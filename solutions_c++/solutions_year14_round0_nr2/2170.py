#include <fstream>
#include <iostream>
#include <iomanip>

template<typename T>
T getValue(std::istream& input)
{
	T value;
	input >> value;
	return value;
}

struct CookieData
{
	double c;
	double f;
	double x;
};

CookieData readCookieData(std::istream& input)
{
	CookieData data;

	data.c = getValue<double>(input);
	data.f = getValue<double>(input);
	data.x = getValue<double>(input);

	return data;
}

double calculateOptimalProductionTime(const CookieData& cookieData)
{
	unsigned factoryCount = 0;

	double rate = 2;
	double accumulatedTime = 0;
	double lastProductionTime = cookieData.x / rate;
	while (true)
	{
		double nextRate = rate + cookieData.f;
		if (cookieData.x / nextRate + cookieData.c / rate > lastProductionTime)
		{
			return accumulatedTime + lastProductionTime;
		}

		lastProductionTime = cookieData.x / nextRate;
		accumulatedTime += cookieData.c / rate;
		rate = nextRate;
		++factoryCount;
	}
}

int main(int argc, char** argv)
{
	std::ifstream input("b.in");
	std::ofstream output("b.out");

	unsigned cases = getValue<unsigned>(input);

	for (unsigned caseIndex = 0; caseIndex < cases; ++caseIndex)
		output << "Case #" << caseIndex + 1 << ": " << std::fixed << std::setprecision(8) << calculateOptimalProductionTime(readCookieData(input)) << std::endl;

	return 0;
}

