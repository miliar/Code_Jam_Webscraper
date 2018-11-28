#include<iostream>
#include<iomanip>
#include<stdio.h>
using namespace std;
int main() {
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    int T,k=1;
    double r,C,F,X,time,ft;
    cin>>T;
    while(T--) {
               cin>>C>>F>>X;
               r=2;
               time=X/2;
               ft=C/2;
               while(time>ft+X/(r+F)) {
                                               time=ft+X/(r+F);
                                               r+=F;
                                               ft+=C/r;
               }
               cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<time<<endl;
               k++;
    }
    return 0;
}
