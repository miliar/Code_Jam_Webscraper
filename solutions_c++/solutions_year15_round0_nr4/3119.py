#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,x,r,c,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
       cin>>x>>r>>c;
       cout<<"Case #"<<j<<": ";
       if((r*c)%x != 0)
       {
           cout<<"RICHARD"<<endl;
           continue;
       }
       if(x == 1)
       {
           cout<<"GABRIEL"<<endl;
       }
       else if( x == 2)
       {
           cout<<"GABRIEL"<<endl;
       }
       else if( x == 3 )
       {

           if(r >= 2 && c >= 2)
            cout<<"GABRIEL"<<endl;
           else
            cout<<"RICHARD"<<endl;
       }
       else if(x == 4)
       {
           if(r >= 3 && c >= 3)
            cout<<"GABRIEL"<<endl;
           else
            cout<<"RICHARD"<<endl;
       }
    }
    return 0;
}
