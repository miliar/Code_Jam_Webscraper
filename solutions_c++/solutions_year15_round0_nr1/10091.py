//
//  main.cpp
//  GoogleCodeJamQualificationRound
//
//  Created by Julia Tazin on 4/10/15.
//  Copyright (c) 2015 Julia Tazin. All rights reserved.
//

/*-----------------------------
 "Literature"
 http://www.cplusplus.com/reference/string/stoi/
 ----------------------------*/

/*-----------------------------
 Notes
 1) Everything is 0-indexed (except the case numbers in the output).
 
 a) Input usually has first n lines with meta information
 b) Several cases follow, each of which can span multiple lines
 
 3) Command line tool available for downloading/submitting.
 ----------------------------*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

/*-----------------------------
 Input/Output File Paths
 ----------------------------*/
const string pathToInputOutputDirectories = "/Users/Julia/Documents/Julia's Documents/Programming Projects/GoogleCodeJam/GoogleCodeJamQualificationRound/";
const string pathToInputDirectory = "GoogleCodeJamInputFiles/";
const string pathToOutputDirectory = "GoogleCodeJamOutputFiles/";

// TODO_1: Specify the problem identifier.
const string currentProblemIdentifier = "A-small-attempt2";

const string inputFileExtension = ".in";
const string outputFileExtension = ".out";

const string fullPathToInputFile = pathToInputOutputDirectories + pathToInputDirectory + currentProblemIdentifier + inputFileExtension;
const string fullPathToOutputFile = pathToInputOutputDirectories + pathToOutputDirectory + currentProblemIdentifier + outputFileExtension;

/*-----------------------------
 Globals
 ----------------------------*/

// TODO_?:
//const int maxInputSize = 100;

/*-----------------------------
 Helper Types
 ----------------------------*/

typedef enum _lineType
{
    intLine,
    intArrayLine,
    stringLine,
    stringArrayLine,
    charArrayLine,
    customLine
} lineType;

/*-----------------------------
 Input/Output Classes
 ----------------------------*/

class inputClass
{
public:
    int GetNumberOfCasesFromInputFile(ifstream &inputFile); // Generic*: Returns the number of cases in the file. *Used when the first line represents the number of cases only. *Must be called before any lines are read.
    void ReadCaseInputFromFile(ifstream &inputFile); // Semi-generic*: Given a file, will read a case and fill out the class variables. *Must be edited to contain class variable names.
    void* ParseLine(string &line, lineType lineType, int numberOfElementsInLine); // Generic*: Will parse a line according to its lineType. *Only supports a handful of speciic line types
    void CustomParseLine(string &line);
    string FindTheMeatOfTheProblem(); // Specific: Solves the problem. Bulk of the work is here. Returns a properly formatted string without the "Case #n: ".
    void FreeMemory(); // Semi-generic*: Frees class memory. *Need to specify which class variables must be freed and how.
    
    // TODO_2: How many lines per case?
    static const int numberOfLinesPerCase = 1;
    // TODO_3: What are the input line types?
    lineType inputLineTypes[numberOfLinesPerCase] = {customLine};
    
    // TODO_4: What class variables are needed? (Typically, a single input line corresponds to a class variable.)
    int maxShynessLevel; // Maximum shyness level
    int* numberOfPeoplePerShynessLevel; // Nnumber of people per shyness level (length of array is maxShynessLevel+1)
    
    
    // TODO_: Class variables not directly on an input line
};

class outputClass
{
public:
    void WriteCaseOutputToFile(ofstream &outputFile, int caseNumber, string output); // Generic: ????
    bool Test(string output);
    
    int outputCaseType = intArrayLine; // TODO: needed?
};

/*-----------------------------
 File Parsing
 ----------------------------*/
vector<string> &split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

vector<string> split(const std::string &s, char delim) {
    vector<string> elems;
    split(s, delim, elems);
    return elems;
}

int inputClass::GetNumberOfCasesFromInputFile(ifstream &inputFile)
{
    string line;
    if (getline(inputFile, line))
    {
        return stoi(line);
    }
    
    return -1;
}

void inputClass::ReadCaseInputFromFile(ifstream &inputFile)
{
    string line;
    int numberOfElementsInLine; // TODO: bad access when I make this int* :(
    // TODO_
    numberOfElementsInLine = -1;
    
    for (int i = 0; i < numberOfLinesPerCase; i++)
    {
        if (getline(inputFile, line))
        {
            lineType lineType = inputLineTypes[i];
            if (lineType == customLine)
            {
                CustomParseLine(line);
            }
            else
            {
                //void* returnVal = ParseLine(line, lineType, numberOfElementsInLine);
                switch (i)
                {
                    // TODO_5: Fill out the input class.
                    default:
                        break;
                }
            }
        }
    }
}

void* inputClass::ParseLine(string &line, lineType lineType, int numberOfElementsInLine)
{
    void* returnVal = NULL;
    
    switch(lineType)
    {
        case intLine:
            int returnIntVal;
            returnIntVal = stoi(line);
            returnVal = (void*)(&returnIntVal);
            break;
        case intArrayLine:
        {
            int* returnIntArrayVal;
            vector<string> splitLine;
            splitLine = split(line, ' ');
            int arrayLength = 0;
            if (numberOfElementsInLine > 0)
            {
                arrayLength = numberOfElementsInLine;
            }
            else
            {
                for (vector<string>::iterator str = splitLine.begin(); str != splitLine.end(); ++str) {
                    arrayLength++;
                }
//                numberOfStrings = arrayLength; // TODO: should return via numberOfElementsInLine*
            }
            returnIntArrayVal = new int[arrayLength]; // TODO: not ideal to be allocating like this for every case.
            int i = 0;
            for (vector<string>::iterator str = splitLine.begin(); str != splitLine.end(); ++str) {
                int intValue = stoi(*str);
                returnIntArrayVal[i] = intValue;
                i++;
            }
            returnVal = (void*)(&returnIntArrayVal);
        }
            break;
        case stringLine:
        {
            string returnStringVal;
            returnStringVal = line;
            returnVal = (void*)(&returnIntVal);
        }
            break;
        case stringArrayLine:
        {
            string* returnStringArrayVal;
            vector<string> splitLine;
            splitLine = split(line, ' ');
            int arrayLength = 0;
            if (numberOfElementsInLine > 0)
            {
                arrayLength = numberOfElementsInLine;
            }
            else
            {
                for (vector<string>::iterator str = splitLine.begin(); str != splitLine.end(); ++str) {
                    arrayLength++;
                }
//                numberOfStrings = arrayLength; // TODO: should return via numberOfElementsInLine*
            }
            returnStringArrayVal = new string[arrayLength]; // TODO: not ideal to be allocating like this for every case.
            int i = 0;
            for (vector<string>::iterator str = splitLine.begin(); str != splitLine.end(); ++str) {
                returnStringArrayVal[i] = *str;
                i++;
            }
            returnVal = (void*)(&returnStringArrayVal);
        }
            break;
        case charArrayLine:
            // TODO:
            break;
        default:
            // TODO: error?
            break;
    }
    return returnVal; // TODO: can't return reference of vector? return int**? easier to use for me...
}

void inputClass::CustomParseLine(string &line)
{
    // Get the two parts of the line.
    vector<string> splitLine;
    splitLine = split(line, ' ');
    
    maxShynessLevel = stoi(splitLine.at(0));
    string shynessLevelsString = splitLine.at(1);
    
    // Process the second part.
    //BIG INT
    int shynessLevelsStringBigInt = stoi(shynessLevelsString);
//    vector<string> splitLine2;
//    splitLine2 = split(shynessLevelsString, '\0'); // TODO: Will this split at char level?
    
    int* shynessLevelsArray;
    shynessLevelsArray = new int[maxShynessLevel + 1]; // +1 since there is a 0 shyness level.
    
    for (int i = maxShynessLevel; i >= 0; i--) {
        int singleShynessValue = shynessLevelsStringBigInt % 10;
        shynessLevelsArray[i] = singleShynessValue;
        shynessLevelsStringBigInt /= 10;
    }
    
    numberOfPeoplePerShynessLevel = shynessLevelsArray;
}

void inputClass::FreeMemory()
{
    // TODO_: Free memory for ....?
    ////    int* case
    //    delete[] itemPrices;
    //    itemPrices = NULL;
    
    //    string* case
    delete[] numberOfPeoplePerShynessLevel;
    numberOfPeoplePerShynessLevel = NULL;
}

void outputClass::WriteCaseOutputToFile(ofstream &outputFile, int caseNumber, string output)
{
    outputFile << "Case #" + to_string(caseNumber) + ": " + output + "\n";
}

/*-----------------------------
 The Meat of the Problem
 ----------------------------*/
string inputClass::FindTheMeatOfTheProblem()
{
    // TODO_: Solve the problem!
    string returnString;
    int* runningSumOfShyness = new int[maxShynessLevel + 1]; // runningSumOfShyness[i]  = number of people before that shyness level.
    
//    maxShynessLevel;
//    numberOfPeoplePerShynessLevel;
    
    runningSumOfShyness[0] = 0;
    int addedPeople = 0;
    
    for (int i = 1; i <= maxShynessLevel; i++)
    {
        runningSumOfShyness[i] = runningSumOfShyness[i - 1] + numberOfPeoplePerShynessLevel[i - 1];
        if ((numberOfPeoplePerShynessLevel[i] > 0) && ((runningSumOfShyness[i] + addedPeople) < i))
        {
            addedPeople += (i - (runningSumOfShyness[i] + addedPeople));
        }
    }
    
    returnString = to_string(addedPeople);
    
    return returnString;
}

/*-----------------------------
 Main
 ----------------------------*/

void MainAlgorithm()
{
    inputClass inputObject;
    outputClass outputObject;
    
    // Open input file and get number of cases.
    ifstream inputFile;
    inputFile.open(fullPathToInputFile);
    int numberOfCases = inputObject.GetNumberOfCasesFromInputFile(inputFile);
    
    // Prepare output file.
    ofstream outputFile;
    outputFile.open(fullPathToOutputFile);
    
    // For each set of data, compute the answer.
    for (int i = 0; i < numberOfCases; i++)
    {
        // Read case from the file.
        inputObject.ReadCaseInputFromFile(inputFile);
        
        // Run algorithm on set of data.
        string output = inputObject.FindTheMeatOfTheProblem();
        
//        // Test output.
//        outputObject.Test(output);
        
        // Write output results for set to file.
        outputObject.WriteCaseOutputToFile(outputFile, i + 1, output);
        
        inputObject.FreeMemory();
    }
    
    inputFile.close();
    outputFile.close();
}

int main(int argc, const char * argv[])
{
    cout << "Hello, World!\n";
    
    MainAlgorithm();
    
    return 0;
}

