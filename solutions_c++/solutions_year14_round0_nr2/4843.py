#include <math.h>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

string prd(const double x, const int decDigits) {
    stringstream ss;
    ss << fixed;
    ss.precision(decDigits);
    ss << x;
    return ss.str();
}

int main()
{

    ifstream fin("B-small-attempt0.in");
    ofstream fout("outputB.txt");
    int T;
    fin>>T;
    for(int t=1;t<=T;t++){
            double c,f,x;
            fin>>c>>f>>x;
            double time,preTime=99999999999;
            double cookies=2.0;
            int n=0;
            while(true){
                time=x/(cookies+n*f);
                for(int i=0;i<n;i++)
                    time+=c/(cookies+i*f);
                if(preTime<time)
                    break;
                preTime=time;
                n++;
            }
            fout<<"Case #"<<t<<": "<<prd(preTime,7)<<endl;

    }
    return 0;
}
