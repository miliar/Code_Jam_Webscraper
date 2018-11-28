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

int checkAll(int arr[10])
{
    long index2 = 0;
    for(index2=0;index2<10;index2++)
    {
        if(arr[index2] == 0)
            return 0;
    }
    return 1;
}

long func(long n)
{
    int isExist[10];
    long index;
    for(index=0;index<10;index++)
        isExist[index] = 0;
    long multNumber = 1;
    while(1)
    {
        long multVal = n*multNumber;
        std::stringstream strInp;
        strInp << multVal;
        std::string strVal = strInp.str();

        long strIndex;
        for(strIndex=0;strIndex<strVal.length();strIndex++)
        {
            isExist[strVal[strIndex]-'0'] = 1;
        }

        int ifCovered = checkAll(isExist);
        if(ifCovered == 1)
        {
      //   cout << multVal << endl;
            //break;
            return multVal;
        }
        multNumber += 1;
    }
    return -1;
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

        long n;
        //cin >> cursize;

        std::istringstream iss2;

        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss2.str(line);
            iss2 >> n;

        //    cout << "Cursize "<< cursize << endl;
            }


    long res = 0;
    if(n == 0)
        outfile << "Case #"<<curTestCase+1<<": INSOMNIA"<<endl;
    else
    {

        res = func(n);
        outfile << "Case #"<<curTestCase+1<<": "<<res<<endl;
    }
    //cout << res << endl;
    }

    //cout << "Hello world!" << endl;
    return 0;
}
