#include<iostream>
#include<fstream>
#include<iomanip>


using namespace std;


int main()
{
    int T;
    ifstream in("in.txt");
    ofstream out("out.txt");
    double c,f,x;
    double t=0,cs = 2;
    in>>T;
    out<<fixed;
    for(int i=1;i<=T;i++)
    {
        in>>c>>f>>x;

        if(x<c)
        {
            out<<"Case #"<<i<<": "<<x/cs<<"\n";
            continue;
        }

        while(1)
        {
            if(c/(cs) + x/(cs+f) < x/cs)
                t += (c/cs);
            else
            {
                t += x/cs;
                break;
            }
            cs += f;
        }


        out<<"Case #"<<i<<": "<<setprecision(7)<<t<<"\n";

        cs = 2;
        t = 0;
    }
    return 0;
}
        


    
