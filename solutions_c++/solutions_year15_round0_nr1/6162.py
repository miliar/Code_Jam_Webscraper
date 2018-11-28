#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <iomanip>

using namespace std;
int main()
{
    int index,tCase;
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("output.txt");
    int t;
    in>>t;
    for(tCase=1; tCase<=t; ++tCase)
    {
        int maxShyness;
        string shyness;
        int ctr = 0, peopleStanding = 0, soln = 0;
        in>>maxShyness>>shyness;
        for(index = 0;index<=maxShyness; ++index)
        {
            ctr = 0;
            int temp = shyness[index]-48;
            if(temp>0 && index>peopleStanding)
            {
                ctr = index - peopleStanding;
                soln += ctr;
            }
            peopleStanding += temp + ctr;
        }
        out<<"Case #"<<tCase<<": "<<soln<<endl;
    }
    return 0;
}
