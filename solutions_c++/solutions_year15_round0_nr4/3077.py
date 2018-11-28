#include <iostream>
using namespace std;

int main()
{   int i,t,x,y,z;
    cin>>t;
    for(i=1;i<=t;++i)
    {   cin>>x>>y>>z;
        if(x==1)
           cout<<"Case #"<<i<<": GABRIEL \n";
        if((x==2)&&((y*z)%2==0))
             cout<<"Case #"<<i<<": GABRIEL \n";
        else if(x==2)
            cout<<"Case #"<<i<<": RICHARD \n";
        if((x==3)&&((y==3&&z>1)||(z==3&&y>1)))
            cout<<"Case #"<<i<<": GABRIEL \n";
        else if(x==3)
            cout<<"Case #"<<i<<": RICHARD \n";
        if((x==4)&&((y==4&&z>2)||(z==4&&y>2)))
            cout<<"Case #"<<i<<": GABRIEL \n";
        else if(x==4)
            cout<<"Case #"<<i<<": RICHARD \n";
    }
    return 0;
}