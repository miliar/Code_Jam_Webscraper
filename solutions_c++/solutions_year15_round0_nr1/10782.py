#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main () {
  string line;
  ifstream input ("A-small-attempt1.in");
  ofstream output ("A-small-attempt1.out");

  if (input.is_open())
  {
	bool TestNumberNotSet = true;
	int NumberOfTests;
	int Shyness;
	long TotalStanding = 0;
	long PeopleNeeded = 0;
	int LineNumber = -1;
    while (getline(input,line))
    { 
		LineNumber ++;
		if(TestNumberNotSet)
		{
			istringstream(line) >> NumberOfTests;
			TestNumberNotSet = false;
		}
		else 
		{
			for(int i = 2; i < line.length(); i++)
			{
				Shyness = i-2;
				if(TotalStanding >= Shyness)
				{
					TotalStanding += (line[i] - 48);
				}
				else
				{
					PeopleNeeded += Shyness - TotalStanding;
					TotalStanding += (Shyness - TotalStanding) + (line[i] - 48);
				}
			}
			output << "Case #" << LineNumber << ": " << PeopleNeeded << endl;
			TotalStanding = 0;
			PeopleNeeded = 0;
		}
    }
  }
  input.close();
  output.close();
}