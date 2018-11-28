#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
    int T =0;
    string Cs, Fs, Xs;
    double C = 0.0, F = 0.0, X = 0.0;
    ifstream inF(argv[1]);

    inF >> T;
    
    for(int i = 0; i < T; i++)
    {
        double incr = 2.0;
        inF>> C  >> F >> X;
        
        double cTime = C/incr;
        double xTime = X/incr;
        while(xTime > cTime + X/(incr+F))
        {
            incr += F;
            xTime = cTime + X/incr;
            cTime += C/incr;
        }
        
        cout << std::fixed<< std::setprecision( 7 ) << "Case #" << i+1 <<": " << xTime << endl;
        
    }
   return 0;
}

