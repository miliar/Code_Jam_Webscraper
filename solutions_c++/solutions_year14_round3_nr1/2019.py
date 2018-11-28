#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;
typedef long long ll;
ll gcd(ll a, ll b)
{
  ll c = a % b;
  while(c != 0)
  {
    a = b;
    b = c;
    c = a % b;
  }
  return b;
}

bool isPowerOfTwo(ll n)
{
  if (n == 0)
    return 0;
  while (n != 1)
  {
    if (n%2 != 0)
      return 0;
    n = n/2;
  }
  return 1;
}


int main() {
    freopen("inA.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        ll p,q;
        char ch;
        cin>>p>>ch>>q;
        ll x= gcd(p,q);

        p = p/x;
        q = q/x;
        if(!isPowerOfTwo(q)) cout<<"Case #"<<i<<": impossible"<<endl;
        else {
            int j;
            for(j=1;;j++) {
                p = p*2;
                if(p>=q) break;
            }
            cout<<"Case #"<<i<<": "<<j<<endl;
        }
    }
    return 0;
}
