#include <bits/stdc++.h>
using namespace std;
#define GAB(k)  cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl
#define RIC(k)  cout<<"Case #"<<k<<": "<<"RICHARD"<<endl

int main()
{
    int t,k=1;
    cin>>t;
    while(t--)
    {
        int X,R,C,temp=0;
        cin>>X>>R>>C;
        temp=R*C;
        if(X==1)
            GAB(k);
        else if(X==2 && temp%2==1)
            RIC(k);
        else if(X==2 && temp%2!=1)
            GAB(k);
        else if(X==3 && temp==3)
            RIC(k);
        else if(X==3 && temp%3!=0)
            RIC(k);
        else if(X==3)
            GAB(k);
        else if(X==4 && (temp>11))
            GAB(k);
        else if(X==4)
            RIC(k);
        k++;
    }
    return 0;
}
