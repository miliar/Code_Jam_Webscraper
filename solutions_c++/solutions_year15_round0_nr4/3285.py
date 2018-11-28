#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream inputFile("input.txt");
    ofstream outputFile("output.txt");
    int T;
    inputFile >> T;
    for (int nCase = 0; nCase < T; ++nCase)
    {
        int X;
        int R;
        int C;
        inputFile >> X;
        inputFile >> R;
        inputFile >> C;
        outputFile << "Case #" << (nCase + 1) << ": ";
        switch (X)
        {
            case 1:
                outputFile << "GABRIEL" << "\n";
                break;
            case 2:
                if (R*C % X != 0)
                {
                    outputFile << "RICHARD" << "\n";
                }
                else
                {
                    outputFile << "GABRIEL" << "\n";
                }
                break;
            case 3:
                if (R*C % X != 0 || R == 1 || C == 1)
                {
                    outputFile << "RICHARD" << "\n";
                }
                else
                {
                    outputFile << "GABRIEL" << "\n";
                }
                break;
            case 4:
                if (R*C % X != 0 || R <= 2 || C <= 2)
                {
                    outputFile << "RICHARD" << "\n";
                }
                else
                {
                    outputFile << "GABRIEL" << "\n";
                }
                break;
        }
    }
    return 0;
}
