#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<set>
#define ll long long int
#define mk make_pair
#define pb push_back
using namespace std;


int main()
{
    int t,w=1;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        int i,j,k,l,m,n,d,arr[1111]={0},co=0,ans=0,r,x,c;
        cin>>x>>r>>c;
        if(r>c) swap(r,c);
        if(x==1)
            cout<<"Case #"<<w<<": "<<"GABRIEL"<<"\n";
        else if(x==2&&(r*c)%2==0)
            cout<<"Case #"<<w<<": "<<"GABRIEL"<<"\n";
        else if((r*c)%x!=0)
            cout<<"Case #"<<w<<": "<<"RICHARD"<<"\n";
        else if(x>=7)
            cout<<"Case #"<<w<<": "<<"RICHARD"<<"\n";
        else if(c<x)
            cout<<"Case #"<<w<<": "<<"RICHARD"<<"\n";
        else if(c==x&&r<=(c-2))
            cout<<"Case #"<<w<<": "<<"RICHARD"<<"\n";
        else
            cout<<"Case #"<<w<<": "<<"GABRIEL"<<"\n";
        w++;
    }
    return 0;
}
