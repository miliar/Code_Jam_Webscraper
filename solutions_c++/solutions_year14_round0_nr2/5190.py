#include<iostream>
#include<iomanip>
#include<stdio.h>
using namespace std;

int main() {
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    int T,k=1;
    double rate,C,F,X,time,ftime;
    cin>>T;
    while(T--) {
               cin>>C>>F>>X;
               rate=2;
               time=X/2;
               ftime=C/2;
               while(time>ftime+X/(rate+F)) {
                                               time=ftime+X/(rate+F);
                                               rate+=F;
                                               ftime+=C/rate;
               }
               cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<time<<endl;
               k++;
    }
    return 0;
}
