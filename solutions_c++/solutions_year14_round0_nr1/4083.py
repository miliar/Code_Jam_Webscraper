#include <fstream>
#include <iostream>
#include <string>

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

	void writeSolution(int caseNumber, const string &solution)
	{
		output << "Case #" + to_string(caseNumber) + ": " + solution +"\n";
	}
};
