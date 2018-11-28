#include <iostream>
#include <cstdio>
#include <ctime>
#include <string>
#include <iomanip>
#include <fstream>

long double findFastest(long double cost, long double cps, long double step, long double win, long double soFar)
{
	long double seconds, newSeconds, result;

	seconds = soFar + (win / cps);
	soFar += cost / cps;	
	newSeconds = soFar + (win / (cps + step));

	if(seconds < newSeconds)
	{
		return seconds;
	}
	else
	{
		seconds = findFastest(cost, (cps + step), step, win, soFar);
	}

	return seconds;
}

int main()
{
	std::ifstream file;
	file.open("B-small-attempt1.in");

	std::ofstream outputFile("output.txt");

	int i;
	file >> i;
	for(int j = 0; j < i; j++)
	{
		long double cookies = 0.0;
		long double cookiesPerSecond = 2.0;
		long double farmCost = 0.0;
		long double winCost = 0.0;
		long double farmCookiesPerSecond = 0.0;
		long double secondsElapsed = 0.0;
	
		file >> farmCost >> farmCookiesPerSecond >> winCost;
			
		secondsElapsed = findFastest(farmCost, cookiesPerSecond, farmCookiesPerSecond, winCost, 0);

		std::cout.setf(std::ios::fixed, std::ios::floatfield);
		
		outputFile << "Case #" << j + 1 << ": " << std::setprecision(7) << secondsElapsed << std::endl;
	}

	return 0;
}