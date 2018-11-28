#include<iostream>
#include<string>
using namespace std;
int main()
{
    int t,w=1;
    cin>>t;
    while(t--)
    {
        int i=0,x=0,y=0,m=0,l,s=0;
        cin>>x;
        cin>>y;
        cout<<"Case #"<<w<<": ";
        if(x>0)
        {
            for(i=1;i<=x;i++)
                cout<<"WE";
        }
        else if(x<0)
        {
            m=0-x;
            for(i=1;i<=m;i++)
            cout<<"EW";
        }
        if(y>0)
        {
            for(i=1;i<=y;i++)
                cout<<"SN";
        }
        else if(y<0)
        {   m=0-y;
            for(i=1;i<=m;i++)
            cout<<"NS";
        }
            cout<<endl;
        w++;
    }
    return 0;
}
