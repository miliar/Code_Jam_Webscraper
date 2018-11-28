#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <typeinfo>
#include <conio.h>
#include <stdio.h>

#define getch() _getch()

using namespace std;

void main()
{
fstream myFile;
fstream Output;
int lineNo = -1;

int firstChoice;
int lastChoice;
int numberofcases = 1;

string presentLine;

int Layout1[4][4];
int Layout2[4][4];



myFile.open("read.in");
Output.open("output.txt");
while (getline(myFile, presentLine))
{
switch (lineNo)
{

case -1:
lineNo = 0;
continue;


case(0) :
istringstream(presentLine) >> firstChoice;
lineNo += 1;
for (int i = 0; i < 4; ++i)
{
myFile >> Layout1[0][i];
}
continue;

case(1) :
for (int i = 0; i < 4; ++i)
{
myFile >> Layout1[1][i];
}
lineNo += 1;
continue;

case(2) :
for (int i = 0; i < 4; i++)
{
myFile >> Layout1[2][i];
}
lineNo += 1;
continue;

case(3) :
for (int i = 0; i < 4; i++)
{
myFile >> Layout1[3][i];
}
lineNo += 1;
continue;

case(4) :
myFile >> lastChoice;
lineNo += 1;
cout << "\n";
continue;

case(5) :
for (int i = 0; i < 4; i++)
{
myFile >> Layout2[0][i];
}
lineNo += 1;
continue;


case(6) :
for (int i = 0; i < 4; i++)
{
myFile >> Layout2[1][i];
}
lineNo += 1;
continue;

case(7) :
for (int i = 0; i < 4; i++)
{
myFile >> Layout2[2][i];
}
lineNo += 1;
continue;

case(8) :
for (int i = 0; i < 4; i++)
{
myFile >> Layout2[3][i];
}
lineNo += 1;
continue;

case(9) :

int answers = -1;
int answerPos;

for (int m = 0; m < 4; m++)
{
for (int j = 0; j < 4; j++)
{
if (Layout1[firstChoice-1][m] == Layout2[lastChoice-1][j])
{
answerPos = j;
answers += 1;
}
}
}

if (answers == 0)
{
Output << "Case #" << numberofcases << ": " << Layout2[lastChoice - 1][answerPos] <<"\n";
numberofcases += 1;
}

if (answers > 0)
{
Output << "Case #" << numberofcases << ": " << "Bad magician!" << "\n";
numberofcases += 1;
}

if (answers < 0)
{
Output << "Case #" << numberofcases << ": " << "Volunteer cheated!" << "\n";
numberofcases += 1;
}

lineNo = 0;
cout << "\n";
continue;
}
}
myFile.close();

getch();
}

