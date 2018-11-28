#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    ifstream fin("in3.txt", ios::in);
    ofstream fout("3key.txt", ios::out);
    int T, i=1, X, R, C;
    fin>>T;
    while(T--)
    {
        fin>>X>>R>>C;
        //fout<<"config:"<<X<<R<<C<<endl;
        if((R*C) % X != 0)
        {
            fout<<"Case #"<<i<<": RICHARD\n";
        }
        else
        {
            if(X == 1)
            {
                fout<<"Case #"<<i<<": GABRIEL\n";
            }
            else if(X == 2)
            {
                fout<<"Case #"<<i<<": GABRIEL\n";
            }
            else if(X == 3)
            {
                if((R*C) == 3)
                    fout<<"Case #"<<i<<": RICHARD\n";
                else
                    fout<<"Case #"<<i<<": GABRIEL\n";
            }
            else if(X == 4)
            {
                if((R*C) == 4 || (R*C) == 8)
                    fout<<"Case #"<<i<<": RICHARD\n";
                else
                    fout<<"Case #"<<i<<": GABRIEL\n";
            }
        }
        ++i;
    }
    return 0;
}
