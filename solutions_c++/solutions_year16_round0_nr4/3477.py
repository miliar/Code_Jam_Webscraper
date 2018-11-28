#include <iostream>
#include <stdio.h>
#include<string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
typedef long long int ll;
map<ll,ll>m;

int main()
{
    freopen("in", "r",stdin );
    freopen("out.txt", "w",stdout );

    ll t;cin>>t;
    for(ll i=1;i<=t;i++){
       cout<<"Case #"<<i<<": ";
       int k;cin>>k;
       int c;cin>>c;
       int s;cin>>s;
       for(int j = 1;j<=s;j++)cout<<j<<" ";
       cout<<"\n";
    }
    return 0;
}
