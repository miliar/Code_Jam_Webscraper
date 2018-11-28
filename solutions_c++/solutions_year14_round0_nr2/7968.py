// my second program in C++
#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;

//double farmTime(double farmCost, double farmRate, int farmNum){
//if(farmNum==0)
//    {return 0.0;}
//else
//    return farmCost/(2.0+farmRate*farmNum) + farmTime(farmCost,farmRate,farmNum--);
//
//return 0.0;
//}

int main ()
{

    //Declare the files
    ifstream inFile ;
    ofstream outFile ;
    outFile.precision(7);
    outFile.setf(ios::fixed);
    outFile.setf(ios::showpoint);
    //don't change these variables for gcj
    int numberOfCases;
    int currCase;

    //decalre the variables
    string instring;
    //Dem floats
    double C,F,X,PROB,POSS,hold;
    //Number of farms to try
    int N;
    char inputFilename[] = "B-large.in";
    char outputFilename[] = "output.out";

    //No error checking here!
    inFile.open(inputFilename, ios::in);

    if (!inFile) {
      cerr << "Can't open input file " << inputFilename << endl;
      exit(1);
    }

    outFile.open(outputFilename, ios::out);

    if (!outFile) {
      cerr << "Can't open output file " << outputFilename << endl;
      exit(2);
    }

    inFile >> numberOfCases;
    //Iterate over the number of cases
    for(currCase=1;currCase<numberOfCases+1;currCase++)
    {
        inFile>>C>>F>>X;
    N = 0.0;
    hold=0.0;
    POSS = X/2;

    do{
    PROB=POSS;
    N++;
        hold=hold+C/(2+(N-1)*F);


    POSS = X/(2.0+F*N) + hold;

    }while(POSS<PROB);


    outFile << "Case #" << currCase << ": " << PROB << endl;

    }//End of this case

    //Close the files
    inFile.close(); outFile.close();


    return 0;
}

