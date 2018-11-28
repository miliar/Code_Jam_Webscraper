#include <bits/stdc++.h>
using namespace std;

#define endl "\n"
typedef long long int ll;

int main()
{
  ios::sync_with_stdio(false);  cin.tie(0);  cout.tie(0);
  
  ll t, n, teste=1, i;
  
  cin >> t;
  while(t--)
  {
    cin >> n;
    set<ll> s;
    for(i = 0; i < 10; i++) s.insert(i);
    
    ll temp=n;
    for(i = 1; i < 100; i++)
    {
      temp = i*n;
      while(temp!=0)
      {
        s.erase(temp%10);
        temp/=10;
      }
      if(s.size()==0) break;
    }
    
    if(s.size()!=0)
    {
      cout << "Case #" << teste++ << ": INSOMNIA\n";
    }
    else
    {
      cout << "Case #" << teste++ << ": " << i*n << endl;
    }
  }
  
  return 0;
}
