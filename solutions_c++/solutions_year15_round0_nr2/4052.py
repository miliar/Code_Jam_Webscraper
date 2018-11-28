#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>

using namespace std;

const int inf = 1e9;
/*
int subs(vector<int> s, int tl) {
#if 1
  cout << tl << ": ";
  for (int i : s)
    cout << i << " ";
  cout << endl;
#endif
  auto mx = max_element(s.begin(), s.end());
  if (tl <= 0) return *mx;
  if (*mx == 1) return 1;
  if (*mx == 2) return 2;
  if (*mx == 3) return 3;

  vector<int> c = s;
  for (int i = 0; i < c.size(); ++i)
    c[i] = max(0, c[i]-1);

  int h = (*mx)/2;
  int r = (*mx)-h;

  *mx = h;
  s.push_back(r);

  return min(subs(s, tl-1), subs(c, tl-1))+1;
}
*/

pair<int, int> opt[] = {
  {}, // 0
  {}, // 1
  {}, // 2
  {}, // 3
  {2, 2}, // 4 
  {3, 2}, // 5
  {3, 3}, // 6
  {3, 4}, // 7
  {4, 4}, // 8
  {6, 3}, // 9
};

int subs(vector<int> s, int tl) {
  
#if 0
  cout << tl << ": ";
  for (int i : s)
    cout << i << " ";
  cout << endl;
#endif
  auto mx = max_element(s.begin(), s.end());
  if (tl <= 0) return inf;
  if (*mx == 1) return 1;
  if (*mx == 2) return 2;
  if (*mx == 3) return 3;

  vector<int> c = s;
  for (int i = 0; i < c.size(); ++i)
    c[i] = max(0, c[i]-1);

  int mmm = *mx;

  for (int i = 0; i < s.size(); ++i) {
    vector<int> s1 = s;
    if (s1[i] > 3) {
      auto p = opt[s1[i]];
      s1[i] = p.first;
      s1.push_back(p.second);
      mmm = min(mmm, subs(s1, tl-1)+1);
    }
  }

  return min(mmm, subs(c, tl-1)+1);
}


int doit() {
  int d;
  scanf("%d", &d);
  vector<int> p(d);
  for (int i = 0; i < d; ++i)
    scanf("%d", &p[i]);
  int mx = *max_element(p.begin(), p.end());
  return min(mx, subs(p, mx));
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i)
    printf("Case #%d: %d\n", i, doit());
}
