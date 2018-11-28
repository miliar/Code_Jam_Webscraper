#include<bits/stdc++.h>
using namespace std;

#define l long long
#define pb(x) push_back(x)

int main()
{
    int t;
    cin>>t;
    for(int ix=1;ix<=t;ix++)
    {
        int x,r,c;
        cin>>x>>r>>c;
        cout<<"Case #"<<ix<<": ";
        if(x==1)
        {
            if(r*c%1==0)
            cout<<"GABRIEL"<<endl;
            else
            cout<<"RICHARD"<<endl;
        }
        else if(x==2)
        {
            if((r*c)%2==0)
            {
                cout<<"GABRIEL"<<endl;
            }
            else
            {
                cout<<"RICHARD"<<endl;
            }
        }
        else if(x==3)
        {
            if((r*c)==6||r*c==9||r*c==12)
            {
                cout<<"GABRIEL"<<endl;
            }
            else
            {
                cout<<"RICHARD"<<endl;
            }
        }
        else if(x==4)
        {
            if((r*c)==12||(r*c)==16)
            {
                cout<<"GABRIEL"<<endl;
            }
            else
            {
                cout<<"RICHARD"<<endl;
            }
        }
    }
}
