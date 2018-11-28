#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int t;
    ifstream f1("1.txt");
    ofstream f2("2.txt");
    f1>>t;
    for(int y=1;y<=t;y++)
    {
        int x,r,c;
        f1>>x>>r>>c;
        int n=r*c;
        if(x==4)
        {
            if(r*c<x)
                f2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
            else if(r*c==8 || r*c==4 || n%x!=0)
                f2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
            else
                f2<<"Case #"<<y<<": "<<"GABRIEL"<<"\n";

        }
        else if(x==3)
        {
            if(r*c<x)
                f2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
            else if(r*c==3 || n%x!=0)
                f2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
            else
                f2<<"Case #"<<y<<": "<<"GABRIEL"<<"\n";

        }
        else
        {

            if(r*c<x)
                f2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
        else if(n%x!=0 )
            f2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
        else
            f2<<"Case #"<<y<<": "<<"GABRIEL"<<"\n";
        }
    }
    return 0;
}
