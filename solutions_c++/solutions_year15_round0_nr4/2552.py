#include <stdlib.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <string>

using namespace std;

#define INPUT "D-small.in"
#define OUTPUT "D-small.out"

int main()
{
    int  T;
    string s;
    ifstream in;
    in.open(INPUT, ios::in);
    ofstream out;
    out.open(OUTPUT, ios::out);
    getline(in, s);
    T= atoi(s.c_str());
    for(int t=1; t <=T; t++)
    {
        int X, R, C;
        getline(in, s);
        sscanf(s.c_str(), "%d %d %d", &X, &R, &C);
        bool r = false;
        if(X>R*C)
            r=true;
        else
        if((R*C%X)!=0)
            r=true;
        else
        if((X>2)&&(((X-1)>R)||(X-1)>C))
            r=true;
        if(!r)
            out <<"Case #"<<t<<": "<<"GABRIEL"<<endl;
        else
            out <<"Case #"<<t<<": "<<"RICHARD"<<endl;

    }
    in.close();
    out.close();
}




