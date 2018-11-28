#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

std::vector<std::string> SplitString (std::string line, char delimeter)
{
	std::vector<std::string> result;

	int delIndex;
	while ((delIndex = line.find (delimeter)) != std::string::npos)
	{
		result.push_back (line.substr (0, delIndex));
		line = line.substr (delIndex + 1);
	}

	result.push_back (line);
	return result;
}

double TotalProductivity (const size_t farms, const double F)
{
	return 2.0 + farms * F;
}

int main ()
{
	std::ifstream input ("B-large.in");
	std::ofstream output ("B-large.out");
	std::string line;
	getline (input, line);
	size_t n = atoi (line.c_str ());
		
	for (size_t t = 0; t < n; ++t)
	{
		getline (input, line);
		std::vector<std::string> sublines = SplitString (line, ' ');

		const double C = atof (sublines[0].c_str ());
		const double F = atof (sublines[1].c_str ());
		const double X = atof (sublines[2].c_str ());

		if (X <= C)
		{
			output << "Case #" << t + 1 << ": " << std::fixed << std::setprecision (7) << X/2 << std::endl;
			continue;
		}

		size_t farms = 0;
		double curTime = C / TotalProductivity (farms, F);
		double curCookies = C;

		while (curCookies < X)
		{
			double timeWithoutNewFarm = (X - curCookies) / TotalProductivity (farms, F);
			double timeWithNewFarm = X / TotalProductivity (farms + 1, F);
			if (timeWithoutNewFarm <= timeWithNewFarm)
			{
				curTime += timeWithoutNewFarm;
				break;
			}
			else
			{
				++farms;
				curCookies -= C;

				if (X - curCookies <= C)
				{
					curTime += (X - curCookies) / TotalProductivity (farms, F);
					break;
				}
				else
				{
					curTime += C / TotalProductivity (farms, F);
					curCookies += C;
				}
			}
		}

		output << "Case #" << t + 1 << ": " << std::fixed << std::setprecision (7) << curTime << std::endl;
	}

	input.close ();
	output.close ();
	return 0;
}