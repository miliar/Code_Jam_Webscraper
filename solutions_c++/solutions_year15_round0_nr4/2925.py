#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t,x,r,c,prod;
    ifstream fin("D-small-attempt0.in");
    ofstream fout("output.txt");
    fin>>t;
    for(int q=1;q<=t;q++)
    {
        fin>>x>>r>>c;
        prod=r*c;
        if(prod%x!=0)
        fout<<"Case #"<<q<<": RICHARD\n";
        else
        {
            if(x==1)
            fout<<"Case #"<<q<<": GABRIEL\n";
            else if(x==2)
            {
                if((r%2!=0)&&(c%2!=0))
                fout<<"Case #"<<q<<": RICHARD\n";
                else
                fout<<"Case #"<<q<<": GABRIEL\n";
            }
            else if(x==3)
            {
                if(prod==3)
                fout<<"Case #"<<q<<": RICHARD\n";
                else if(prod==6)
                {
                    if(r==1||c==1)
                    fout<<"Case #"<<q<<": RICHARD\n";
                    else if(r==2||r==3)
                    fout<<"Case #"<<q<<": GABRIEL\n";
                }
                else if(prod==9)
                {
                    if(r==1||c==1)
                    fout<<"Case #"<<q<<": RICHARD\n";
                    else if(r==3||c==3)
                    fout<<"Case #"<<q<<": GABRIEL\n";
                }
                else if(prod==12)
                {
                    if(r==1||c==1)
                    fout<<"Case #"<<q<<": RICHARD\n";
                    else if(r==2||r==6||r==3||r==4)
                    fout<<"Case #"<<q<<": GABRIEL\n";
                }
                else if(prod==15)
                {
                    if(r==1||c==1)
                    fout<<"Case #"<<q<<": RICHARD\n";
                    else if(r==3||r==5)
                    fout<<"Case #"<<q<<": GABRIEL\n";
                }
            }
            else if(x==4)
            {
                if(prod==4)
                fout<<"Case #"<<q<<": RICHARD\n";
                else if(prod==8)
                fout<<"Case #"<<q<<": RICHARD\n";
                else if(prod==12)
                {
                    if(r==1||r==12||r==2||r==6)
                    fout<<"Case #"<<q<<": RICHARD\n";
                    else if(r==3||r==4)
                    fout<<"Case #"<<q<<": GABRIEL\n";
                }
                else if(prod==16)
                {
                    if(r==1||r==16||r==2||r==8)
                    fout<<"Case #"<<q<<": RICHARD\n";
                    else if(r==4)
                    fout<<"Case #"<<q<<": GABRIEL\n";
                }
            }
        }
    }
    return 0;
}
