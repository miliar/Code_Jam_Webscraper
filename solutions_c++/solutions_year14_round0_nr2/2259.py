#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;


double t() {

    double mn=1e11;
double current=0;

    double X,C,F;
    cin>>C>>F>>X;


    for(int i=0;i<X/C+1;i++) {
        mn = min(mn, current + X / (2 + F*i));
        current += C / (2 + F*i);

    }
    return mn;

}
int main() {
    int tt;
    cin>>tt;
    for(int i=1;i<=tt;i++) {
        cout<<"Case #"<<i<<": "<<setprecision(15)<<t()<<"\n";
    }
    
}
