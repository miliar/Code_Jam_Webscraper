#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
// TIPS: {{{
// speed up iostream: ios_base::sync_with_stdio(0); cin.tie(0);
// memset(arr, 0, sizeof(arr))
// }}}
// {{{
template<typename A, typename B>
ostream& operator <<(ostream& s, const pair<A, B>& p)
{
  return s << "(" << p.first << "," << p.second << ")";
}
template<typename T>
ostream& operator <<(ostream& s, const vector<T>& c)
{
  s << "[ ";
  for (auto it : c) s << it << " ";
  s << "]";
  return s;
}
// }}}

char LETTER[] = {'P', 'R', 'S'};

void generate_sequence(int* num)
{
  if (num[0] == 0 || num[1] == 0 || num[2] == 0) {
    for (int i = 0; i < 3; ++i) {
      if (num[i])
        cout << LETTER[i];
    }
    return;
  }

  int subnum[3];
  for (int i = 0; i < 3; ++i)
    subnum[i] = num[i] >> 1;
  for (int i = 0; i < 3; ++i) {
    if (num[i] & 1) {
      subnum[i] += 1;
      break;
    }
  }
  generate_sequence(subnum);
  for (int i = 0; i < 3; ++i)
    subnum[i] = num[i] - subnum[i];
  generate_sequence(subnum);
}

int main()
{
  int T;
  int n;
  int now[2];
  int num[3];
  int cnt[2];
  cin >> T;
  for (int TT = 1; TT <= T; ++TT) {
    // Do it
    cin >> n;
    for (int i = 0; i < 3; ++i)
      cin >> num[i];
    swap(num[0], num[1]);
    now[0] = 0;
    now[1] = 1;
    cnt[0] = 1;
    cnt[1] = 2;
    for (int i = 1; i < n; ++i) {
      int t0 = now[1] + now[1];
      int t1 = now[0] + now[1];
      now[0] = t0;
      now[1] = t1;
    }
    for (int i = 0; i < 3; ++i) {
      if (num[i] == now[0])
        --cnt[0];
      else if (num[i] == now[1])
        --cnt[1];
      }
    if (cnt[0] || cnt[1]) {
      cout << "Case #" << TT << ": IMPOSSIBLE" << endl;
      continue;
    }

    cout << "Case #" << TT << ": ";
    generate_sequence(num);
    cout << endl;
  }
  return 0;
}

// vim: fdm=marker fdl=0

