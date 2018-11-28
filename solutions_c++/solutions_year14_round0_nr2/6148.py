#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <unistd.h>
#include <stdio.h>


using namespace std;

vector<int> v1;
vector<int> v2;
int total = -1;
double X=-1;
double C=4;
double F=-1;

double timeByFarms(int farms)
{
    double bal = 0.0;
    double inc = 2.0 + F*farms;
    return X/inc; 
}
// c is number of farms
double calculateTime(int c) {
    double timeCurConf = timeByFarms(c);
    double timeToNextFarm = C/(2.0+F*(float)c);
    double timeNextFarm = timeByFarms(c+1);
    if( timeCurConf <= (timeToNextFarm + timeNextFarm) )
        return timeCurConf;
    else
        return timeToNextFarm + calculateTime(c+1);
}

int main(int argc,char **argv){
    ifstream inf;

    inf.open(argv[1]);

    if(!inf.good())
        return -1;
    inf >> total;
    //cout << "total: " << total << endl;
    string str;
    for( int i = 0; i < total; i ++ ) {
        inf >> C;
        inf >> F;
        inf >> X;
        //cout << "C: "<< C << endl;
        //cout << "F: "<< F << endl;
        //cout << "X: "<< X << endl;
        //printf("C=%.07f F=%.07f X=%.07f\n", C, F, X);
  
        int c = 0;
        double t2 = calculateTime( c );
        printf( "Case #%d: %.07f\n", i+1, t2 );
    }

    return 0;
}
