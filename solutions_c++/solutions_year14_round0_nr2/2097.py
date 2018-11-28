#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
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
    bool end = false;
    while (testNumber < caseNumber)
    {
        end = false;
        string arg[3];
        stringstream ss(text[testNumber +1]);
        string buf;
        int index = 0;
        while (ss >> buf)
        {
             arg[index] = buf;
             index++;      
        }
        double cost = atof(arg[0].c_str());
        double add = atof(arg[1].c_str()); 
        double target = atof(arg[2].c_str());
        double time = 0.0f;
        double actualAdd = 2.0f;
        while (!end)
        {
             double plainTime = target / actualAdd;
             double buildTime = (cost / actualAdd) + (target / (actualAdd + add));
             if(plainTime < buildTime)
             {
                          time += plainTime;
                          end = true;
             }
             else
             {
                          time += cost / actualAdd;
                          actualAdd += add;
             }
        }
        outputFile << "Case #" << (testNumber + 1) <<  ": " << setiosflags(ios::fixed)<< setprecision(7) << time << endl;
        ++testNumber;
    }
    outputFile.close();
    return 0;
}
