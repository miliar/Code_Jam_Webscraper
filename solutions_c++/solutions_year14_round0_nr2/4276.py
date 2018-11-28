#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;
int T;
double C,F,X;
int main(){
    fstream in,out;
    in.open("input.in",ios::in);
    out.open("output.txt",ios::out);
    in >> T;
    for(int test = 1; test <= T; ++test){
        in >> C >> F >> X;
        double ans = X+1;
        double S = 2.0;
        double cum = 0;
        while(true){
            double tmp = cum + X/S;
            if(tmp < ans){
                ans = tmp;
            }else break;
            cum+= C/S;
            S+= F;
        }
        out << "Case #" << test << ": " << setprecision(7) << fixed << ans << endl;
    }

}
