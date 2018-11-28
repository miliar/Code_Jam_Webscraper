#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll d[1000010]={0};
int main()
{
    ll t,n,r;
    d[0]=0;
    d[1]=1;
    string s;
    for(ll i=2;i<1000010;i++)
    d[i]=INT_MAX;
    for(ll i=1;i<1000000;i++)
    {
        s=to_string(i);
        reverse(s.begin(),s.end());
        r=stoi(s);
        d[i+1] = min(d[i+1], d[i] + 1);
		d[r] = min(d[r], d[i] + 1);
    }
    scanf("%lld",&t);
    int j=1;
    while(t--)
    {
        scanf("%lld",&n);
        printf("Case #%d: %lld\n",j,d[n]);
        j++;
    }
}
