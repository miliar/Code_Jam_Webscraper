#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{   freopen("D-small-attempt0.in","r",stdin);
    freopen("omino_out.txt","w",stdout);
    int t,x,r,c,k=0,p;
    cin>>t;
    while(k<t)
    {
        cin>>x>>r>>c;
        p=r*c;
        if(x==1)
        {
        cout<<"Case #"<<k+1<<": "<<"GABRIEL"<<endl;
        }
        else if(x==2)
        {
            if(p&1)
        cout<<"Case #"<<k+1<<": "<<"RICHARD"<<endl;
        else
        cout<<"Case #"<<k+1<<": "<<"GABRIEL"<<endl;


        }
        else if(x==3)
        {
            if(p<=3)
            {        cout<<"Case #"<<k+1<<": "<<"RICHARD"<<endl;
            }
            else if(p%3!=0)
            {
                        cout<<"Case #"<<k+1<<": "<<"RICHARD"<<endl;

            }
            else
                     cout<<"Case #"<<k+1<<": "<<"GABRIEL"<<endl;

        }
        else if(x==4)
        {
            if(p==12 || p==16)
            {
                cout<<"Case #"<<k+1<<": "<<"GABRIEL"<<endl;

            }
            else
                cout<<"Case #"<<k+1<<": "<<"RICHARD"<<endl;


        }
        k++;
    }
    return 0;
}
