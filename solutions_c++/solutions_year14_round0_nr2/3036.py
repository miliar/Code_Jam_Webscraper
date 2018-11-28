

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream input ("/Users/hasan/Desktop/xcode projects/cookie/cookie/B-large.in.txt");
    ofstream output ("/Users/hasan/Desktop/xcode projects/cookie/cookie/B-large.out.txt");
    
    double r,C,F,X,ttt;
    double tt, mint;
    int t;
    input >> t;
    
    for (int l=0; l<t; l++) {
        input >> C >> F >> X;
        r=2.0;
        tt = 0.0, mint = X/r;
        while (tt<mint) {
            tt += C/r;
            r += F;
            ttt = tt + X/r;
            if (ttt<mint)
                mint = ttt;
        }
        
        output <<fixed<<setprecision(7)<< "Case #" << l+1 << ": " << mint << endl;
    }
    
    return 0;
}
