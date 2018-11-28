#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    freopen ("D-small-attempt0.in","r",stdin);
    freopen ("output.txt","w",stdout);
    int T,R,C,X,i;
    cin>>T;
    for(i=0;i<T;++i)
    {
        cin>>X>>R>>C;
        if(X==1)
        {
            cout<<"Case #"<<i+1<<": "<<"GABRIEL\n";
        }
        else if(X==2)
        {
            if( R%2==0 || C%2==0 )
                cout<<"Case #"<<i+1<<": "<<"GABRIEL\n";
            else
                cout<<"Case #"<<i+1<<": "<<"RICHARD\n";
        }
        else if(X==3)
        {
            if( (R==3 && C!=1)||(R!=1 && C==3) )
                cout<<"Case #"<<i+1<<": "<<"GABRIEL\n";
            else
                cout<<"Case #"<<i+1<<": "<<"RICHARD\n";
        }
        else if(X==4)
        {
            if( (R==4 && C>2)||(R>2 && C==4) )
                cout<<"Case #"<<i+1<<": "<<"GABRIEL\n";
            else
                cout<<"Case #"<<i+1<<": "<<"RICHARD\n";
        }
    }
    return 0;
}
