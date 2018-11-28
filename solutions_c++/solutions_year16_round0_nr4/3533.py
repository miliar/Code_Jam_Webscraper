#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k,c,s;
    long long int kc,index;
    int i,j;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>k>>c>>s;
        kc=1;
        for(j=1;j<c;j++)
            kc*=k;
        index=1;
        cout<<"Case #"<<i<<": ";
        while(s){
            cout<<index<<" ";
            index+=kc;
            s--;
        }
        cout<<endl;
    }
    return 0;
}
