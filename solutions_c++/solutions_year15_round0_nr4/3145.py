#include<iostream>
using namespace std;

int main()
{
    int t,X,R,C;
    int tst=0;

    cin>>t;

    while(t--)
    {
        tst++;
        cin>>X;
        cin>>R;
        cin>>C;

        if(X==1)
            cout<<"Case #"<<tst<<": GABRIEL"<<endl;
        else if(X==2)
        {
            if(R*C%2==0)
                cout<<"Case #"<<tst<<": GABRIEL"<<endl;
            else
                cout<<"Case #"<<tst<<": RICHARD"<<endl;
        }
        else if(X==3)
        {
            if(R*C==6 || R*C==9 || R*C==12)
                cout<<"Case #"<<tst<<": GABRIEL"<<endl;
            else
                cout<<"Case #"<<tst<<": RICHARD"<<endl;
        }
        else
        {
            if(R*C==16 || R*C==12)
                cout<<"Case #"<<tst<<": GABRIEL"<<endl;
            else
                cout<<"Case #"<<tst<<": RICHARD"<<endl;
        }

    }
    return 0;
}
