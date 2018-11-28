#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <vector>
using namespace std;

string GetSelectedRow(ifstream &inputFile);
void RunTest(string strRow1, string strRow2, int testCase);
void Tokenize(string& str, vector<int>& tokens);

int main(int argc, char** argv)
{
    if(argc != 2)
    {
        cout << "Usage: executable <filename>" << endl;
        return 0;
    }

    ifstream inputFile;
    inputFile.open(argv[1]);

    string line;
    int nTestCases = 0;

    if(inputFile.is_open())
    {
        getline(inputFile, line);
        nTestCases = atoi(line.c_str());
        for(int i=0; i<nTestCases; i++)
        {
            string strRow1 = GetSelectedRow(inputFile);
            string strRow2 = GetSelectedRow(inputFile);

            RunTest(strRow1, strRow2, i+1);
        }
    }

    return 0;
}

void Tokenize(string& str, vector<int>& tokens)
{
    string::size_type lastPos = str.find_first_not_of(" ", 0);
    string::size_type pos     = str.find_first_of(" ", lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        tokens.push_back(atoi(str.substr(lastPos, pos - lastPos).c_str()));
        lastPos = str.find_first_not_of(" ", pos);
        pos = str.find_first_of(" ", lastPos);
    }
}

string GetSelectedRow(ifstream &inputFile)
{
    string line;
    string selectedLine;
    if(inputFile.is_open())
    {
        getline(inputFile, line);
        int row = atoi(line.c_str());
        for(int i=0; i<4; i++)
        {
            getline(inputFile, line);
            if(row == i+1)
                selectedLine = line;
        }
        return selectedLine;
    }
    return NULL;
}


void RunTest(string strRow1, string strRow2, int testCase)
{
    vector<int> nRow1;
    vector<int> nRow2;

    //cout << "Selected String : " << strRow1 << endl;
    Tokenize(strRow1, nRow1);
    //cout << "Selected String : " << strRow2 << endl;
    Tokenize(strRow2, nRow2);

    bool foundMoreThanOne = false;
    bool foundOnlyOne = false;
    bool foundNone = true;
    int selectedCard = 0;

    for(int k=0; k<4; k++)
    {
        //cout << nRow1[k] << endl;
        for(int l=0; l<4; l++)
        {
            //cout << nRow2[l] << " ";
            if(nRow1[k] == nRow2[l])
            {
                selectedCard = nRow1[k];
                foundNone = false;
                if(foundOnlyOne)
                    foundMoreThanOne = true;
                foundOnlyOne = true;
            }
        }
        //cout << endl;
    }

    if(foundNone)
        cout << "Case #" << testCase << ": " << "Volunteer cheated!" << endl;

    else if(foundMoreThanOne)
        cout << "Case #" << testCase << ": " << "Bad magician!" << endl;

    else
        cout << "Case #" << testCase << ": " << selectedCard << endl;
}
