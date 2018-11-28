#include <iostream>
#include <string>

using namespace std;

string getit(int x,int m)
{
    string g = "GABRIEL";
    if(x==1)

            return g;
    else if(x==2)
        {
            if((m)%2==0) return g;
        }
    else if(x==3)
        {
         if(m%3==0 && m/3>1) return g;
        }
    else if(x==4)
        {
            if(m%4==0 && m/4>2) return g;

        }
    return "RICHARD";
}

int main()
{

    int tc;cin>>tc;
    for(int i=1;i<=tc;i++)
        {
            int x,r,c;
            cin>>x>>r>>c;
            cout <<"Case #"<<i<<": "<<getit(x,r*c)<<"\n";

        }

    return 0;

}

