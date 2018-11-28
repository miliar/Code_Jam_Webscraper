#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include "math.h"

using namespace std ;

bool palCheck (int x) ;

int main()
{

    //Area for holding global variables
    int testCases ;
    int runs = 0 ;

    //Code used to input the file for testing
    ifstream inputFile ;
    string filename ;

    cout << "What is the name of the inputfile?: " ;
    getline(cin,filename) ;
    cout << endl ;
    inputFile.open(filename.c_str()) ;

    //Code used to write out the correpsonding file
    ofstream outputFile ;

    cout << "What would you like to name the output file?: " ;
    getline(cin,filename) ;
    cout << endl ;
    outputFile.open(filename.c_str()) ;

    inputFile >> testCases ;

    while (runs < testCases)
    {
        int low ;
        int high ;

        inputFile >> low ;
        inputFile >> high ;
        int fsNum = 0 ;

        for (int i = low ; i <= high ; i++)
        {
            bool fs = false ;
            int sqr = sqrt(i) ;

            if ((sqr * sqr) == i)
            {
               if (palCheck(i))
               {
                   fs = palCheck(sqr) ;
               }

            }

            if (fs)
            {
               fsNum ++ ;
            }
        }

        outputFile << "Case #" << (runs + 1) << ": " << fsNum << endl ;
        runs ++ ;
    }
    inputFile.close() ;
    outputFile.close() ;
    return 0 ;
}

bool palCheck (int x)
{
    ostringstream y ;
    y << x ;
    string z = y.str() ;
    int start = 0 ;
    int end = (z.length() - 1) ;
    bool result = true ;

    while (start <= end && result)
    {
        if(z[start] != z[end])
        {
            result = false ;
        }

        start ++ ;
        end = end - start ;
    }

    return result ;
}
