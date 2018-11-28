#include<bits/stdc++.h>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
int main()
{
    //READ("D-small-attempt1.in");
    //WRITE("D-small-attempt1.out");
    int t,x,r,c;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        string s="";
        cin>>x>>r>>c;
        if(x == 1)
            s = "GABRIEL";
        else if(x == 2)
        {
            if(r%2 == 0 || c%2 == 0)
                s="GABRIEL";
            else
                s="RICHARD";
        }
        else if(x == 3)
        {
            if(r*c <6)
                s="RICHARD";
            else if(r%3 == 0 || c%3 == 0)
                s="GABRIEL";
            else
                s="RICHARD";
        }
        else if(x == 4)
        {
            if(r*c >= 12)
                s="GABRIEL";
            else
                s="RICHARD";
        }
        cout<<"Case #"<<i+1<<": "<<s<<endl;
    }
}
