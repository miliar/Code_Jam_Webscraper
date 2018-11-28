#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("Dso.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<i<<": ";
        for(int j=1;j<=k;j++)
            cout<<j<<" ";
        cout<<"\n";
    }


    return 0;
}


