#include<fstream>
using namespace std;
int main ()
{
    ifstream in("D-small-attempt1.in");
    ofstream out("output.txt");
    int t,P,y,c;
    in>>t;
    for(int i=1;i<=t;i++)
    {
        in>>P>>y>>c;
        out<<"Case #"<<i<<": ";
        if(P==1)
            out<<"GABRIEL\n";
        else
            if(P==2)
                if((y*c)%2==0)
                    out<<"GABRIEL\n";
                else
                    out<<"RICHARD\n";
            else
                if(P==3)
                    if((y>2 || c>2) && (y*c)>=6 && ((y*c)-6)%3==0)
                        out<<"GABRIEL\n";
                    else
                        out<<"RICHARD\n";
                else
                    if(P==4)
                        if((y>3 || c>3) && (y*c)>=12 && ((y*c)-12)%4==0)
                            out<<"GABRIEL\n";
                        else
                            out<<"RICHARD\n";
                    else
                        out<<"RICHARD\n";
    }
}
