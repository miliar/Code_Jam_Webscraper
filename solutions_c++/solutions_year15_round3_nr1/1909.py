#include <fstream>
//#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;
int main() {
    ifstream cin("inputt.in");
    ofstream cout("wow.in");
    double a,t,b,c,d,e,i,j;
    cin>>t;
    for(i=0;i<t;i++) {
        cin>>a>>b>>c;
        d=max(a,b);
        e=min(a,b);
        if(e<c||c==1) cout<<"Case #"<<i+1<<": "<<ceil(d/c)*e+c-1<<endl;
        else cout<<"Case #"<<i+1<<": "<<ceil(d/c)*e+c<<endl;
    }
}
