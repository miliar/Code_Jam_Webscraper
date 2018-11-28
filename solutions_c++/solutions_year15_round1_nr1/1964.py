#include <iostream>
#include <fstream>


using namespace std;

int main()
{
    ifstream in("A-large(1).in");
    ofstream out("salida.out");

    long int t,n,hongo[1001],h,i,x,y,mayordif;
    in>>t;
    for(h=1;h<=t;h++)
    {
        in>>n;
        for(i=1;i<=n;i++)
        {
            in>>hongo[i];
        }
        x=0;
        for(i=2;i<=n;i++)
        {
            if(hongo[i]<hongo[i-1])
            {
                x=x+hongo[i-1]-hongo[i];
            }
        }
        mayordif=0;

        for(i=2;i<=n;i++)
        {
        if(hongo[i-1]-hongo[i]>mayordif)
        {
            mayordif=hongo[i-1]-hongo[i];

        }
        }
        y=0;
        for(i=1;i<=n-1;i++)
        {
            if(hongo[i]<mayordif)
            {
                y=y+hongo[i];
            }
            else
            {
                y=y+mayordif;
            }
        }
     out<<"Case #"<<h<<": "<<x<<" "<<y<<endl;
    }


    in.close();
    out.close();
    return 0;
}
