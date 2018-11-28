#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    in>>n;
    for(int k=0;k<n;k++) {

        bool flag=true;
        long double C,F,X,time=0,speed=0;
        in>>C>>F>>X;
        if (X < C) {
            out<<setiosflags( std::ios_base::fixed )<<setprecision(7)<<"Case #"<<k+1<<": "<<X/2<<endl;
            continue;
        }
        speed=2.;
        time=0.;

        while (flag) {

            if (X/speed < (C/speed+X/(speed+F))) {
                time+=X/speed;
                out<<setiosflags( std::ios_base::fixed )<<setprecision(7)<<"Case #"<<k+1<<": "<<time<<endl;
                flag=false;
            }
            else {
                time+=C/speed;
                speed+=F;
            }

        }

    }
}

