
#include<iostream>
using namespace std;

int main()
{

    int T,r,c,x,k;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>x>>r>>c;
        if(x==1)
         cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
        else if(x==2 )
        {
            if((r*c%2==0))
             cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             else
             cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
        }

        else if(x==3 )

        {
            if((r*c)%3!=0)
            cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
            else
            if(r==1||c==1)
            cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
            else
            cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
        }
        else if(x==4)
        {
            if((r==4&&c==3)||(r==3&&c==4)||(r==4&&c==4))
            cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
            else
            cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;

        }

    }
}
