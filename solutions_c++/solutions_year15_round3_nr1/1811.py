#include <fstream>
#include <iostream>

using namespace std;

const char InFile[]="input.txt";
const char OutFile[]="output.txt";

ifstream fin(InFile);
ofstream fout(OutFile);

int T,R,C,W;

int main()
{
    fin>>T;
    for(int t=1;t<=T;++t)
    {
        int sol=0;
        fin>>R>>C>>W;
        if(W==1)
        {
            fout<<"Case #"<<t<<": "<<R*C<<"\n";
            continue;
        }
        if(W==C)
        {
            fout<<"Case #"<<t<<": "<<R+C-1<<"\n";
            continue;
        }
        sol=C/W-1;
        int add=0;
        if(C%W==0)
        {
            --sol;
        }
        fout<<"Case #"<<t<<": "<<(sol+1)*R+W<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}
