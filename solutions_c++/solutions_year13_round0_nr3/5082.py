
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <sstream>
using namespace std;

/*
 * 
 */
bool isPalindrome(int x)
{
    string s;
    ostringstream convert;
    convert << x;
    s = convert.str();
    int length = s.length();
    for (int i = 0;i<=length/2;i++)
    {
        if (s.at(i) != s.at(length-i-1)) return false;
    }
    return true;
}

int main(int argc, char** argv) {
    ifstream myFile;
    ofstream outFile;

    int n;
    int start,end;

    myFile.open("C-small-attempt0.in");
    //myFile.open("input.txt");
    outFile.open("output.txt");
    if (myFile.is_open())
    {
        myFile >> n;
        for (int q = 0;q < n;q++)
        {
            outFile << "Case #" << q+1 << ": ";
            int total = 0;
            myFile >> start;
            myFile >> end;

            double x = sqrt(start);
            int s = ceil(x);
            while(s*s <= end)
            {
                if ((isPalindrome(s))&&(isPalindrome(s*s)))
                {
                    total++;
                }
                s++;
            }
            outFile << total << endl;
        }
    }
    return (EXIT_SUCCESS);
}

