#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include <fstream>

using namespace std;

ifstream in("D.in");
ofstream out("D.out");

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
            if(x==5)
            {
                if( (r*c)%5!=0)
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
            if(x==6)
            {
                 if( (r*c)%6!=0)
                {
                    richard();
                }
                else
                {
                    if((r<=3)||(c<=3))
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
