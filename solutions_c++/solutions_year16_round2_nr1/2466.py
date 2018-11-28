#include<bits/stdc++.h>
using namespace std;
void p(int n,int a)
{
    while(n--)
    {
        cout<<a;
    }
}
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;++i)
    {
        string S;
        S.reserve(3000);
        cin>>S;
        int a[100]={0};
        for(int j=0;j<S.length();j++)
        {
            a[S[j]]++;
        }
        cout<<"Case #"<<i<<": ";
        if(a['Z'])
        {
            int n=a['Z'];
            a['Z']=0;
            a[0]=n;
            a['E']-=n;
            a['R']-=n;
            a['O']-=n;
        }
        if(a['W'])
        {
            int n=a['W'];
            a['W']=0;
            a[2]=n;
            a['T']-=n;
            a['O']-=n;
        }
        if(a['G'])
        {
            int n=a['G'];
            a['G']=0;
            a[8]=n;
            a['E']-=n;
            a['I']-=n;
            a['H']-=n;
            a['T']-=n;
        }
        if(a['T'])
        {
            int n=a['T'];
            a['T']=0;
            a[3]=n;
            a['E']-=n;
            a['R']-=n;
            a['E']-=n;
            a['H']-=n;
        }
        if(a['R'])
        {
            int n=a['R'];
            a['R']=0;
            a[4]=n;
            a['F']-=n;
            a['O']-=n;
            a['U']-=n;
        }
        if(a['O'])
        {
            int n=a['O'];
            a['O']=0;
            a[1]=n;
            a['N']-=n;
            a['E']-=n;
        }
        if(a['F'])
        {
            int n=a['F'];
            a['F']=0;
            a[5]=n;
            a['I']-=n;
            a['V']-=n;
            a['E']-=n;
        }
        if(a['X'])
        {
            int n=a['X'];
            a['X']=0;
            a[6]=n;
            a['I']-=n;
            a['S']-=n;
        }
        if(a['S'])
        {
            int n=a['S'];
            a['S']=0;
            a[7]=n;
            a['E']-=n;
            a['V']-=n;
            a['E']-=n;
            a['N']-=n;
        }
        if(a['I'])
        {
            int n=a['I'];
            a['I']=0;
            a[9]=n;
            a['N']-=n;
            a['N']-=n;
            a['E']-=n;
        }
        for(int j=0;j<=9;j++)
        {
            p(a[j],j);
        }
        cout<<endl;
    }
}
