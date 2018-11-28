#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,c=0;
    cin>>t;
    while(t--)
    {
        int x,r,l,num,i;
        cin>>x>>r>>l;
        if(r*l>=(x*(x-1)))
        {
            if((r*l)%x==0)
                cout<<"Case #"<<c<<": GABRIEL"<<endl;
            else
                cout<<"Case #"<<c<<": RICHARD"<<endl;
        }
        else
        {
            cout<<"Case #"<<c<<": RICHARD"<<endl;
        }
    }
    return 0;
}
