#include <cstdio>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <string>
#include <set>
#include <stack>
#include <sstream>

#define pb push_back

#define mp make_pair
#define f first
#define s second
#define ll long long

using namespace std;

vector<ll> primes;
set<ll> mem;
vector<vector<ll>> sol;
ll lgput(ll base, ll exp, ll mod) {

  ll r = 1;
  while(exp > 0) {
    if (exp & 1) {
      r = (r * base) % mod;
    }
    base = (base  * base) % mod;
    exp >>= 1;
  }
  return r;
}
bool is_prime(ll val) {
  vector<int> primes{2, 3, 5, 7, 11, 13, 15, 17, 19};

  for (auto p: primes) {
    if (lgput(p, val - 1, val) != 1) {
      return false;
    }
  }
  return true;
}

ll to_int(vector<int> &v, int base) {
  ll res = 0;
  for (int i = 0; i < v.size(); ++i) {
    res = (res * base + v[i]);
  }
  return res;
}
vector<int> to_vec(ll val, int base) {
  vector<int> bin;
  while(val > 0) {
    bin.push_back(val % base);
    val /= base;
  }
  reverse(bin.begin(), bin.end());
  return bin;
}
vector<ll> gen_and_check(int N) {

  vector<ll> empty_sol;
  vector<int> v1(N, 1);
  for (int i = 1; i < N - 1; ++i) {
    v1[i] = rand() % 2;
  }

  ll z = to_int(v1, 10);
//  cerr << "Trying with" << z << "\n";
  if (mem.find(z) != mem.end()) {
    return empty_sol;
  }
  if (is_prime(z)) {
    return empty_sol;
  }
  mem.insert(z);

  vector<ll> NR(11, 0);
  for (int base = 2; base <= 10; ++base) {
    ll nr = 0;
    for (int k = 0; k < v1.size(); ++k) {
      nr = (nr * base + v1[k]);
    }
    if (is_prime(nr)) {
      return empty_sol;
    }
    NR[base] = nr;
  }

  vector<ll> cur_sol;
  for (int base = 2; base <= 10; ++base) {
    bool found = false;
    for (auto div: primes) {
      if (NR[base] % div == 0) {
        cur_sol.push_back(div);
        found = true;
        break;
      }
    }
    if (!found) {
      return empty_sol;
    }
  }
  cur_sol.push_back(z);
  return cur_sol;
}
void gen_primes() {
  int LIM = 1e7;
  vector<int>mark(LIM, 1);
  for (int i = 2; i < LIM; ++i) {
    if (mark[i]) {
      primes.push_back(i);
      for (ll j = 1LL * i * i; j < LIM; j += i) {
        mark[j] = 0;
      }
    }
  }
}
string solve(int N, int J) {
  while(J > 0) {
    vector<ll> res = gen_and_check(N);
    if (!res.empty()) {
      sol.push_back(res);
      --J;
    }
  }

  ostringstream ss;

  for (auto v: sol) {
    ss << *v.rbegin() << " ";
    for (int i = 2; i < 11; ++i) {
      ss << v[i - 2] << " " ;
    }
    ss << "\n";
  }
  return ss.str();
}
int main() {
  ifstream cin("test.in");
  ofstream cout("test.out");
  gen_primes();
  srand(time(NULL));
  int T; cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    int N, J; cin >> N >> J;
    cout << "Case #" << tc << ":\n";
    cout << solve(N, J) << "\n";
  }
  return 0;
}
