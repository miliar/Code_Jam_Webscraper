#include <iostream>
#include <cstdio>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>


using namespace std;

typedef vector<std::string> StringVector;


int main()
{
        long testCase,curTestCase;
    //cin >> testCase;
    std::string line;
    std::istringstream iss;

    ifstream myfile;
    myfile.open("input.txt",ios::in);

    ofstream outfile;
    outfile.open("out.txt");

    if (std::getline(myfile, line)) {
    iss.str(line);
    iss >> testCase;
    }

    //fscanf(fpt,"%ld\n",&testCase);
   // cout << testCase;
    for(curTestCase=0;curTestCase<testCase;curTestCase++)
    {

        long sMax;
        std::string strInput;

        //cin >> cursize;

        std::istringstream iss2;

        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss2.str(line);
            iss2 >> sMax;
            iss2 >> strInput;
            }
    //getchar();
   //int sMax = 0;
    //cout << sMax << " "<< strInput << endl;
    long lLength = strInput.length();
    int index;
    long counter = 0;

    long curVal = 0;
    for(index=0;index<lLength;index++)
    {

       curVal += strInput[index]- '1';
       if(curVal < 0)
       {
          counter += 1;
          curVal = 0;
       }
    }
    //cout << counter;
    outfile << "Case #"<<curTestCase+1<<": "<<counter<<endl;
    }

    return 0;
}
