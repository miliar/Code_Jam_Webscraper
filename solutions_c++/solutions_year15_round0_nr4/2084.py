#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int T,x,r,c;
    bool f;
    ifstream in;
    in.open("D-small-attempt1.in");
    ofstream out;
    out.open("out.txt");
    in>>T;
    for(int t=1; t<=T; t++)
    {
        f = false;
        in>>x>>r>>c;
        if(x==1)
        {
            f = true;
        }
        else if(x==2)
        {
            if(r%2 && c%2)
            {
                f = false;
            }
            else
            {
                f = true;
            }
        }
        else if(x==3)
        {
            if(r==1 || c==1)
            {
                f = false;
            }
            else if(r*c==4)
            {
                f=false;
            }
            else if(r*c==6)
            {
                f = true;
            }
            else if(r*c==9)
            {
                f = true;
            }
            else if(r*c==12)
            {
                f = true;
            }
            else if(r*c==16)
            {
                f = false;
            }
        }
        else if(x==4)
        {
            if(r==1 || c==1)
            {
                f = false;
            }
            else if(r==2 || c==2)
            {
                f = false;
            }
            else if(r*c==9)
            {
                f = false;
            }
            else if(r*c==12 || r*c==16)
            {
                f = true;
            }
        }
        out<<"Case #"<<t<<": ";
        if(f)
        {
            out<<"GABRIEL"<<endl;
        }
        else out<<"RICHARD"<<endl;
    }
    return 0;
}
