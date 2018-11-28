#include<iostream>
using namespace std;

int p,q,r,s,countt;
int o[100],e[100];

void check(int v,int i)
{
    if(v==p){e[i]=v; countt++;}
    if(v==q){e[i]=v;countt++;}
    if(v==r){e[i]=v;countt++;}
    if(v==s){e[i]=v;countt++;}
}

int main()
{
    int t,a1,a2;
    int a,b,c,d;
    int m1[16],m2[16];
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>a1;
        for(int j=0;j<16;j++)
            cin>>m1[j];
        cin>>a2;
        for(int j=0;j<16;j++)
            cin>>m2[j];

        a=m1[(a1-1)*4+0];
        b=m1[(a1-1)*4+1];
        c=m1[(a1-1)*4+2];
        d=m1[(a1-1)*4+3];

        p=m2[(a2-1)*4+0];
        q=m2[(a2-1)*4+1];
        r=m2[(a2-1)*4+2];
        s=m2[(a2-1)*4+3];

        check(a,i);
        check(b,i);
        check(c,i);
        check(d,i);
        o[i]=countt;
        countt=0;
    }

    for(int i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        if(o[i]==0)
            cout<<"Volunteer cheated!\n";
        else if(o[i]==1)
            cout<<e[i]<<"\n";
        else if(o[i]>1)
            cout<<"Bad magician!\n";
    }
    return 0;
}
