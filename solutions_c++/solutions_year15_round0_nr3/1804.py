#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    ll t;
    scanf("%lld",&t);
    for(ll cases=1;cases<=t;cases++)
    {
        char temp;
        bool minm=false;
        bool result=false;
        ll row,col;
        string strng;
        ll l,x;
        scanf("%lld%lld",&l,&x);
        cin>>strng;
        char graphs[4][4]={
            {'1','i','j','k'},
            {'i','1','k','j'},
            {'j','k','1','i'},
            {'k','j','i','1'}
        };
        bool graphval[4][4]={
            {true,true,true,true},
            {true,false,true,false},
            {true,false,false,true},
            {true,true,false,false}
        };
        ll tt=0,ctr=0;//tt->F
        temp='1';
        char intermediate[3];
        for(ll i=1;i<=x;i++)
        {
            for(ll j=0;j<l;j++)
            {
                if(temp=='1')   row=0;
                else if(temp=='i')      row=1;
                else if(temp=='j')      row=2;
                else if(temp=='k')       row=3;
                if(strng[j]=='1')   col=0;
                else if(strng[j]=='i')    col=1;
                else if(strng[j]=='j')    col=2;
                else if(strng[j]=='k')    col=3;
                temp=graphs[row][col];
                if(graphval[row][col]==false)   minm=(!minm);
                if(ctr==0&&temp=='i')
                {
                    ctr++;
                    intermediate[0]=temp;
                    temp='1';
                }
                else if(ctr==1&&temp=='j')
                {
                    ctr++;
                    intermediate[1]=temp;
                    temp='1';
                }
                else if(ctr==2&&temp=='k'&&i==x&&j==l-1)
                {
                    ctr++;
                    intermediate[2]=temp;
                    temp='1';
                }
            }
        }
        if(minm==false && ctr==3)   result=true;
        if(result==true)
            printf("Case #%d: YES\n",cases);
        else
            printf("Case #%d: NO\n",cases);
    }
}

