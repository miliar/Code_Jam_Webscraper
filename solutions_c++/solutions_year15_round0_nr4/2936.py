#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("C:\\Users\\Saurabh Prakash\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh Prakash\\Desktop\\out.txt","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        int x,r,c;
        cin>>x>>r>>c;
        if(x==1)
            cout<<"Case #"<<cas++<<": GABRIEL\n";
        else if(x==2)
        {
            if((r*c)&1)
                cout<<"Case #"<<cas++<<": RICHARD\n";
            else
                cout<<"Case #"<<cas++<<": GABRIEL\n";
        }
        else if(x==3)
        {
            if(r*c%3==0 && (r!=1 && c!=1))
                cout<<"Case #"<<cas++<<": GABRIEL\n";
            else
                cout<<"Case #"<<cas++<<": RICHARD\n";
        }
        else if(x==4)
        {
            if(r*c%4!=0 || r==1 || c==1)
                cout<<"Case #"<<cas++<<": RICHARD\n";
            else if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4))
                cout<<"Case #"<<cas++<<": GABRIEL\n";
            else
                cout<<"Case #"<<cas++<<": RICHARD\n";
        }
    }

    return 0;
}
