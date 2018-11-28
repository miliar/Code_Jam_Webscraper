#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream in("B-large.in");
    ofstream out("salB.out");

    int t,i,a;
    double frec=2,c,f,x,segundos,esperando,comprando;

    in>>t;
    for(i=1;i<=t;i++)
    {
        in>>c>>f>>x;
        frec=2;
        a=1;
        segundos=0;
        while(a==1)
        {


        esperando=x/frec;
        comprando=(c/frec)+(x/(frec+f));

        if(comprando>esperando)
        {
            segundos=segundos+esperando;
            a=0;
        }
        else
        {
            segundos=segundos+(c/frec);
            frec=frec+f;

        }
        }
        out << "Case #" << i << ": " << fixed << setprecision(7) << segundos << endl;


    }

    in.close();
    out.close();
    return 0;
}
