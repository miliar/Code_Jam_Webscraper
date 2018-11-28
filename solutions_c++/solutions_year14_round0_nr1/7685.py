#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin>>T;
    for (int t=0; t<T; t++)
    {
        int a,b,c=0;
        fin>>a;
        bool pos[17];
        memset(pos,0,sizeof(pos));
        for (int k=0; k<4; k++)
            for (int i=0; i<4; i++)
            {
                fin>>b;
                if (k==a-1)
                {
                    pos[b]=1;
                }
            }
        fin>>a;
        for (int k=0; k<4; k++)
            for (int i=0; i<4; i++)
            {
                fin>>b;
                if (k==a-1)
                {
                    if (pos[b])
                    {
                        if (c==0)
                            c=b;
                        else
                            c=-1;
                    }
                }
            }
        fout<<"Case #"<<t+1<<": ";
        if (c==-1) fout<<"Bad magician!"<<endl;
        else if (c==0) fout<<"Volunteer cheated!"<<endl;
        else fout<<c<<endl;
    }
    return 0;
}
