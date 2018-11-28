#include <stdlib.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <string>

using namespace std;

#define INPUT "A-small-attempt3.in"
#define OUTPUT "A-small.out"

int main()
{
    int  T;
    string s;
    ifstream in;
    in.open(INPUT, ios::in);
    ofstream out;
    out.open(OUTPUT, ios::out);
    getline(in, s);
    T= stoi(s);
    for(int t=1; t <=T; t++)
    {
        int R, C, W;
        getline(in, s);
        sscanf(s.c_str(), "%d %d %d", &R, &C, &W);
        int y=0;
        if(W==1)
            y = R*C;
        else
            if(C<=2*W)
                if(C==W)
                    y = R-1 +W;
                   else
                    y = R + W;
            else
                if(C==W)
                    y = R-1+W;
                 else
                    y = (R-1)*C/W+(C-1)/W+W;
        out <<"Case #"<<t<<": "<<y<<endl;
    }
    in.close();
    out.close();
}




