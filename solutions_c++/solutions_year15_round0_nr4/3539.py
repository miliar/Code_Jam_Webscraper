#include<iostream>
using namespace std;

int main()
{
    int T,i,x,r,c;
    cin>>T;

    for(i=0;i<T;++i)
    {
        cout<<"Case #"<<i+1<<": ";
        cin>>x>>r>>c;

        if(x>=7)
            cout<<"RICHARD";
        else
        {
            if(r*c%x==0)
            {
              if(r>=x-1&&c>=x-1)
                cout<<"GABRIEL";
                else
                cout<<"RICHARD";
            }
            else
                cout<<"RICHARD";
        }
        cout<<"\n";
    }
}
