#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main()
{
    ifstream in;
    in.open("B-large.in");
    ofstream out;
    out.open("B-small-attempt.out");
    int n;
    in>>n;
    for (int cur=1;cur<=n;cur++){
        double ans=0.0,C,F,X,t;
        double v=2;
        double c=0, Y, T;
        in>>C>>F>>X;
        while ((double)X/v>(double)(C/v+X/(F+v))){
           t=(double)C/v;
           Y = t - c;
           T = ans + Y;
           c = T - ans - Y;
           ans = T;
           v+=F;
        }
        ans=ans+(double)X/v;
        out<<"Case #"<<cur;
        out<<fixed;
        out.precision(7);
        out<<": "<<ans;
        if (cur<n) out<<"\n";
    }
    return 0;
}
