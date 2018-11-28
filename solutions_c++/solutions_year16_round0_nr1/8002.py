#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define lim ((ll)(1e5)+5)
#define F first
#define S second
#define D double
#define mod ((ll)(1e9)+7)
#define pq priority_queue
#define vl vector<ll>
#define pll pair<ll,ll>
#define vll vector<pll>
#define inf ((ll)(1e17)+7)
ll zero=0;
ll one=1;

int main()
{
ll t,temp;
ll coun=0;
scanf("%lld",&t);
while(t--)
{
    ll n;
    coun++;
    printf("Case #%lld: ",coun);
    set<ll>s;
    s.clear();
    ll i=1;
    ll flag=0;
    scanf("%lld",&n);
    if(n==0)
    {
    printf("INSOMNIA\n");
    }
    else
    {
    	while(s.size()!=10)
    	{
        temp=i*n;
        while(temp!=0)
        {
        s.insert(temp%10);
        temp/=10;
        }

        i++;
    	}
    }
   if(s.size()==10)
   printf("%lld\n",(i-1)*n);

}
return 0;}
