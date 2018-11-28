#include <fstream>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <ctime>
#include <algorithm>
#include <iomanip>

using namespace std;

string dirName = "Magic Trick\\";
string inpFileName = "asp.in";

string inputPath = "C:\\Users\\asjai\\Downloads\\cj\\" + dirName + inpFileName;
enum ANSCASE
{
	VALID,
	MAGICBAD,
	USERBAD
};


class OneCase
{
private:
	

	int firstRow;
	int firstMatrix[4][4];
	int secondRow;
	int secondMatrix[4][4];
	string const SMAGICBAD = "Bad magician!";
	string const SUSERBAD = "Volunteer cheated!";
	int result;
	ANSCASE ans;

public:
	OneCase()
	{
		ans = ANSCASE::VALID;
	}

	~OneCase()
	{
	}

	void readInput(ifstream& ifs);
	void evaluate();
	void putOutput(ofstream& ofs, int testNo);
};

void OneCase::readInput(ifstream& ifs)
{
	ifs >> firstRow;
	firstRow--;
	int i, j;

	i = 0, j = 0;
	while (i < 4)
	{
		j = 0;
		while (j < 4)
		{
			ifs >> firstMatrix[i][j];
			++j;
		}
		++i;
	}

	ifs >> secondRow;
	secondRow--;

	i = 0, j = 0;
	while (i < 4)
	{
		j = 0;
		while (j < 4)
		{
			ifs >> secondMatrix[i][j];
			++j;
		}
		++i;
	}
}

void OneCase::evaluate()
{
	bool matched = false;

	if (firstMatrix[firstRow][0] == secondMatrix[secondRow][0])
	{
		matched = true;
		result = firstMatrix[firstRow][0];
	}
	else if (firstMatrix[firstRow][0] == secondMatrix[secondRow][1])
	{
		matched = true;
		result = firstMatrix[firstRow][0];
	}
	else if (firstMatrix[firstRow][0] == secondMatrix[secondRow][2])
	{
		matched = true;
		result = firstMatrix[firstRow][0];
	}
	else if (firstMatrix[firstRow][0] == secondMatrix[secondRow][3])
	{
		matched = true;
		result = firstMatrix[firstRow][0];
	}

	if (firstMatrix[firstRow][1] == secondMatrix[secondRow][0])
	{
		if (matched)
		{
			ans = ANSCASE::MAGICBAD;
		}
		else
		{
			matched = true;
			result = firstMatrix[firstRow][1];
		}
	}
	else if (firstMatrix[firstRow][1] == secondMatrix[secondRow][1])
	{
		if (matched)
		{
			ans = ANSCASE::MAGICBAD;
		}
		else
		{
			matched = true;
			result = firstMatrix[firstRow][1];
		}
	}
	else if (firstMatrix[firstRow][1] == secondMatrix[secondRow][2])
	{
		if (matched)
		{
			ans = ANSCASE::MAGICBAD;
		}
		else
		{
			matched = true;
			result = firstMatrix[firstRow][1];
		}
	}
	else if (firstMatrix[firstRow][1] == secondMatrix[secondRow][3])
	{
		if (matched)
		{
			ans = ANSCASE::MAGICBAD;
		}
		else
		{
			matched = true;
			result = firstMatrix[firstRow][1];
		}
	}

	if (ans != ANSCASE::MAGICBAD)
	{
		if (firstMatrix[firstRow][2] == secondMatrix[secondRow][0])
		{
			if (matched)
			{
				ans = ANSCASE::MAGICBAD;
			}
			else
			{
				matched = true;
				result = firstMatrix[firstRow][2];
			}
		}
		else if (firstMatrix[firstRow][2] == secondMatrix[secondRow][1])
		{
			if (matched)
			{
				ans = ANSCASE::MAGICBAD;
			}
			else
			{
				matched = true;
				result = firstMatrix[firstRow][2];
			}
		}
		else if (firstMatrix[firstRow][2] == secondMatrix[secondRow][2])
		{
			if (matched)
			{
				ans = ANSCASE::MAGICBAD;
			}
			else
			{
				matched = true;
				result = firstMatrix[firstRow][2];
			}
		}
		else if (firstMatrix[firstRow][2] == secondMatrix[secondRow][3])
		{
			if (matched)
			{
				ans = ANSCASE::MAGICBAD;
			}
			else
			{
				matched = true;
				result = firstMatrix[firstRow][2];
			}
		}
	}

	if (ans != ANSCASE::MAGICBAD)
	{
		if (firstMatrix[firstRow][3] == secondMatrix[secondRow][0])
		{
			if (matched)
			{
				ans = ANSCASE::MAGICBAD;
			}
			else
			{
				matched = true;
				result = firstMatrix[firstRow][3];
			}
		}
		else if (firstMatrix[firstRow][3] == secondMatrix[secondRow][1])
		{
			if (matched)
			{
				ans = ANSCASE::MAGICBAD;
			}
			else
			{
				matched = true;
				result = firstMatrix[firstRow][3];
			}
		}
		else if (firstMatrix[firstRow][3] == secondMatrix[secondRow][2])
		{
			if (matched)
			{
				ans = ANSCASE::MAGICBAD;
			}
			else
			{
				matched = true;
				result = firstMatrix[firstRow][3];
			}
		}
		else if (firstMatrix[firstRow][3] == secondMatrix[secondRow][3])
		{
			if (matched)
			{
				ans = ANSCASE::MAGICBAD;
			}
			else
			{
				matched = true;
				result = firstMatrix[firstRow][3];
			}
		}
	}

	if (ans != ANSCASE::MAGICBAD && matched)
	{
		ans = ANSCASE::VALID;
		return;
	}
	else if (ans != ANSCASE::MAGICBAD)
	{
		ans = ANSCASE::USERBAD;
	}
}

void OneCase::putOutput(ofstream& ofs, int testNo)
{
	switch (ans)
	{
	case VALID:
		ofs << "Case #" << testNo << ": " << result;
		break;
	case MAGICBAD:
		ofs << "Case #" << testNo << ": " << SMAGICBAD.c_str();
		break;
	case USERBAD:
		ofs << "Case #" << testNo << ": " << SUSERBAD.c_str();
		break;
	}
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