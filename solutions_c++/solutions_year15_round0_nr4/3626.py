#include <iostream>
#include <string>
#include <fstream>
using namespace std;



int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("solution.txt","w",stdout);

    int t,x,r,c;
    cin>>t;
    string winner;
    for(int i=1; i<=t; ++i)
    {
        cin>>x>>r>>c;
        if ((r*c)%x==0)
        {
            if(x%2==0)
            {
                if( ((x/2)>=r || (x/2)>=c) && x!=2)//x/2  >=
                    winner="RICHARD";
                else
                    winner="GABRIEL";
            }
            else if(x/2>=r || x/2>=c)
                winner="RICHARD";
            else
                winner="GABRIEL";
        }
        else
            winner="RICHARD";
        cout<<"Case #"<<i<<": "<<winner<<endl;
    }
    return 0;
}
