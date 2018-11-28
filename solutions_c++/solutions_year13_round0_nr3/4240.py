#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;
const ll MAXR = 1e7;


ll a[126];
int t, j;

bool calc(ll x)
{
  string s;
  while(x > 0)
  {
    s += char('0' + (x % 10));
    x /= 10;
  }
  int n = s.size();
  for(int i = 0; i < n / 2; i++)
    if(s[i] != s[n - i - 1]) return false;
  return true;
}

void op()
{
  for(ll i = 1; i <= MAXR; i++)
  {
    if(calc(i) && calc(i*i)) a[j++] = i * i;
  }
}

int get_pos(ll x)
{
  int l = 0, r = j, m;
  while(l < r)
  {
    m = (l + r) / 2;
    if(a[m] < x) l = m + 1;
    else r = m;
  }
  return l;
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t;
  op();
  for(int i = 0; i < t; i++)
  {
    ll l, r;
    cin >> l >> r;

    int l_ind = get_pos(l);
    int r_ind = get_pos(r + 1) - 1;

    cout << "Case #" << i + 1 << ": " << r_ind - l_ind + 1 << endl;
  }
  return 0;
}
