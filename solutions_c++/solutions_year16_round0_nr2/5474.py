#include <iostream>
#include <cstdio>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

typedef vector<long> LongVector;

long func(std::string strInput)
{
    long len = strInput.length();

    long index;

    char prevChar = strInput[0];
    // write for 1 len TODO
    if(strInput.length() == 1)
    {
        if(strInput[0] == '+')
            return 0;
        else
            return 1;
    }

    std::string strNew;
    strNew = prevChar;
    for(index = 1;index<len;index++)
          {
            char curChar = strInput[index];
            if(curChar != prevChar)
            {
                strNew += curChar;
                prevChar = curChar;
            }

          }

    //cout << strNew << endl;
    long newLen = strNew.length();
    if(strNew[newLen-1] == '+')
        return newLen-1;
    else
        return newLen;

}

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

        std::string strInput;
        //cin >> cursize;

        std::istringstream iss2;

        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss2.str(line);
            iss2 >> strInput;

        //    cout << "Cursize "<< cursize << endl;
            }


    long res = 0;
    res = func(strInput);
    outfile << "Case #"<<curTestCase+1<<": "<<res<<endl;

    //cout << res << endl;
    }

   return 0;
}
