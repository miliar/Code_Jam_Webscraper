#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cmath>
//#include <math.h>
using namespace std;

int main()
{
    long long int r,t,i,j;
    int casenum, count;
    ifstream input ("A-0.in");
    string line;
    stringstream convert;

    casenum = 1;

    input >> i;

    while (getline(input, line)) {
        istringstream iss(line);
        while (iss >> r >> t) {
            count = 0;
            j = 2*r + 1; 
            t = t-j; 
            //cout << "t j: " << t << " " << j << " " << endl;
            while (t >=0) {
               j =j+ 4;
               t = t-j; 
               //cout << "t j: " << t << " " << j << " " << endl;
               count++;
            }

            cout << "Case #" << casenum << ": " << count << endl;
            casenum++;
        }
    }
}
