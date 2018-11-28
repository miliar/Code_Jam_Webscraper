#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <utility>
#include <deque>

using namespace std;

const long long MOD = 1000002013;

long long dist (long long o, long long e, long long n)
{
  long long res = 0;
  long long a, b;
  a = n * (e - o);
//  cerr << "o,e,n: " << o <<  " " << e << " " << n << endl;
//  cerr << "A : " << a << endl;

  b = (e - o - 1) * (e - o);
  b /= 2;

//  cerr << "B: " << b << endl;

  res = a - b;
  res %= MOD;

  return res;
}

void solve()
{
  long long pres = 0;
  long long res = 0;
  long long n, m;
  vector < pair < pair < long long , int > , long long > > v(0);

  cin >> n;
  cin >> m;
  for (int i = 0; i < m; ++i)
  {
    long long o, e, p;
    cin >> o >> e >> p;
    v.push_back(make_pair (make_pair (o, 0), p));
    v.push_back(make_pair (make_pair (e, 1), p));

    pres += dist(o, e, n) * p;
    pres %= MOD;
  }
  
  deque < pair < long long, long long > > current (0);
  sort(v.begin(), v.end());

  for (int i = 0; i < v.size(); ++i)
  {
    if (v[i].first.second == 0)
    {
      current.push_front(make_pair (v[i].first.first, v[i].second));
    }
    else
    {
      long long p = v[i].second;
      while (p != 0)
      {
        long long minus_p = min(p, current[0].second); 
//        cerr << minus_p << endl;

        res += (minus_p * dist(current[0].first, v[i].first.first, n)) % MOD;
        res %= MOD;
//        cerr << dist(current[0].first, v[i].first.first, n) << endl;

        p -= minus_p;
        current[0].second -= minus_p;
        if (current[0].second == 0)
          current.pop_front();
      }
    }
  }

  long long ans = pres - res;
  if (ans < 0)
    ans += MOD;

  ans %= MOD;

  cout << ans;
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests_count;
  scanf("%d\n", &tests_count);
  for (int test = 0; test < tests_count; ++test)
  {
    cout << "Case #" << test + 1 << ": ";
    solve();
    cout << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}

