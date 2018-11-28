#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int i,t,y,r,c,min;
    fstream fin,fout;
    fin.open("D-small-attempt5.in",ios::in);
    fout.open("op.txt",ios::out);
    fin>>t;
    for(i=1;i<=t;i++)
    {
        fin>>y>>r>>c;
        if((r*c)%y==0)
        {
            if(y<3)
            {
                fout<<"Case #"<<i<<": GABRIEL\n";
            }
            else
            {
                if(y==4)
                {
                    if((r>2&&c>=4)||(r>=4&&c>2))
                        fout<<"Case #"<<i<<": GABRIEL\n";
                    else
                        fout<<"Case #"<<i<<": RICHARD\n";
                }
                else
                {
                    if((r>=2&&c>=3)||(r>=3&&c>=2))
                        fout<<"Case #"<<i<<": GABRIEL\n";
                    else
                        fout<<"Case #"<<i<<": RICHARD\n";
                }
            }
        }
        else
            fout<<"Case #"<<i<<": RICHARD\n";
    }
    fin.close();
    fout.close();
    return 0;
}
