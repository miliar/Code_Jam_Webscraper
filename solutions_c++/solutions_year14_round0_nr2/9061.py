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

fstream output ("1.out", ios::out|ios::trunc);
vector <string> input = getLines ("1.in");
output.precision (12);
if (input.size()==0) 
{
cerr << "Empty input!";
return 1;
}

unsigned T = atoi (input[0].c_str());

for (unsigned i = 0; i < T; ++i)
{
output << "Case #" << "  "<< ": ";

flt neededToBuy, farmOutput,winAmount;

vector<string> words = GetWordsFromLine (input[i+1]);

neededToBuy = strtod (words[0].c_str(), NULL);
farmOutput     = strtod (words[1].c_str(), NULL);
winAmount     = strtod (words[2].c_str(), NULL);

flt increment = 2.0; 
flt currentAmount = 0.0;

flt prevMinTime = winAmount/increment, minTime;
bool startup = true;
//cout << neededToBuy <<	"	"	<< farmOutput <<	"	" << winAmount<<"	"<<"\n";

flt totalTime = 0;

flt testTime = 0;

while (true)
{

	if (testTime+winAmount/increment> prevMinTime)
	{
		totalTime = prevMinTime;
		break;
	}
	else
	{
		prevMinTime = testTime+winAmount/increment;
	
   
	testTime += neededToBuy/increment;
increment+=farmOutput;
	}

   

}

output << "Case #"<<i+1<<": "<<totalTime<<"\n";

}




output.close();
std::cout << "DONE!";
cin.get();
}