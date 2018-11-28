#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int b[1001];
    ifstream init;
    init.open("init.txt");
    int a;
    for(int i=0; i<1001; i++)
    {
        init>>a;
        init>>b[i];
    }
    ifstream in;
    in.open("C-small-attempt0.in");
    int t;
    in>>t;
    int c,d;
    ofstream out;
    out.open("out.txt");
    for(int i=0; i<t; i++)
    {
        in>>c>>d;
        out<<"Case #"<<i+1<<": "<<b[d]-b[c-1]<<endl;
    }
    return 0;
}
