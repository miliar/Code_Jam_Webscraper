#include <iostream>
#include <fstream>
#include <iostream>     // std::cout, std::fixed
#include <iomanip>      // std::setprecision

using namespace std;

int main()
{
    int T,XX=1;

    ifstream fin("B-large.in");
    ofstream fout("B-large.out");

    fin >> T;

    while(T-->0)
    {
        double C,F,X;
        fin >> C >> F >> X;
        double secY=0;
        int farms=0;
        while(((C/(2+F*farms)) + (X/(2+F*(farms+1))) ) < (X/(2+F*farms)))
        {
            secY+=C/(2+F*farms);
            farms++;
        }
        secY+=X/(2+F*farms);

        fout << "Case #" << XX++ << ": " << fixed << setprecision(7) << secY << "\n";
    }
    return 0;
}

