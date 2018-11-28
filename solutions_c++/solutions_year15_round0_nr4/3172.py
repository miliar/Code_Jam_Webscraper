#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.txt", "w", stdout);
    int t = 0;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        int x,r,c;
        string s;
        cin>>x>>r>>c;
        s = "";
        if(x==1)
        {
            s="GABRIEL";
        }
        else if(x==2)
        {
            if(r*c%2==0)
            {
                s="GABRIEL";
            }
            else
            {
                s="RICHARD";
            }
        }
        else if(x==3)
        {
            if(r*c%3==0 && r*c>=6)
            {
                s="GABRIEL";
            }
            else
            {
                s="RICHARD";
            }
        }
        else if(x==4)
        {
            if(r*c>=12)
            {
                s="GABRIEL";
            }
            else
            {
                s="RICHARD";
            }
        }
        cout<<"Case #"<<tc<<": "<<s<<endl;
    }
    return 0;
}
