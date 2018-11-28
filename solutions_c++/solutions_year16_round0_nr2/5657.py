#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("B-large.in");
    out.open("B-large.out");
    unsigned tests, currentTest=0;
    in>>tests;

    while(currentTest++ <tests)
    {
        string cakes;
        in>>cakes;
        char prev='+';
        unsigned moves=0;
        for(unsigned i=0; cakes[i]!='\0';i++)
        {
            if(cakes[i]=='-' && prev=='+') moves+=2;
            prev=cakes[i];
        }
        if(cakes[0]=='-')moves--;
        out<<"Case #"<<currentTest<<": "<<moves<<endl;
    }
    in.close();
    out.close();
    return 0;
}
