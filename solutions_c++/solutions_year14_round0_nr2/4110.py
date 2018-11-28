#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

class OutputWriter
{
private:
	ofstream output;

public:
	OutputWriter(const string &file)
	{
		output.open(file);
	}

	~OutputWriter()
	{
		if (output.is_open())
		{
			output.close();
		}
	}

	void writeSolution(const int &caseNumber, const double &solution)
	{
		output << "Case #" << caseNumber << ": " << fixed << setprecision(7) << solution << "\n";
	}
};
