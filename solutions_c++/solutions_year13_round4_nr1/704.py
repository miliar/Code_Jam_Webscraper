#pragma comment(linker, "/STACK:46777216")

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <algorithm>
#include <memory.h>
#include <cmath>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned char byte;
typedef pair<int, int> pii;
#define forn(i,n) for (ll i = 0; i < ll(n); ++i)
#define mp make_pair

int main() {
  int T;
  cin >> T;
  forn (_, T) {
    cout << "Case #" << (_ + 1) << ": ";
    ll n, m; cin >> n >> m;
    map<ll, ll> in, out;
    ll res = 0;
    const ll mod = 1000002013;
    forn (i, m) {
      ll o, e, p; cin >> o >> e >> p;
      in[o] += p;
      out[e] += p;
      ll cost = ll(e - o) * n - ll(e - o) * (e - o - 1) / 2;
      cost %= mod;
      cost *= p;
      cost %= mod;
      res = (res + mod - cost) % mod;
    }

    priority_queue<pair<ll, ll>> q;
    for (map<ll, ll>::iterator it = in.begin(); it != in.end(); ++it) {
      q.push(std::make_pair(-it->first, it->second));
    }
    for (map<ll, ll>::iterator it = out.begin(); it != out.end(); ++it) {
      q.push(std::make_pair(-it->first, -it->second));
    }

    map<ll, ll> tickets;

    
    ll prev = 0;
    
    while (!q.empty()) {
      ll pos = -(q.top().first);
      map<ll, ll> nt;
      ll diff = pos - prev;
      for ( map<ll, ll>::iterator it = tickets.begin(); it != tickets.end(); ++it) {
        ll cost = diff * (-it->first) - diff * (diff - 1) / 2;
        cost %= mod;
        cost *= it->second;
        cost %= mod;
        res = (res + cost) % mod;
        nt[-((-it->first) - diff)] = it->second;
      }
      tickets.swap(nt);

      ll value = q.top().second;
      q.pop();
      if (value < 0) { // exit
        value *= -1;
        while (value > 0) {
          ll cnt = tickets.begin()->second;
          cnt = min(cnt, value);
          value -= cnt;

          tickets.begin()->second -= cnt;
          if (tickets.begin()->second == 0) {
            tickets.erase(tickets.begin());
          }
        }
      } else {
        tickets[-n] += value;
      }
      prev = pos;
    }

    res = (mod - res) % mod;
    cout << res << endl;
  }


  return 0;
}