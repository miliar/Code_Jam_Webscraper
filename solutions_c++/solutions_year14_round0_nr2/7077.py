#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <sys/time.h>
#include <float.h>
#include <iomanip>
using namespace std;

int main() {
    ofstream outputFile("output.txt");
    ifstream myfile("B-large.in");
    int t_c;
    int t  = 1;
    myfile >> t_c;
    while (t<t_c+1) {
    double c,f,x,temp1,temp2,temp3,r,temp4;
    temp4 = 0;
    r = 2.0;
    myfile >> c >> f >> x;
        temp1 = x/r;
        temp2 = c/r;
        r = r+f;
        temp3 = x/r;
        temp3 = temp3+temp2;
        if (temp3>temp1) {
            temp4 = temp4+temp1;
        } else {
            temp4 = temp4+temp2;
        }
    while(temp1>=temp3) {
        temp1 = x/r;
        temp2 = c/r;
        r = r+f;
        temp3 = x/r;
        temp3 = temp3+temp2;
        if (temp3>temp1) {
            temp4 = temp4+temp1;
        } else {
            temp4 = temp4+temp2;
        }
    }
    outputFile << "Case #" << t <<": "<<setprecision(15) <<temp4 <<endl;
    t++;
    }
return 0;
}
