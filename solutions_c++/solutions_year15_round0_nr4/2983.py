#include<iostream>
#include<stdio.h>
using namespace std;
int minn(int a,int b)
{
    return(a<b?a:b);
}
int check(int a,int b,int r,int c)
{
    if((a==r&&b==c)||(a==c&&b==r))
    return 1;
    else
        return 0;
}
int main()
{
    int t,j=1,a,x,c,r;
    freopen ( "D-small-attempt2.in", "r", stdin );
    freopen ("output17.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        cin>>x>>c>>r;
        a=r*c;
       if(minn(c,r)==1)
        {
            if((check(1,1,r,c)&&(x==2||x==3||x==4))||(check(1,2,r,c)&&(x==3||x==4))||(check(1,4,r,c)&&(x==3||x==4))||(check(1,3,r,c)&&(x==3||x==2||x==4)))
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
            else
              cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
        }
        else if(minn(c,r)==2)
        {
            if((check(2,2,r,c)&&(x==3||x==4))||(check(2,3,r,c)&&(x==4))||(check(2,4,r,c)&&(x==3||x==4)))
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
            else
              cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
        }
        else if(minn(c,r)==3)
        {
            if((check(3,3,r,c)&&(x==2||x==4)))
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
            else
              cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
        }
        else
        {
            if(x==3)
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
            else
              cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
        }

        j++;
    }
    return 0;
}
