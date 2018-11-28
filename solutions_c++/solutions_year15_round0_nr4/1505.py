#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("H.in");
    ofstream out("H.out");
    int i, X, R, C, T;
    in>>T;
    for(i=1; i<=T; i++)
    {
        X=R=C=0;
        in>>X;
        in>>R;
        in>>C;
        out<<"Case #"<<i<<": ";

        if((R*C)%X != 0)
        {
            out<<"RICHARD\n";
        }
        else
        {
            if(((X)>R && (X)>C)|| (X-1>C)||(X-1>R))
            {
                out<<"RICHARD\n";
            }
            else if((X/2)>R || (X/2)>C)
            {
                out<<"RICHARD\n";
            }
            else
            {
                out<<"GABRIEL\n";
            }
        }
    }
    return 0;
}
