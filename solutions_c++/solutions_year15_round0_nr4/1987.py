#include<bits/stdc++.h>
#define mp make_pair
using namespace std;
int main()
{
    int t,j,x,r,c,f=0;
    ifstream IF;
    ofstream OF;
    IF.open("input.txt");
    OF.open("output.txt");
    IF>>t;
    for(j=1;j<=t;j++)
    {
        IF>>x>>r>>c;
        if(x==1)
            f=1;
        else if(x==2)
        {
            if((r*c)%2)
                f=0;
            else
                f=1;
        }
        else if(x==3)
        {
            if(r==1)
                f=0;
            else if(r==2)
            {
                if(c==3)
                    f=1;
                else
                    f=0;
            }
            else if(r==3)
            {
                if(c!=1)
                    f=1;
                else
                    f=0;
            }
            else
            {
                if(c!=3)
                    f=0;
                else
                    f=1;
            }
        }
        else
        {
            if((r==3 && c==4)||(r==4 && c==3)||(r==4 && c==4))
                f=1;
            else
                f=0;
        }
        if(f)
            OF<<"Case #"<<j<<": GABRIEL"<<endl;
        else
            OF<<"Case #"<<j<<": RICHARD"<<endl;
    }
    IF.close();
    OF.close();
    return 0;
}


