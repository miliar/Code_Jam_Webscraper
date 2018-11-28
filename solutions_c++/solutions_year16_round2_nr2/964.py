#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

typedef pair<int, pair<string, string> > best;

best bourrin(string a, string b)
{
  for (int i=0; i<a.size(); i++)
  {
    if (a[i] == '?')
    {
      best res = make_pair(1000000000, make_pair("", ""));
      for (char c = '0'; c<='9'; c++)
      {
        a[i] = c;
        res = min(res, bourrin(a, b));
      }
      return res;
    }
  }
  
  for (int i=0; i<b.size(); i++)
  {
    if (b[i] == '?')
    {
      best res = make_pair(1000000000, make_pair("", ""));
      for (char c = '0'; c<='9'; c++)
      {
        b[i] = c;
        res = min(res, bourrin(a, b));
      }
      return res;
    }
  }
  
  int x = 0, y = 0;
  for (int i=0; i<a.size(); i++)
    x = x * 10 + a[i] - '0';
  for (int i=0; i<b.size(); i++)
    y = y * 10 + b[i] - '0'; 
  
  return make_pair(abs(x - y), make_pair(a, b));
}

void main2()
{
  string a, b;
  cin >> a >> b;
  
  pair<string, string> res = bourrin(a, b).second;
  cout << res.first << " " << res.second << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
