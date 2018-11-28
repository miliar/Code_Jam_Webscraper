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

	void writeSolution(int caseNumber, const int &war, const int &deceit)
	{
		output << "Case #" << caseNumber << ": " << war << " " << deceit << "\n";
	}
};
