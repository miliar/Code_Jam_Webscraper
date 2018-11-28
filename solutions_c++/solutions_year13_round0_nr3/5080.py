#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string>

std::ifstream input;
std::ofstream output;

long long begin, end, result;
inline bool IsPalindrom(long long& in)
{
	std::string s = std::to_string(in);
	int beginS = 0;
	int endS = s.size() - 1;
	bool isWork = true;
	bool isResult = true;
	while(isWork)
	{
		if(s[beginS] != s[endS])
			return false;
		beginS++;
		endS--;
		if(beginS >= endS)
			return true;

	}
}


inline bool IsKvadrat(long long& in)
{
	long long koren = (long long)sqrt((long double)in);
	if(koren * koren != in)
		return false;
	return IsPalindrom(koren);
}

inline void CountGoodNumbers()
{
	result = 0;
	for(long long i=begin; i <= end; i++)
	{
		if(IsPalindrom(i) && IsKvadrat(i))
			result++;
	}
}

int main()
{
	input.open("task.in");
	output.open("taskResult.out");
	int countCases;
	input >> countCases;
	printf("%d\n",countCases);

	for(int i=0; i < countCases; i++)
	{
		input >> begin >> end;

		CountGoodNumbers();

		output << "Case #" << i + 1 << ": " << result << "\n";
	}
	input.close();
	output.flush();
	output.close();
   return 0;
}