#include<bits/stdc++.h>
using namespace std;
main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("outD.txt","w",stdout);
    int tc;
    cin>>tc;
    for(int i=0;i<tc;i++)
    {
        string name;
        int a,b,c;
        cin>>a>>b>>c;
        if(a==1) name="GABRIEL";
        else if(a==2)
        {
            if(b*c%2==0)name="GABRIEL";
                else name="RICHARD";
        }
         else if(a==3)
        {
            if(b*c%3==0&&c*b>=6)name="GABRIEL";
                else name="RICHARD";
        }
        else if(a==4)
        {
            if(c*b>=12)name="GABRIEL";
                else name="RICHARD";
        }
        cout<<"Case #"<<i+1<<": "<<name<<endl;
    }
}
