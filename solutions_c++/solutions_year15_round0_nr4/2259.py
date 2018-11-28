#include <iostream>

using namespace std;

int main()
{
    int z;
    cin>>z;

    for(int t=1; t<=z; t++)
    {
        int x, r, c;
        cin>>x>>r>>c;

        if(x==1) cout<<"Case #"<<t<<": GABRIEL"<<endl;
        if(x==2)
        {
            if((r*c)%2==0)cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else cout<<"Case #"<<t<<": RICHARD"<<endl;
        }
        if(x==3)
        {
            if(r==3 && c==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else if(r==3 && c==2) cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else if(r==2 && c==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else if(r==3 && c==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else if(r==4 && c==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else cout<<"Case #"<<t<<": RICHARD"<<endl;
        }

        if(x==4)
        {
            if(r==4 && c==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else if(r==3 && c==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else if(r==4 && c==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
            else cout<<"Case #"<<t<<": RICHARD"<<endl;
        }
    }

    return 0;
}
