#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef long long LL;
const LL MOD = 1000000007;
const LL INF = 10000000000LL;

template <class T>
struct BIT/*{{{*/
{
  vector<T> tree;
  const int size;
  BIT(int s) : tree(s), size(s) {}
  // i 番目までの要素の累積和
  int read(int i) const
  {
    int sum = 0;
    while (i > 0) {
      sum += tree[i];
      i -= i & -i;
    }
    return sum;
  }

  // i 番目の要素
  int read_single(int i) const
  {
    int sum = tree[i];
    if (i > 0) {
      const int z = i - (i & -i);
      --i;
      while (i != z) {
        sum -= tree[i];
        i -= (i & -i);
      }
    }
    return sum;
  }

  void add(int i, int v)
  {
    while (i <= size) {
      tree[i] += v;
      i += (i & -i);
    }
  }
};/*}}}*/

int bubble_cnt(const vector<LL> &v, int start, int end, bool rev) {
    BIT<int> bit(2000);
    int res = 0;
    for(int i = start; i < end; ++i) {
        res += bit.read(v[i]);
        const int val = rev ? v[i] : 1500 - v[i];
        bit.add(val, 1);
    }
    return res;
}

void solve(int CASE) {
    int N;
    cin >> N;

    vector<LL> as(N);
    map<LL,LL> dict;
    for(int i = 0; i < N; ++i) {
        cin >> as[i];
        dict[as[i]] = 1;
    }
    {
        int idx = 1;
        for(auto &p : dict) {
            p.second = idx;
            ++idx;
        }
    }
    for(LL &a : as) {
        a = dict[a];
    }

    auto max_it = max_element(as.begin(), as.end());
    int max_pos = max_it - as.begin();
    as.erase(max_it);

    LL res = INF;
    for(int i = 0; i < N; ++i) {
        //const int move_cost = i <= max_pos ? max_pos - i : i - max_pos + 1;
        const int cost = abs(i - max_pos) + bubble_cnt(as, 0, i, false) + bubble_cnt(as, i, N-1, true);
        //cout << cost << endl;
        if(cost < res) {
            res = cost;
        }
    }
    cout << "Case #" << CASE << ": " << res << endl;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);

    int N;
    cin >> N;
    for(int CASE = 1; CASE <= N; ++CASE) {
        solve(CASE);
    }
    return 0;
}
