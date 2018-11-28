#include <gmpxx.h>
//#include <gtk/gtk.h>
//#include <cairo.h>

#include "shelly.hpp"

using namespace std;
using namespace shelly;

int swap_sort(vector<int> in, bool b) {
  int res = 0;
  if (!b) {
    while (true) {
      bool j = false;
      for (size_t i = 1; i < in.size(); i++) {
        if (in[i - 1] > in[i]) {
          j = true;
          res++;
          swap(in[i - 1], in[i]);
        }
      }
      if (!j)
        break;
    }
  } else {
    while (true) {
      bool j = false;
      for (size_t i = 1; i < in.size(); i++) {
        if (in[i - 1] < in[i]) {
          j = true;
          res++;
          swap(in[i - 1], in[i]);
        }
      }
      if (!j)
        break;
    }
  }
  return res;
}

bool Check(const vector<int> &a) {
  int  m = INT32_MIN;
  size_t pos;
  for (size_t i = 0; i < a.size(); i++) {
    m = max(m, a[i]);
    if (m == a[i])
      pos = i;
  }
  for (size_t i = 1; i <= pos; i++) {
    if (a[i - 1] > a[i])
      return false;
  }
  for (size_t i = pos + 1; i < a.size(); i++) {
    if (a[i - 1] < a[i])
      return false;
  }
  return true;
}
/*
int Do(const vector<int> &all, const vector<int> &ss, int i) {
  vector<int> goal;
  vector<int> l(ss.begin(), ss.end() - i), r(ss.end() - i, ss.end());

  goal.insert(goal.begin(), r.begin(), r.end());
  goal.insert(goal.end(), l.rbegin(), l.rend());
  cout << to_string(goal) << endl;
  vector<int> tt(ss.size());
  for (size_t i = 0; i < goal.size(); i++) {
    int pos = find(all.begin(), all.end(), goal[i]) - all.begin();
    tt[pos] = i;
  }
  int tr = swap_sort(tt, false);
  goal.clear();

  goal.insert(goal.end(), l.begin(), l.end());
  goal.insert(goal.end(), r.rbegin(), r.rend());
cout << to_string(goal) << endl;
  for (size_t i = 0; i < goal.size(); i++) {
    int pos = find(all.begin(), all.end(), goal[i]) - all.begin();
    tt[pos] = i;
  }
  int ts = swap_sort(tt, false);

  return min(tr, ts);
}*/

int Do(const vector<int> &all, vector<int> &l, vector<int> &r) {
  int i = l.size() + r.size();
  if (i == all.size()) {
    vector<int> tl = l, tr = r;
    Sort(tl);
    sort(tr.rbegin(), tr.rend());

    vector<int> goal = tl;
    goal.insert(goal.end(), tr.begin(), tr.end());

    vector<int> tt(goal.size());
    for (size_t i = 0; i < goal.size(); i++) {
      int pos = find(all.begin(), all.end(), goal[i]) - all.begin();
      tt[pos] = i;
    }
    return swap_sort(tt, false);
  }
  int res = INT32_MAX;
  l.push_back(all[i]);
  res = min(res, Do(all, l, r));
  l.pop_back();

  r.push_back(all[i]);
  res = min(res, Do(all, l, r));
  r.pop_back();

  return res;
}

int main(int argc, char **argv) {
  freopen("input.txt", "r", stdin);
//  gtk_init(&argc, &argv);
  int T;
  cin >> T;
  for (int TT = 1; TT <= T; TT++) {
    int N;
    cin >> N;
    vector<int> all;
    for (int i = 0; i < N; i++) {
      int t;
      cin >> t;
      all.push_back(t);
    }
    vector<int> l, r;
    int best = Do(all, l, r);
    cout << Format("Case #%0: %1", TT, best) << endl;
  }
  return 0;
}
