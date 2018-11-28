#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<climits>
#define ll long long
using namespace std;

int main()
{
    ll t,y=1;
    string s;
    freopen("iy.in","r",stdin);
    freopen("oy.out","w",stdout);
    cin>>t;
    while(t--)
    {
        string s1;
        cin>>s;
        ll n=s.length();
        s1=s[0];
        for(int i=1;i<n;i++)
        {
            if(s[i]<s1[0])
                s1=s1+s[i];
            else
                s1=s[i]+s1;
        }
        cout<<"Case #"<<y<<": "<<s1<<endl;
        y++;
    }
return 0;
}
