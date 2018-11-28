#include<iostream>
#include<cstring>
using namespace std;
int main(){
int cse,x,r,c,i=1,calc,d;
cin>>cse;
while(i<=cse)
{
    cin>>x>>r>>c;
    if(x==1)
            d=2;
    else if(x==2)
    {
        if(r%2==0||c%2==0)
            d=2;
        else
            d=0;
    }
    else if (x==3)
    {
        if(r>=2&&c>=2&&(r*c)%3==0)
            d=2;
        else
            d=0;
    }
    else if(x==4)
    {
        if(r>=3&&c>=3&&(r*c)%4==0)
            d=2;
        else
            d=0;
    }
    else if(x==5)
    {
        if(r*c>=20&&(r*c)%5==0)
            d=2;
        else
            d=0;
    }
    else if(x==6)
    {
        if((r*c)>=30&&(r*c)%6==0)
            d=2;
        else
            d=0;
    }
    else
        d=0;


    if(d==0)
       cout<<"Case #"<<i<<": RICHARD"<<endl;
    else
       cout<<"Case #"<<i<<": GABRIEL"<<endl;

    i++;
}
    return 0;
}
