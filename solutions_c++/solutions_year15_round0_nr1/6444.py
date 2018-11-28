#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<int> parseString(string str) {
    vector<int> result;
    for (int i = 0; i < str.length(); ++i)
    {
        string temp = str.substr(i, 1);
        result.push_back(atoi(temp.c_str()));
    }
    return result;
}

int main()
{
    int T;
    ifstream inputFile("input.txt");
    inputFile >> T;
    ofstream outputFile("output.txt");
    for (int nCase = 0; nCase < T; ++nCase)
    {
        int Smax;
        string data;
        inputFile >> Smax;
        inputFile >> data;
        vector<int> shns = parseString(data);
        int nInvite = 0;
        int nPeople = 0;
        for (int i = 0; i < shns.size(); i++)
        {
            if (nPeople >= i)
            {
                nPeople += shns[i];
            }
            else
            {
                nInvite += i - nPeople;
                nPeople += i - nPeople;
                nPeople += shns[i];
            }
        }
        outputFile << "Case #" << nCase+1 << ": " << nInvite << endl;
    }
    inputFile.close();
    outputFile.close();
    return 0;
}
        
