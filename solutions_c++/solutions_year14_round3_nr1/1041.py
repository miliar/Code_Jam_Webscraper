#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<stack>

#define ull unsigned long long

using namespace std;

ull gcd(ull p, ull q)
{
  if (p == 0)
    return q;
  if (q == 0)
    return p;
  if (p > q)
    return (gcd(p%q, q));
  else
    return (gcd(p, q%p));
}

void red (ull &p, ull &q)
{
  ull nd = gcd(p, q);
  p = p/nd;
  q = q/nd;
}

void find(ull &p, ull &q, string s)
{
    int k = 0;
    p = 0, q = 0;
    while (s[k] >= '0' && s[k] <= '9' && k < (int)s.size())
    {
			 p = p*10 + s[k] - '0';
       k++;
    }
    k++;
    while (s[k] >= '0' && s[k] <= '9' && k < (int)s.size())
    {
			 q = q*10 + s[k] - '0';
       k++;
    }
}

void go(ull p, ull q)
{
  int k = 1;
  while (k <= 40 && (1 << k)*p < q)
    k++;
  if (k >= 41)
  {
    cout << "impossible";
  }
  else
    cout << k; 
} 

bool check(ull p, ull q)
{
  if (p > q)
  {
    cout << "impossible"; return false;
  }
  if (p == q)
  {
		cout << 0; return false;
  }
  ull k = 1;
  for (int i = 1; i <= 40; i++)
  {
//    cout << q << " " << k << " " << i << endl;
    k = k*2;
    if (q == k)
      return true;
  }
  cout << "impossible"; return false;
}

int main()
{ 
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  string s;
  ull p, q;
  int t;
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    cin >> s;
    find (p, q, s);
    red(p, q);
  //  cout << p << " " << q << endl;
    cout << "Case #" << i  +1 << ": ";
    if (check(p, q))
      go(p, q);
    cout << endl;
  }
  return 0;
}
