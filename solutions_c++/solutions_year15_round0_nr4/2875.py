#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<string.h>
#include<queue>
#define M 1000000007
using namespace std;

main()
{
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long i,j,k,n,m,x,r,c,t,q;
    cin>>t;
    for(q=1;q<=t;q++)
    {
        cin>>x>>r>>c;
        if(((r*c)%x)!=0)
        {
            cout<<"Case #"<<q<<": "<<"RICHARD"<<endl;
            continue;

        }
        if((x>r&&x>c))
        {
            cout<<"Case #"<<q<<": "<<"RICHARD"<<endl;
            continue;

        }

        if(x==1)
        {
            cout<<"Case #"<<q<<": "<<"GABRIEL"<<endl;
            continue;
        }
        if(x==2)
        {
            cout<<"Case #"<<q<<": "<<"GABRIEL"<<endl;
            continue;


        }
        if(x==3)
        {
            if(r==3&&c==1||r==1&&c==3)
            {
                cout<<"Case #"<<q<<": "<<"RICHARD"<<endl;

            }
            else
            {
                cout<<"Case #"<<q<<": "<<"GABRIEL"<<endl;
            continue;
            }
        }
        if(x==4)
        {
            if(r<=2||c<=2)
            {
                cout<<"Case #"<<q<<": "<<"RICHARD"<<endl;

            }
            else
            {
                cout<<"Case #"<<q<<": "<<"GABRIEL"<<endl;

            }
        }


    }
    return 0;
}

