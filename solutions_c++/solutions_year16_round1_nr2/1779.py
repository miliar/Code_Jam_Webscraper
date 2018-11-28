#include <iostream>
#include <cstdio>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <numeric>

using namespace std;

typedef vector<long> LongVector;


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

        long input[2501];
        long in;
        for(in=0;in<2501;in++)
            input[in] = 0;

        LongVector vecInput;
        std::string strInput;
        //cin >> cursize;
        long curLenN;
        std::istringstream iss2;

        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss2.str(line);
            iss2 >> curLenN;

        //    cout << "Cursize "<< cursize << endl;
            }


        //std::istringstream iss2;
        long index2;
       for(index2=0;index2<2*curLenN-1;index2++)
       {
        std::string strOneline;
        std::istringstream iss3;

        if (std::getline(myfile, line))
            {
            iss3.str(line);
            //iss3 >> testCase;
            }


       // iss3 >> strOneline;

                long index3;
               for(index3=0;index3<curLenN;index3++)
               {
                   long curVal;
                   iss3 >>  curVal;
                   vecInput.push_back(curVal);
                    input[curVal] += 1;
               }

       }

/*
    std::string res;
    long index4;
    for(index4=0;index4<curLenN*(2*curLenN-1);index4++)
    {
        cout << vecInput[index4] << endl ;
    }
    */
    LongVector vecOut;
      for(in=0;in<2501;in++)
            {
                if(input[in] %2 == 1)
                {

                    vecOut.push_back(in);
                }

            }
    //res = func(vecInput);
    std::string strOutput;
    long in5;
    for(in5=0;in5<vecOut.size();in5++)
        {
             ostringstream oss;
            oss << vecOut[in5];
            strOutput +=  oss.str(); //std::to_string(vecOut[in5]);
            if(in5 != vecOut.size()-1)
                strOutput += " ";
        }
    outfile << "Case #"<<curTestCase+1<<": "<<strOutput<<endl;

    //cout << res << endl;
    }

   return 0;
}
