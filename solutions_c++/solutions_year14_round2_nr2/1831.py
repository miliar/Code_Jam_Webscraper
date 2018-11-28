#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define ll long long
using namespace std;

int num, i, j, t, a, b, k, ans;

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("B-small-attempt0.in","r",stdin);
    freopen("1.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        num++;
        ans=0;
        cin>>a>>b>>k;
        for(i=0; i<a; i++)
            for(j=0; j<b; j++)
                if((i&j)<k)ans++;
        cout<<"Case #"<<num<<": "<<ans<<endl;
    }
}
