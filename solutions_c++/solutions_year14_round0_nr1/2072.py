#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
int main()
{
    int caseNumber;
    int lineNumber = 0;
    int index = 0;
    string text[100000];
    string line;
    ifstream myfile("input.txt");
    ofstream outputFile("output.txt");
    if(myfile.is_open())
    {
        while(getline(myfile, line))
        {
            text[index] = line;
            index++;
        } 
    }
    myfile.close();
    caseNumber = atoi(text[0].c_str());
    int testNumber = 0;
    while (testNumber < caseNumber)
    {
        int startRowNumber;
        int endRowNumber;
        string startRow[4];
        string endRow[4];
        int solutionNumber = 0;
        int solution;
        startRowNumber = atoi(text[testNumber * 10 + 1].c_str());
    
            
        endRowNumber = atoi(text[testNumber * 10 + 6].c_str());
        int prevNumber[4][4];
        int afterNumber[4][4];
        for (int i = 0; i < 4; i++)
        {
            string buf;
            stringstream ss(text[testNumber * 10 + 2 + i]);
            int index = 0;
            while (ss >> buf)
            {
                  startRow[index] = buf;
                  index++;
            }
            index = 0;
            stringstream ssend(text[testNumber * 10 + 7 + i]);
            while (ssend >> buf)
            {
                  endRow[index] = buf;
                  index++;
            }
            for (int j = 0; j < 4; j++)
            {
                prevNumber[i][j] = atoi(startRow[j].c_str());
                afterNumber[i][j] = atoi(endRow[j].c_str());
            }
        }

 
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if(prevNumber[startRowNumber - 1][i] == afterNumber[endRowNumber - 1][j])
                {
                   solutionNumber++;
                   solution = prevNumber[startRowNumber - 1][i];
                }
            }
        }
        if (solutionNumber == 1)
        {
            outputFile << "Case #" << (testNumber + 1) << ": "  << solution << endl;
        }
        else if (solutionNumber == 0)
        {
            outputFile << "Case #" << (testNumber + 1) <<  ": " << "Volunteer cheated!" << endl;
        }
        else
        {
            outputFile << "Case #" << (testNumber + 1) <<  ": " << "Bad magician!" << endl;
        }
        ++testNumber;
    }
    outputFile.close();
    return 0;
}
