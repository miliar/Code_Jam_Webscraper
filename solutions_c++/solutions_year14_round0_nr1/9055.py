#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdio>
#include <stdlib.h>
#include <algorithm>

//#include "ttmath/ttmath.h"


using namespace std;

//typedef ttmath::Big<2,5> BigNumber;
typedef unsigned long long number;

typedef long double flt;

vector<string> getLines (const char path [])
{
fstream file (path, ios::in);

if (!file)
{
cout << "Error opening " << path;
return vector<string>(0);
}


string temp;
vector<string> output;

while (getline (file, temp))
{
output.push_back (temp);
}

return output;
}




vector<string> GetWordsFromLine (const string& line)
{
vector<string> out (0);

unsigned lastSpace = 0;

for (unsigned i = 0; i < line.size(); i++)
{
   if (line[i] == ' ' || i == line.size()-1)
   {
       if (i == line.size()-1) i++;
       string word = line.substr(lastSpace, i-lastSpace);
       if (word.size()!=0) out.push_back (word);
       lastSpace = i+1;
   }
}
if (out.size()!=0) return out;
else return vector<string>(1,"ERROR");
}



int main ()
{
cout.precision (12);

fstream output ("3.out", ios::out|ios::trunc);
vector <string> input = getLines ("3.in");
output.precision (12);
if (input.size()==0) 
{
cerr << "Empty input!";
return 1;
}

unsigned T = atoi (input[0].c_str());

for (unsigned i = 0; i < T; ++i)
{
	int firstAnswer = atoi (input[i*10+1].c_str())-1;
	int firstSet [4][4];
	//cerr <<firstAnswer<<"	";
	
	for (unsigned j = 0; j < 4; ++j)
		sscanf (input[i*10+2+j].c_str(), "%i %i %i %i", &firstSet[j][0], &firstSet[j][1], &firstSet[j][2], &firstSet[j][3]);
		
		int secondAnswer = atoi (input[i*10+6].c_str())-1;
	
	int secondSet[4][4];
	
	for (unsigned j = 0; j < 4; ++j)
		sscanf (input[i*10+7+j].c_str(), "%i %i %i %i", &secondSet[j][0], &secondSet[j][1], &secondSet[j][2], &secondSet[j][3]);
		
		//Done getting input!
		unsigned numberMatches = 0;
		int answer = 0;
		
		
		for (unsigned x = 0; x < 4; ++x)
		for (unsigned y = 0; y < 4; ++y)
			{
				if (firstSet[firstAnswer][x] == secondSet[secondAnswer][y])
				{
					numberMatches++;
					answer = firstSet[firstAnswer][x];
				}
			}
			
			output << "Case #"	<< i+1 << ": ";
			
			if (numberMatches > 1)
			{
				output << "Bad magician!\n";
			}
			else if (numberMatches == 0)
			{
				output << "Volunteer cheated!\n";
			}
			else output << answer <<	"\n";
		
}



output.close();
std::cout << "DONE!";
cin.get();
}