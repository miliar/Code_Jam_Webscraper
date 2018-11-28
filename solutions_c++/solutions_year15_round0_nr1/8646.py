#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <sstream>
using namespace std;

int main()
{
    ifstream  afile;
    ofstream outfile;
    outfile.open("outfile.dat");
    string line;
    int noofcases;
    afile.open("A-large.in");

    getline(afile,line);
    noofcases = atoi(line.c_str());
    for(int x=1; x<=noofcases; x++)
    {
        int maxshyness;
        getline(afile,line);
        istringstream iss(line);
        iss >> maxshyness >> line;

        long sum=0, count=0;
        for(int i =0; i<=maxshyness;i++)
        {
            if(i==0)
            {
                sum += atoi(line.substr(i, 1).c_str());
            }
            else
            {
            if(sum >= i)
            sum += atoi(line.substr(i, 1).c_str());
            else
            {
                count++;
                sum++;
                sum += atoi(line.substr(i, 1).c_str());
            }
            }

            if(sum>=maxshyness)
                break;
        }

        outfile << "Case #" << x << ": " << count << '\n';

    }
    return 0;
}
