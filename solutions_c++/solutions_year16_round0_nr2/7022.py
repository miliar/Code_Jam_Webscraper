// Google Code Start File
// By Beau V.
// Notes:
// 4/8/2016
// began about 12:20am after problem A

#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

const long READ_SIZE = 10000; // 100MB
const long WRITE_SIZE = 1000; // 1MB

void readFile(char *fileName, char fileContents[][READ_SIZE]);
void writeFile(char *fileName, char fileContents[][WRITE_SIZE], __int64 lines);

void printFileContents(char fileContents[][READ_SIZE], __int64 lines); // for testing
void printVector(vector<string> v); // for testing
void printVector(vector<__int64> v); // for testing

// a few common tricks
//std::sort(theVector.begin(), theVector.end());
//std::reverse(theVector.begin(), theVector.end());
vector<string> getStrings(const string& str, const char& token);
// create a string vector to int vector function

__int64 stringToInt(string s); // Beau's version
__int64 stoi(string s){return stringToInt(s);}
string intToString(__int64 i); // Beau's version
string itos(__int64 i){return intToString(i);}

__int64 solveTestCases(char fileContents[][READ_SIZE], char printContents[][WRITE_SIZE]);

// further function prototypes for solving

int main()
{
    static char input[READ_SIZE][READ_SIZE]; // looks like the input file wont be larger than what can fit in RAM
    char output[WRITE_SIZE][WRITE_SIZE];
    __int64 testCases;

    readFile("test.in", input);
    //printFileContents(input, 10);
    testCases = solveTestCases(input, output);
    cout << "there were " << testCases << " test cases" << endl;
    writeFile("output.txt", output, testCases);
    return 0;
}

void readFile(char *fileName, char fileContents[][READ_SIZE])
{
    ifstream inFile(fileName);
    if(inFile.fail())
    {
        cout << "could not load file" << endl;
    }

    for(__int64 i = 0; !inFile.eof(); i++)
    {
        inFile.getline(fileContents[i],READ_SIZE);
    }
    inFile.close();
}

void writeFile(char *fileName, char fileContents[][WRITE_SIZE], __int64 lines)
{
    ofstream outFile(fileName);
    if (outFile.is_open())
    {
        for(__int64 i = 0; i < lines; i++)
        {
            outFile.write(fileContents[i], strlen(fileContents[i]));
            outFile << "\n";
        }
        outFile.close();
    }
    else
    {
        cout << "could not save file" << endl;
    }
}

void printFileContents(char fileContents[][READ_SIZE], long lines)
{
    for(__int64 i = 0; i < lines; i++)
    {
        cout << fileContents[i] << endl;
    }
}

void printVector(vector<string> v)
{
    cout << "-vector contents begin-" << endl;
    for(__int64 i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }
    cout << "-vector contents end-" << endl;
}

void printVector(vector<__int64> v)
{
    cout << "-vector contents begin-" << endl;
    for(__int64 i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }
    cout << "-vector contents end-" << endl;
}

vector<string> getStrings(const string& str, const char& token)
{
    string next;
    vector<string> result;
    for (string::const_iterator it = str.begin(); it != str.end(); it++)
    {
        if (*it == token)
        {
            if (!next.empty())
            {
                result.push_back(next);
                next.clear();
            }
        }
        else
        {
            next += *it;
        }
    }
    if (!next.empty())
    {
        result.push_back(next);
    }
    return result;
}

__int64 stringToInt(string s)
{
    // could use atoi in multiple sections, see creditStringToInt in Beau's AddressInts 
    return _strtoi64(s.c_str(),NULL,0); // use in place of atoi()
    // read notes from last year telling myself to use strtoi64
}

string intToString(__int64 i)
{
    // could also split into multiple sections to construct the string using only %d
    string stringOfInt = "";
    char charsOfInt[50];
    sprintf_s(charsOfInt, "%lld", i); // %lld largely incompatiable
    return charsOfInt;
}

__int64 solveTestCases(char fileContents[][READ_SIZE], char printContents[][WRITE_SIZE])
{
    __int64 testCases = stoi(fileContents[0]);
    __int64 testCaseNumber = 1; // test case number

    // i starts at 1 so watch for memory allocation errors
    for(__int64 i = 1; i <= READ_SIZE; i++) // now i is an index
    {
        // load the test case

        // delimit strings in test case, for in files with multiple lines a test case use i++ here
        string cakeStack = fileContents[i];

        // did something with a vector here before



        // solve it, using OOP is not mandatory

        // combine the cakes
        __int64 combinedCount = 1;
        for(__int64 i = 0; i < cakeStack.length()-1; i++)
        {
            if(cakeStack[i] != cakeStack[i+1])
            {
                combinedCount++;
            }
        }

        __int64 minimalFlips = combinedCount;
        if(cakeStack[cakeStack.length()-1] == '+')
            minimalFlips--;



        // print it to print contents
        string solutionLine = "Case #";
        solutionLine += itos(testCaseNumber);
        solutionLine += ": ";
        solutionLine += itos(minimalFlips); // the solution value
        strcpy_s(printContents[testCaseNumber-1], solutionLine.c_str());

        // show what was added to printContents
        cout << solutionLine << endl;

        // dont add this to the for loop bool, other questions read multiple lines as input for a single test case
        testCaseNumber++;
        if(testCaseNumber > testCases)
        {
            break;
        }
    } // to the next test case
    return testCases;
}

// further functions for solving here

// notes while thinking
/*
+-+- <- topstack, bottomstack ->
[][]

]][]

[[[]

]]]]

[[[[ 4

-+-+
][][
[][[
]][[
[[[[ 3

--+-
]][]
[[[]
]]]]
[[[[3

any repeating sides may be treated as one pancake
leaving only combinations of +-+- and -+-+

--++--++
]][[]][[
[[]][[[[
]]]][[[[
[[[[[[[[ 3

+-+
[][
][[
[[[2

-+-
][]
[[]
]]]
[[[3

-+-+
][][
[][[
]][[
[[[[ 3

-+
][
[[1

+-
[]
]]
[[2

+-+-
...
4

processing in groups of 2 pancakes eliminating combos,
forming combinations of -+ and +-
such as -+-+, +-+, -+-, +-+-+-+-+-,

a - proceeding a + takes 2 moves if its not the first pancake
a - preceeding a + takes 1 move, rethinking...

the bottom cake is -
that takes 1 move
if there are 2 on top of that,
it must be the combination -+,
rethinking...

if the bottom combined cake is -
the minimal flips is the number of combined cakes
if the bottom cake is +
the minimal flips is the number of combined cakes - 1

i think this is it
*/
