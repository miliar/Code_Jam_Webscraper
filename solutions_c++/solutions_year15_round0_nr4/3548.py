#include <iostream>

using namespace std;

int main()
{
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        int x,r,c;
        cin>>x>>r>>c;

        if(x==1)
            cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
        else if(x==2)
        {
            if(r*c%x!=0)
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
            else
                cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
        }
        if(x==4)
        {
            if(r*c%x!=0||c<=2||r<=2)
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
            else
                cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;

        }
        if(x==3)
        {
            if(r*c%x!=0||(r!=3&&c!=3)||(r==3&&(c<2||c>4))||(c==3&&(r<2||r>4)))
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
            else
                cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
        }

    }
    return 0;
}
