#include <fstream>
#include <iomanip>
using namespace std;
bool checkfast(double C,double rate, double F, double X){
    return (C/rate+X/(rate+F)<X/rate);
    }
int main(){
    int T;
    ifstream in("inputl.txt");
    ofstream out("output.txt");
    in >> T;
    for(int i=0;i<T;i++){
        double C, F, X;
        in>> C>>F>>X;
        double t=0;
        double rate=2;
        while(checkfast(C,rate,F,X)){
            t=t+ C/rate;
            rate=rate+F;
        }
        t=t+X/rate;
        out<<"Case #"<<i+1<<": "<<fixed<<setprecision(8)<< t<<endl;
    }
}
