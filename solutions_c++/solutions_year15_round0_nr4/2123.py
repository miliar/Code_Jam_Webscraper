#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
        freopen("D-small-attempt1.in","r",stdin);
        freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int x,r,c;
    for(int t=0;t<T;t++)
    {
        cin>>x>>r>>c;
        if(x==1)cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
        else if(x==2)
        {
            if((r*c)%2==0)cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
            else cout<<"Case #"<<t+1<<": "<<"RICHARD"<<endl;
        }
        else if (x==3)
        {
            if((r*c)==6 || (r*c)==12 ||(r*c)==9)
            cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
            else
            cout<<"Case #"<<t+1<<": "<<"RICHARD"<<endl;
        }
        else if (x==4)
        {
            if((r*c)==16 || (r*c)==12)
            cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
            else
            cout<<"Case #"<<t+1<<": "<<"RICHARD"<<endl;
        }

    }
    return 0;
}
