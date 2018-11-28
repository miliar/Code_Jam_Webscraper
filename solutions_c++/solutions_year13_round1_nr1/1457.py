
#include <iostream>
#include <string>
#include <math.h>
#include <memory.h> 
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

#define inFile cin
#define  outFile cout

int main()
{
    ifstream inFile;
    ofstream outFile;
    inFile.open("A-small-attempt0.in");
    outFile.open("A-small-attempt0.out");

    int num_cases;
    inFile>>num_cases;
    for (int i = 1; i < num_cases + 1; i++ )
    {
        long long r;
        long long t;
        inFile>>r>>t;
        long long count = -1;
        long long j = r;
        long long sum = 0;
        while (sum <= t)
        {
            sum += 2*j +1;
            j += 2;
            count++;
        }
        outFile<<"Case #"<<i<<": "<<count<<'\n';
    }
    return 0;
}


