#include <fstream>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <ctime>
#include <algorithm>
#include <iomanip>

using namespace std;

string dirName = "Cookie Clicker\\";
string inpFileName = "bsp.in";

string inputPath = "C:\\Users\\asjai\\Downloads\\cj\\" + dirName + inpFileName;

class OneCase
{
private:
	long double InitFlow;
	long double CostOfFarm;
	long double ExtraPoints;
	long double TargetX;
	long double TotalTime;
public:
	OneCase()
	{
		InitFlow = 2.0;
		TotalTime = 0.0;
	}

	~OneCase()
	{
	}

	void readInput(ifstream& ifs);
	void evaluate();
	void putOutput(ofstream& ofs, int testNo);
	long double Time2TargetWithFlow(long double currentFlow);
};

void OneCase::readInput(ifstream& ifs)
{
	ifs >> CostOfFarm;
	ifs >> ExtraPoints;
	ifs >> TargetX;
}

long double OneCase::Time2TargetWithFlow(long double currentFlow)
{
	long double timeReqToBuyFarm = CostOfFarm / currentFlow;
	long double time2Target = TargetX / currentFlow;

	long double minTime;
	long double expectedTime = min(time2Target, timeReqToBuyFarm + TargetX / (currentFlow + ExtraPoints));

	if ((expectedTime == time2Target) || (time2Target <= timeReqToBuyFarm))
	{
		minTime = time2Target;
	}
	else
	{
		minTime = min(time2Target, timeReqToBuyFarm + Time2TargetWithFlow(currentFlow + ExtraPoints));
	}

	return minTime;
}

void OneCase::evaluate()
{
	TotalTime = Time2TargetWithFlow(InitFlow);
}

void OneCase::putOutput(ofstream& ofs, int testNo)
{
	ofs << "Case #" << testNo << ": " << TotalTime;
}

int main()
{
	int totalCase = 0;
	std::string outputPath = inputPath + "_result";

	std::ifstream ifs;
	std::ofstream ofs;

	ifs.open(inputPath, ifstream::in);
	ifs >> totalCase;

	//	char* dummy = new char[L];
	//	ifs.getline(dummy, L);

	ofs.open(outputPath, ofstream::out);
	ofs << std::fixed;
	ofs.precision(7);

	int i = 1;
	while (i <= totalCase)
	{
		clock_t start_t = clock();
		if (i > 1) ofs << endl;
		OneCase object;
		object.readInput(ifs);
		object.evaluate();
		object.putOutput(ofs, i);
		clock_t stop_t = clock();
		cout << "For Case #" << i << " time taken is " << (stop_t - start_t) / CLOCKS_PER_SEC << endl;
		++i;
	}

	std::cout << outputPath.c_str();
	getchar();

	ifs.close();
	ofs.close();

	return 0;
}