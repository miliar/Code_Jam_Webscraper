#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

double cost=-1;
double GetNextTime(double prod) {
    return cost/prod;
}
int main()
{
    ifstream ss;
    ofstream sss;
    sss.precision(10);
    ss.open("a.txt");
    sss.open("a.out");
    int nbCases;
    ss >> nbCases;
    for(int i=0 ; i<nbCases ; i++) {
        double f, x, prod;
        prod=2;
        ss >> cost >> f >> x;
        double time=0;
        while(42) {
            double timeToNext = GetNextTime(prod);
            double timeToFinish = x/prod;
            if(timeToNext+x/(prod+f)>timeToFinish) {
                time+=timeToFinish;
                break;
            } else {
                time+=timeToNext;
                prod+=f;
            }
        }
        sss << "Case #" << i+1 << ": " << time << endl;
    }
    ss.close();
    sss.close();
    return 0;
}
