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
scanf("%lld\n",&t);
ll cas=1;
while(t--)
{
string s;
printf("Case #%lld: ",cas);
cas++;
deque<char> a;
a.clear();

getline(cin,s);
a.push_back(s[0]);
for(ll i=1;i<s.size();i++)
{
  if(s[i]>=a.front())
  a.push_front(s[i]);
  else
  a.pb(s[i]);
}
for(deque<char>::iterator i=a.begin();i!=a.end();i++)
{
    cout<<*i;
}
printf("\n");
}
return 0;}
