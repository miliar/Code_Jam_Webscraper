#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t,a,b,k;
    ifstream fe("B-small-attempt0.in");
    ofstream fs("B-small-attempt0.out");
    fe>>t;
    for (int q=1; q<=t; q++)
    {
        fe>>a>>b>>k;
        int con=0;
        for (int w=0; w<a; w++)
        {
            for (int e=0; e<b; e++)
            {
                if ((w&e)<k)
                {
                    con++;
                }
            }
        }
        fs<<"Case #"<<q<<": "<<con<<endl;
    }
    return 0;
}
