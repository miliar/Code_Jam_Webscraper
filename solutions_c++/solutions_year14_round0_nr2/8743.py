// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>

int main(int argc, char* argv[])
{
	int testCases = 0;
	
	long double farmPrice, farmGenerate, neededCookie, generateSum, maxTime, myCookies;
	long double timeSum;

	std::string tmpLine = "";
	std::string choiceLine = "";

	std::ifstream myfile("input.txt", std::ios::in);
	std::ofstream outFile("output.txt", std::ios::out);

	if (myfile.is_open() && outFile.is_open())
	{
		getline(myfile, tmpLine);
		testCases = stoi(tmpLine);

		for (int i = 0; i < testCases; i++)
		{
			timeSum = 0;
			generateSum = 2;
			myCookies = 0;
			getline(myfile, tmpLine);
	
			std::istringstream ss(tmpLine);

			std::string x;        // here's a nice, empty string
			getline(ss, x, ' ');  // try to read the next field into it
			farmPrice = stod(x);

			getline(ss, x, ' ');  // try to read the next field into it
			farmGenerate = stod(x);

			getline(ss, x, ' ');  // try to read the next field into it
		    neededCookie = stod(x);

			maxTime = neededCookie / 2;

			bool done = false;
			while (!done)
			{
				long double timeToGetFarm = farmPrice / generateSum;
				long double timeToReachNeededOld = neededCookie / generateSum;
				long double justSomeTime = (neededCookie - farmPrice) / generateSum;
				long double timeToReachNeededNew = ((neededCookie) / (generateSum+farmGenerate)) + timeToGetFarm;

				//std::cout << std::setprecision(16) << "current time: " << timeSum << "\n";
				if (timeToReachNeededNew < timeToReachNeededOld)
				{
					timeSum += timeToGetFarm;
					generateSum += farmGenerate;
				}
				else
				{
					timeSum += timeToReachNeededOld;
					done = true;
					std::cout << std::setprecision(13) << std::left << std::setfill('0') << "got cookie: " << timeSum << "\n";
					outFile << std::setprecision(13) << std::left << std::setfill('0') << "Case #" << (i + 1) << ": " << timeSum << "\n";
				}
			}
		}

		myfile.close();
		outFile.close();
	}
	else std::cout << "Unable to open file";

	//std::cin.get();
	return 0;
}