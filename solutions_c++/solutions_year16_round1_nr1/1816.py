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

std::string func(std::string strInput)
{
      std::string strOut = strInput.substr(0,1);

      long len = strInput.length();
      long index;
      for(index=1;index<len;index++)
      {
          if(strInput[index] >= strOut[0])
          {
              strOut = strInput[index] + strOut;
          }
          else
            strOut += strInput[index];
      }
      return strOut;
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


    std::string res;
    res = func(strInput);
    outfile << "Case #"<<curTestCase+1<<": "<<res<<endl;

    //cout << res << endl;
    }

   return 0;
}
