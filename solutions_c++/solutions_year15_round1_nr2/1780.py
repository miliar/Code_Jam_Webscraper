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

long gcd(long a, long b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

long lcm(long a, long b)
{
    long temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}

long func(LongVector M,long b,long n)
{
//    cout << b << " " <<n<<endl;
    long index,index2;
    long counter = 0;


    long result = std::accumulate(M.begin(), M.end(), 1, lcm);
    long inn;
    long per = 0;
    for(inn=0;inn<b;inn++)
    {
        per+= result/M[inn];
    }
   // cout << n << " "<<per<< " " << result<<endl;
    long temp = n/per;
    if(n%per == 0)
        temp -= 1;
    n = n - temp*per;
 //   cout << n << " " << temp<< " " << result<<endl;
    if(n == 0)
        return 1;

    if(n <= b)
        return n;
    //if(tempp != 0)
      //  n = tempp;

    for(index=1;;index++)
    {
        for(index2=0;index2<b;index2++)
        {
            if(index%M[index2] == 0)
            {
                //cout << index << " "<<index2<<" " << M[index2] << endl;
                counter++;
                if(counter == n-b)
                    return index2+1;
            }
        }
    }
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
        LongVector vecInput;
        long cursize,n;
        //cin >> cursize;

        std::istringstream iss2;

        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss2.str(line);
            iss2 >> cursize;
            iss2 >> n;
        //    cout << "Cursize "<< cursize << endl;
            }

       long index;

            //cin >> chInput[index][index];
            std::string line;
            std::istringstream iss3;

            if (std::getline(myfile, line))
            {
            iss3.str(line);

            }

            long in;
           for(in=0;in<cursize;in++)
            {
                long longVal;
                iss3 >> longVal;
      //          cout << longVal << endl;
                vecInput.push_back(longVal);
            }
           // chInput[index][index2] = '\0';



    long res = func(vecInput,cursize,n);
    //cout << res << endl;
    outfile << "Case #"<<curTestCase+1<<": "<<res<<endl;
    }


    return 0;
}
