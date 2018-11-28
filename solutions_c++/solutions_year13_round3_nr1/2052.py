#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

typedef long long ll;

string s;

ll f(string x, ll n)
{
  ll k = x.size(), cnt = 0;
  for(int i = 0; i <= k; i++)
  {
    ll p = k - 1;
    while(p - i >= n - 1)
    {
      ll answ = 0;
      for(ll j = i; j <= p; j++)
       {
          if(x[j] != 'a' && x[j] != 'e' && x[j] != 'o' && x[j] != 'u' && x[j] != 'i') answ++;
          else if(answ < n) answ = 0;
          if(answ >= n) break;
       }
      if(answ >= n) cnt++;
      p--;
    }
  }
  return cnt;
}
int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  ll n, t;
  cin >> t;
  for(int i = 0; i < t; i++)
  {
    cin >> s >> n;
    cout << "Case #" <<  i + 1 << ": " << f(s, n) << endl;
  }
  return 0;
}
