#include<fstream>
#include<iostream>
#include<set>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("cookie.out");

int main(){
    int T;
    fin >> T;
    for(int t=0; t<T; t++){
        double C, F, X;
        fin >> C >> F >> X;
        
        double time = 0;
        double prod = 2;
        
        while(true){
            double time2 = time + (C / prod);
            double prod2 = prod + F;
            if(time2 + X/prod2 > time + X/prod) break;
            time = time2;
            prod = prod2;
        }
        
        fout.precision(10);
        fout << "Case #" << t+1 << ": " << time + (X/prod) << endl;
    }
}
