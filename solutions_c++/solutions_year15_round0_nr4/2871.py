#include <cmath>
#include <cstdio>
#include <iostream>
using namespace std;


int main()
{
    int T,X,R,C,l=1;
    freopen("om_in.txt","r",stdin);
    freopen("om_out.txt","w",stdout);
    cin>>T;
    while(l<=T)
    {
        cin>>X>>R>>C;
        cout<<"Case #"<<l<<":"<<" ";
        switch(X)
        {
            case 1:
             cout<<"GABRIEL"<<endl;
             break;
            case 2:
             (R*C<X || (R*C%2!=0))?cout<<"RICHARD"<<endl:cout<<"GABRIEL"<<endl;
              break;
            case 3:
             (R*C<=X || (R*C%3!=0))?cout<<"RICHARD"<<endl:cout<<"GABRIEL"<<endl;
              break;
            case 4:
             ((R*C==16) || (R*C%12==0))?cout<<"GABRIEL"<<endl:cout<<"RICHARD"<<endl;
        }

        l++;
    }

    return 0;
}

