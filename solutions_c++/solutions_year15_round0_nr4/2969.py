#include<bits/stdc++.h>
#define in cin
#define out cout
using namespace std;
int main()
{
    ofstream out;
    out.open("4.out");
    ifstream in;
    in.open("D-small-attempt0.in");
    int t;
    in>>t;
    for(int i=1; i<=t; i++)
    {
        int x,r,c;
        in>>x>>r>>c;
        if(x==1)
            cout<<"Case #"<<i<<": GABRIEL\n";
        else
        {
            if(x==2)
            {
                if(((r*c)%2)==0)
                    cout<<"Case #"<<i<<": GABRIEL\n";
                else
                    cout<<"Case #"<<i<<": RICHARD\n";
            }
            if(x==3)
            {
                if(r==1 || c==1)
                    cout<<"Case #"<<i<<": RICHARD\n";
                else if((r%2)==0 && (c%2)==0)
                    cout<<"Case #"<<i<<": RICHARD\n";
                else
                    cout<<"Case #"<<i<<": GABRIEL\n";
            }
            if(x==4)
            {
                if((r*c)==16 || (r*c)==12)
                    cout<<"Case #"<<i<<": GABRIEL\n";
                else
                    cout<<"Case #"<<i<<": RICHARD\n";

            }

        }
    }
    out.close();
    in.close();
}

