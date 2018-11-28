#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

int testCase()
{
  int n, x;
  scanf("%d%d", &n, &x);

  multiset<int> a;
  for (int i = 0; i < n; i++)
  {
    int s;
    scanf("%d", &s);
    a.insert(s);
  }

//  for (auto s : a)
//    cerr << s << " ";
//  cerr << endl;

  int ans = 0;
  while (!a.empty())
  {
    ans++;
    multiset<int>::iterator last = a.end();
    --last;
    int s1 = *last;
//    cerr << s1 << " ";
    a.erase(last);

    multiset<int>::iterator it = a.upper_bound(x - s1);
    if (it != a.begin())
    {
      --it;
//      cerr << *it;
      assert(s1 + *it <= x);
      a.erase(it);
    }
//    cerr << endl;
  }
  return ans;
  //printf("%d\n", ans);
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
//  cin >> T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d: %d\n", t, testCase());
  }
  return 0;
}
