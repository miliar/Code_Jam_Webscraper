#include <fstream>
using namespace std;

int main() {
    ifstream in("B-large.in");
    ofstream out("output.out");
    out.precision(15);
    double c,f,x,s,rate;
    int i,l,t;
    in>>t;
    for (l=1; l<=t; l++) {
        in>>c>>f>>x;
        rate = 2.0;
        s=0;
        while (x/rate > (c/rate) + (x/(rate+f)) ) {
            s+=(c/rate);
            rate+=f;
        }
        s+=x/rate;
        out<<"Case #"<<l<<": "<<s<<'\n';
    }
    out.close();
    return 0;


}
