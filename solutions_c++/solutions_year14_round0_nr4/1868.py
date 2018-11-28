#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>
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
        int battleRound = atoi(text[testNumber * 3 + 1].c_str());
        string buf;
        int warWin = 0;
        int dWarWin = 0;
        stringstream ss(text[testNumber * 3 + 2]);
        std::vector<double> naomiMass;
        while (ss >> buf)
        {
              naomiMass.push_back(atof(buf.c_str()));
        }
        stringstream ssk(text[testNumber * 3 + 3]);
        std::vector<double> kenMass;
        while (ssk >> buf)
        {
              kenMass.push_back(atof(buf.c_str()));
        }
        std::sort(naomiMass.begin(),naomiMass.end());
        std::sort(kenMass.begin(),kenMass.end());
        double minKen = kenMass[0];
        double maxKen = kenMass[battleRound - 1];
        for (int i = 0; i < battleRound; i++)
        {
            if(naomiMass[i] > minKen)
            {
                dWarWin++;
                minKen = kenMass[dWarWin];
            }            
        }
        for (int i = 0; i < battleRound; i++)
        {
            if(naomiMass[naomiMass.size() - 1] > kenMass[kenMass.size() - 1])
            {
                 warWin++;
                 naomiMass.pop_back();
                 kenMass.erase(kenMass.begin());
            }
            else
            {
                naomiMass.pop_back();
                for (int j = kenMass.size() - 2; j >= 0; j--)
                {
                    if (naomiMass[naomiMass.size() - 1] > kenMass[j])
                    {
                        kenMass.erase(kenMass.begin() + j + 1);
                        break;
                    }
                }
            }
        }
        outputFile << "Case #" << (testNumber + 1) <<  ": " << dWarWin << " " << warWin  << endl;
        ++testNumber;
    }
    outputFile.close();
    return 0;
}
