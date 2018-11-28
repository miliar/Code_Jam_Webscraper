#include<fstream>
using namespace std;
int main ()
{
    ifstream in("D-small-attempt2.in");
    ofstream out("output.txt");
    int t,x,r,c;
    in>>t;
    for(int i=1;i<=t;i++)
    {
        in>>x>>r>>c;
        out<<"Case #"<<i<<": ";
        if(x==1)
            out<<"GABRIEL\n";
        else
            if(x==2)
                if((r*c)%2==0)
                    out<<"GABRIEL\n";
                else
                    out<<"RICHARD\n";
            else
                if(x==3)
                    if((r>2 || c>2) && (r*c)>=6 && ((r*c)-6)%3==0)
                        out<<"GABRIEL\n";
                    else
                        out<<"RICHARD\n";
                else
                    if(x==4)
                        if((r>3 || c>3) && (r*c)>=12 && ((r*c)-12)%4==0)
                            out<<"GABRIEL\n";
                        else
                            out<<"RICHARD\n";
                    else
                        out<<"RICHARD\n";
    }
}
