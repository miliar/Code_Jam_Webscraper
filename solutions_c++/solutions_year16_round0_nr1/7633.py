#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define mod 1000000007

int main()
{
    ifstream cin("input2.in");
    ofstream cout("cj1.txt");
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        ll n;
        cin>>n;
        bool a[10];
        memset(a,false,sizeof(a));
        int rem=10;
        if(n==0)
        {
            cout<<"Case #"<<z<<": ";
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        int N=n;
        while(rem!=0)
        {
            ll x=n;
            while(x!=0)
            {
                int r=x%10;
                if(a[r]==false)
                {
                    a[r]=true;
                    rem--;
                }
                x=x/10;
            }
            n+=N;
        }
        cout<<"Case #"<<z<<": ";
            cout<<n-N<<" ";
        cout<<endl;
    }
    return 0;
}
