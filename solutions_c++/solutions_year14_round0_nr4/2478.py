#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

struct Ev
{
  double w;
  int ty;

  bool operator < (Ev const& other) const { return w > other.w; }
};

int war(vector<double> a, vector<double> b)
{
  int n = sz(a);
  assert(sz(b) == n);

  vector<Ev> events;
  for (int i = 0; i < n; i++)
    events.push_back({a[i], 0});
  for (int i = 0; i < n; i++)
    events.push_back({b[i], 1});
  sort(all(events));

  int first = 0, second = 0;
  for (Ev e : events)
  {
    if (e.ty == 1)
      second++;
    else if (second > 0)
      second--;
    else
      first++;
  }
  assert(first == second);
  return first;
}

void testCase()
{
  int n;
  cin >> n;
  vector<double> a(n), b(n);
  for (int i = 0; i < n; i++)
    cin >> a[i];
  for (int i = 0; i < n; i++)
    cin >> b[i];
//  sort(all(a), greater<double>());
//  sort(all(b), greater<double>());
  
  printf("%d %d\n", n - war(b, a), war(a, b));
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d: ", t);
    testCase();
  }
  return 0;
}
