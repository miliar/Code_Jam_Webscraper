#include <iostream>
#include <fstream>

using namespace std;

ifstream in("D-small-attempt2.in");
ofstream out("salida.out");

    int t,x,r,c,k;


void gabriel()
{
    out<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
}

void richard()
{
out<<"Case #"<<k<<": "<<"RICHARD"<<endl;
}
int main()
{
in>>t;

    for(k=1;k<=t;k++)
    {
        in>>x>>r>>c;
        if(x<7)
        {
            if(x==1)
            {
                gabriel();
            }
            if(x==2)
            {
                if((r*c)%2!=0)
                {
                    richard();
                }
                else
                {
                gabriel();
                }
            }
            if(x==3)
            {
                if((r*c)%3!=0)
                {
                    richard();
                }
                else
                {
                    if((r==1)||(c==1))
                    {
                        richard();
                    }
                    else
                    {
                        gabriel();
                    }
                }
            }
            if(x==4)
            {
                if((r*c)%4!=0 )
                {
                    richard();
                }
                else
                {
                    if((r<=2)||(c<=2))
                    {
                        richard();
                    }
                    else
                    {

                        gabriel();
                    }
                }
            }
        }
        else
        {
        richard();

        }

    }

in.close();
out.close();
    return 0;
}
