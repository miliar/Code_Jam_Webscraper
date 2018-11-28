#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream f("A-large.in");
    ofstream fki("mo.txt");
    int t;
    f>>t;
    for (int i=0; i<t; i++)
    {
        int smax;
        f>>smax;
        string s;
        f>>s;
        int ujember=0;
        int regiember=0;
        for (int j=0; j<=smax; j++)
        {
            if (regiember+ujember<j){ujember+=(j-regiember-ujember);}
            regiember+=s[j]-48;
        }
        fki<<"Case #"<<i+1<<": "<<ujember<<endl;
    }
    return 0;
}
