#include <fstream>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <ctime>
#include <algorithm>
#include <iomanip>

using namespace std;

const float EPSILON = 0.00001;

string dirName = "Deceitful War\\";
string inpFileName = "odlp.in";

string inputPath = "C:\\Users\\asjai\\Downloads\\cj\\" + dirName + inpFileName;

int compare(const void* a, const void* b)
{
	if (*(float*)a > *(float*)b)
		return 1;
	if (*(float*)a == *(float*)b)
		return 0;
	return -1;
}

class OneCase
{
private:
	int NumberOfBlocks;
	float Naomi[1000];
	float Ken[1000];
	int NaomiWon;
	int NaomiWonDeceitfully;
public:
	OneCase()
	{
		NaomiWonDeceitfully = 0;
		NaomiWon = 0;
	}

	~OneCase()
	{
	}

	void readInput(ifstream& ifs);
	void evaluate();
	void putOutput(ofstream& ofs, int testNo);
	int FindLowestKenIndex(float val, int high, int low);
	//void CalDeceitFullWins();
};

void OneCase::readInput(ifstream& ifs)
{
	ifs >> NumberOfBlocks;

	int i = 0;
	while (i < NumberOfBlocks)
	{
		ifs >> Naomi[i++];
	}

	i = 0;
	while (i < NumberOfBlocks)
	{
		ifs >> Ken[i++];
	}
}

void OneCase::evaluate()
{
	qsort(Naomi, NumberOfBlocks, sizeof(float), compare);
	qsort(Ken, NumberOfBlocks, sizeof(float), compare);

	int i = 0;
	float kenCopy[1000];
	while (i < NumberOfBlocks)
	{
		kenCopy[i] = Ken[i];
		++i;
	}

	i = 0;
	while (i < NumberOfBlocks)
	{
		bool kWon = false;
		for (int j = 0; j < NumberOfBlocks; j++)
		{
			if (kenCopy[j] > Naomi[i])
			{
				kenCopy[j] = 0;
				kWon = true;
				break;
			}
		}
		if (!kWon)
			NaomiWon++;
		i++;
	}

	/*
	i = 0;
	while (i < NumberOfBlocks)
	{
		cout << Naomi[i++] << " ";
	}
	cout << endl;

	i = 0;
	while (i < NumberOfBlocks)
	{
		cout << Ken[i++] << " ";
	}
	cout << endl;
	*/

	NaomiWonDeceitfully = NumberOfBlocks;
	i = 0;
	int j = 0;
	while (i < NumberOfBlocks)
	{
		if (Naomi[i] < Ken[j])
		{
			NaomiWonDeceitfully--;
			j--;
		}
		i++;
		j++;
	}

	//CalDeceitFullWins();
}

void OneCase::putOutput(ofstream& ofs, int testNo)
{
	ofs << "Case #" << testNo << ": " << NaomiWonDeceitfully << " " << NaomiWon;
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