#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
using namespace std;
ifstream inp;
ofstream oup;
int main(){
    inp.open("input2.in");
    oup.open("output2.txt");
    int T;
    inp>>T;
    for (int t=0; t<T; t++){
        double C;
        double F;
        double X;
        inp>>C>>F>>X;
        int farms;
        farms=ceil(X/C-1-2/F);
        
        
        
        
        double time=0;
        for (int i=0; i<farms; i++){
            time += C/(2+i*F);
        }
        time+=X/(2+F*farms);
        if (X/2<X/(2+F)+C/2) time=X/2;
        
        oup<<"Case #"<<t+1<<": "<<std::setprecision(10)<<time<<endl;
    }   

}
