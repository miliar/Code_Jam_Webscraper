#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int given[4][4][4]={{{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}},{{0,1,0,1},{1,1,1,1},{0,1,0,1},{1,1,1,1}},{{0,0,0,0},{0,0,1,0},{0,1,1,1},{0,0,1,0}},{{0,0,0,0},{0,0,0,0},{0,0,0,1},{0,0,1,1}}};
typedef long long ll;
int main()
{
    freopen("mn4.in","r",stdin);
    freopen("out.out","w",stdout);
    ll t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        ll x,r,c;
        cin>>x>>r>>c;
        if(given[x-1][r-1][c-1])
        {
            cout<<"GABRIEL";
        }
        else
        {
            cout<<"RICHARD";
        }
        cout<<endl;
    }
}
