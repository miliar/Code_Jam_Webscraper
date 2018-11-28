#include<bits/stdc++.h>
using namespace std;
#define ll long long
int solve(int n)
{
    map<int,int>mp;
    int temp,mir;
    for(int i=1;; i++)
    {
        mir=temp=n*i;
        while(temp)
        {
            mp[temp%10]++;
            temp/=10;
        }
        if(mp.size()==10)
            return mir;
    }
}
int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,n;
    cin>>t;
    for(int c=1; c<=t; c++)
    {
        cin>>n;
        if(n)
            cout<<"Case #"<<c<<": "<<solve(n)<<endl;
        else
            cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
    }
    return 0;
}

