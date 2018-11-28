#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int x,r,c;
        cin>>x>>r>>c;
        if(r < c)
            swap(r,c);
        cout<<"Case #"<<i<<": ";
        if(x == 4)
        {
            if(r < 4 || (r==4 && c<=2))
                cout<<"RICHARD"<<endl;
            else
                cout<<"GABRIEL"<<endl;
        }
        else if(x == 3)
        {
            if(r < 3 || (r==4 && c!=3) || (r==3 && c == 1))
                cout<<"RICHARD"<<endl;
            else
                cout<<"GABRIEL"<<endl;
        }
        else if(x == 2)
        {
            if((r < 2)||(r==3 && c!=2))
                cout<<"RICHARD"<<endl;
            else
                cout<<"GABRIEL"<<endl;
        }
        else
        {
            cout<<"GABRIEL"<<endl;
        }
    }
    return 0;
}
