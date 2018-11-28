#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define mod 1000000007

int main()
{
    ifstream cin("inp.in");
    ofstream cout("out.txt");
    int t;
    ll i=1;
    cin>>t;
    while(t--){
        ll N;
        cin>>N;
        bool a[10];
        memset(a,false,sizeof(a));
        ll rem=10;
        if(N==0){
            cout<<"Case #"<<i++<<": ";
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        ll K = N;
        while(rem!=0){
            ll x=N;
            while(x!=0){
                int r=x%10;
                if(a[r]==false){
                    a[r]=true;
                    rem--;
                }
                x=x/10;
            }
            N+=K;
        }
        cout<<"Case #"<<i++<<": ";
            cout<<N-K<<" ";
        cout<<endl;
    }
    return 0;
}
