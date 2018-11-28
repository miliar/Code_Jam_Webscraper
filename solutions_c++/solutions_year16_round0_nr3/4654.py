#include <bits/stdc++.h>

#define DEBUG

#ifdef DEBUG
#define DBG(...) printf(__VA_ARGS__)
#else
#define DBG(...)
#endif

using namespace std;

typedef long long ll;

ll levels;
ll J, N;

void search(string seq, ll level)
{
  if (level == levels)
  {
    bool jamcoin = true;
    string num = "1" + seq + "1";
    vector<ll> divs(15, 0);
    for (ll b=2; b<=10; b++)
    {
      char *ptr;
      ll inbase = strtoll(num.c_str(), &ptr, b);
      bool found = false;
      for (ll i=2; i*i <= inbase; i++)
        if (inbase % i == 0) { divs[b] = i; found = true; break; }
      if (!found) // it is prime
      { 
        //cout << num << " base " << b << endl; 
        jamcoin = false;
        break;
      }
    }
    if (jamcoin)
    {
      cout << num << ' ';
      for (ll b=2; b<=10; b++) 
      {
        cout << divs[b];
        if (b==10) cout << endl;
        else cout << ' ';
      }
      J--;
      if (J == 0) exit(0);
    }
    return;
  }
  search(seq+"0", level+1);
  search(seq+"1", level+1);
}

int main() {

  ll T;
  cin >> T >> N >> J;
  cout << "Case #1:" << endl;
  levels = N-2;
  search("", 0);
  return 0;
}

