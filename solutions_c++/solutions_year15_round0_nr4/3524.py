#include <iostream>
#include <fstream>

using namespace std;

int i, X, R, C, test;
char flag;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("G:\\Codex\\D-small-attempt0.in");
    fout.open("G:\\Codex\\Domino_out.txt");
    fin>>test;

    for(i=0; i<test; i++)
    {
        fin>>X>>R>>C;
        if((R*C)%X!=0)
          flag='r';
        else
        {
            if(X==1 || X==2)
               flag='g';
            else if(X==3)
            {
                if(R*C == 3)
                    flag='r';
                else
                    flag='g';
            }
            else
            {
                if(R*C <12)
                    flag='r';
                else
                    flag='g';
            }


        }

    fout<<"Case #"<<i+1<<": ";
    if(flag == 'r')
        fout<<"RICHARD";
    else
        fout<<"GABRIEL";
    fout<<"\n";

    }
    fin.close();
    fout.close();
    return 0;
}
