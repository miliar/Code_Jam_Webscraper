// my second program in C++
#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;


int main ()
{

    //Declare the files
    ifstream inFile ;
    ofstream outFile ;

    //don't change these variables for gcj
    int numberOfCases;
    int currCase;

    //decalre the variables
    int arrayPos, currPos;
    int a[4],b[4],i;
    int numberofAns,hold;
    string instring;

    char inputFilename[] = "A-small-attempt2.in";
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
    //getline(inFile,instring);
    //Iterate over the number of cases
    for(currCase=1;currCase<numberOfCases+1;currCase++)
    {
         numberofAns = 0;
        //Get the array position
        inFile >> arrayPos;
        getline(inFile,instring);

        //Skip the lines until we get to the line we want
        for(currPos=1;currPos<arrayPos;currPos++)
        {
          getline(inFile,instring);
        }

        for( i = 0;i<4;i++)
        {
            inFile >> a[i];
        }
        //skip one more line
        getline(inFile,instring);

        //Skip the rest of the lines until we get to the second half of data
        for(currPos=arrayPos;currPos<4;currPos++)
        {
          getline(inFile,instring);
        }

        //Position of the second array
        inFile >> arrayPos;
        getline(inFile,instring);

        for(currPos=1;currPos<arrayPos;currPos++)
        {
          getline(inFile,instring);
        }

        for( i = 0;i<4;i++)
        {

            inFile >> b[i];
        }
        //skip one more line
        getline(inFile,instring);

        //Skip the rest of the lines until we get to the second half of data
        for(currPos=arrayPos;currPos<4;currPos++)
        {
          getline(inFile,instring);
        }

        //Next line
        for(int j = 0; j<4;j++)
        {
            for(int k = 0; k<4; k++)
            {
                    if(a[j]==b[k])
                        {
                        hold = k;
                        numberofAns++;
                        }
            }
        }


        outFile << "Case #" << currCase << ": ";
        switch(numberofAns)
        {
            case 0: outFile << "Volunteer cheated!" << endl; break;
            case 1: outFile << b[hold] << endl; break;
            default:outFile << "Bad magician!" << endl;
        }

}//End of this case

    //Close the files
    inFile.close(); outFile.close();


    return 0;
}

