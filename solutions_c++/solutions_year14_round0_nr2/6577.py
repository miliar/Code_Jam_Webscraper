#include <iostream>
#include <iomanip>
#include <array>
#include <vector>
#include <algorithm>

using namespace std;

double solve(double c, double f, double x){
    int n = 0;
    double t = 0;
    double pt = 100000000000000;
    while(true){
        double a = n*f+2;
        //cout << "n:" << n << " t:" << t << " a:" << a << endl;
        double nt = t + x/a;
        if(nt > pt){
            return pt;
        }
        pt = nt;
        t += c/a;
        n++;
        //if(x > (c/f) * a){
        //    t += c/a;
        //    n++;
        //}else{
        //    return t + x/a;
        //}
    }
}


int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        double c,f,x;
        cin >> c >> f >> x;
        cout << "Case #" << t << ": " 
            << fixed
            << setprecision(7)
            << solve(c,f,x) << endl;
    }
}
