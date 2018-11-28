#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORI(i,b) FOR(i,0,b)



int main()
{
    ifstream input("input.in",ifstream::in);
    ofstream output("output.out",ofstream::out);

    int T;
    input >> T;
    FORI(i,T)
    {
        int r, t;
        input >> r;
        input >> t;
        int rings = 0;
        do
        {
            t-= pow(r+rings*2+1,2)-pow(r+rings*2,2);
            rings++;
        }
        while(t >= 0);
        rings--;
        output << "Case #" << i+1 << ": " << rings << endl;
    }
    return 0;
}
