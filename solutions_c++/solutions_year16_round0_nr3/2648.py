//
//  main.cpp
//  jam2
//
//  Created by Liubov Galkovska on 4/9/16.
//
//

#include <iostream>
#include <vector>
#include <set>
#include <math.h>
using namespace std;
/***********************/
void dec_to_bin (int inNum, vector<int>& outBin)
{
    int n = inNum;
    while (n)
    {
        outBin.push_back(n%2);
        n /=2;
    }
    /*
     for (int i = outBin.size() - 1; i >= 0; --i)
     {
     cout << outBin[i];
     }*/
}
/***********************/
uint64_t toBase (int iBase, const vector<int>& iBin)
{
    uint64_t res = 0;
    for (int i = 0; i < iBin.size(); ++i)
    {
        res += pow(iBase, i) * iBin[i];
    }
    return res;
}
/***********************/
uint64_t checkPrime (uint64_t inNum)
{
    uint64_t i = 2;
    uint64_t limit = sqrt(inNum);
    
    for (i = limit; i >=2;  --i)
    {
        if (inNum%i == 0)
        {
      //      cout << inNum << " " << i << " " << inNum%i << endl;
            break;
        }
    }
    
    return i;
}
/***********************/
void outputResult (const vector<int>& inBinNum, const vector<uint64_t>& inDivs)
{
    for (int i = inBinNum.size() - 1; i >= 0; --i)
    {
        cout << inBinNum[i];
    }
    
    for (int i = 0; i < inDivs.size(); ++i)
    {
        cout << " " << inDivs[i];
    }
    cout << endl;
}
/***********************/
int main()
{
   // int a;
   // cin >> a >> a>> a >> a;
    
    int testCases, N, J;
    cin >> testCases >> N >> J;
    
    cout << "Case #1:" << endl;
    
    uint64_t start = 0, stop = 0, count = 0;
    start = 1 + pow(2,N-1);
    stop  = pow (2,N);
    //   cout << start << " " << stop << endl;
    
    for (int i = start; (i < stop) && (count < J); i+=2)
    {
        vector<int> binNum;
        dec_to_bin (i, binNum);
        
        vector<uint64_t> divisions;
        uint64_t division = 0;
        bool good = true;
        
        for (int base = 2; good && (base <= 10); ++base)
        {
            uint64_t interp = toBase (base, binNum);
            //cout << "interp: " << interp << endl;
            division = checkPrime (interp);
            if (division == 1)
                good = false;
            else
                divisions.push_back (division);
        }
        
        if (good)
        {
            ++count;
            outputResult(binNum, divisions);
        }
        
        
    }
    
    return 0;
}