#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        int n,r,c,te;
        cin>>n>>r>>c;
        if(r>c)te=r,r=c,c=te;
        //cout<<r<<" "<<c<<endl;
        string win;
        if(n==4)
        {
            if(r==1||r==2)win="RICHARD";
            else if(r==3)
            {
                if(c==3)win="RICHARD";
                else if(c==4)win="GABRIEL";
            }
            else if(r==4)
            {
                win="GABRIEL";
            }
        }
        else if(n==1)
        {
            win="GABRIEL";
        }
        else if(n==2)
        {
            if((r*c)%2==0)win="GABRIEL";
            else if((r*c)%2==1)win="RICHARD";
        }
        else if(n==3)
        {
            if(r==1)win="RICHARD";
            else if(r==2)
            {
                if(c==3)win="GABRIEL";
                else if(c==2||c==4)win="RICHARD";
            }
            else if(r==3)
            {
                win="GABRIEL";
            }
            else if(r==4)
            {
                win="RICHARD";
            }
        }
        cout<<"Case #"<<tci<<": "<<win<<endl;
    }
    return 0;
}
