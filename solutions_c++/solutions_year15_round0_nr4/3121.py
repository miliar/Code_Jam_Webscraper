#include<iostream>
using namespace std;

int main()
{
    int t,x,r,c,test=0;

    cin>>t;

    while(t--)
    {
        test++;
        cin>>x;
        cin>>r;
        cin>>c;

        if(x==1)
            cout<<"Case #"<<test<<": GABRIEL"<<endl;
        else if(x==2)
        {
            if(r*c%2==0)
                cout<<"Case #"<<test<<": GABRIEL"<<endl;
            else
                cout<<"Case #"<<test<<": RICHARD"<<endl;
        }
        else if(x==3)
        {
            if(r*c==6 || r*c==9 || r*c==12)
                cout<<"Case #"<<test<<": GABRIEL"<<endl;
            else
                cout<<"Case #"<<test<<": RICHARD"<<endl;
        }
        else
        {
            if(r*c==16 || r*c==12)
                cout<<"Case #"<<test<<": GABRIEL"<<endl;
            else
                cout<<"Case #"<<test<<": RICHARD"<<endl;
        }

    }
    return 0;
}
