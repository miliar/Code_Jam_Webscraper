#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "B"

#pragma comment(linker,"/STACK:32000000")

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

bool IsGood(const vi& seq, const vi& p) {
  int n = seq.size();
  vi index(n);
  for (int i = 0; i < n; ++i) {
    index[seq[i]] = i;
  }
  for (int i = 0; i < n; ++i) {
    if (p[i] != -1 && index[p[i]] > index[i]) {
      return false;
    }
  }
  return true;
}

void ComputeZFunction(const string& text, vector<int>* z_function) {
  *z_function = vector<int>(text.length(), 0);
  int rightest_prefix_begin = 1;
  int rightest_prefix_end = 0;
  for (int first_index = 1; first_index < text.length(); ++first_index) {
    int equal = min(z_function->at(first_index - rightest_prefix_begin), 
                    rightest_prefix_end - first_index + 1);
    if (equal == rightest_prefix_end - first_index + 1 &&
        rightest_prefix_end + 1 < text.length() && 
        text[rightest_prefix_end + 1] == text[rightest_prefix_end + 1 - first_index]) {
      int last_equal = rightest_prefix_end + 1;
      while (last_equal + 1 < text.length() && 
             text[last_equal + 1] == text[last_equal + 1 - first_index]) {
        ++last_equal;
      }
      rightest_prefix_begin = first_index;
      rightest_prefix_end = last_equal;
      z_function->at(first_index) = rightest_prefix_end - first_index + 1;
    } else {
      z_function->at(first_index) = equal;
      if (rightest_prefix_end < first_index) {
        rightest_prefix_begin = first_index + 1;
        rightest_prefix_end = first_index;
      }
    }
  }
  z_function->at(0) = text.length();
}

bool IsSubstring(const string& text, const string& pattern) {
  string tmp = pattern;
  tmp += '#';
  tmp += text;
  vector<int> z;
  ComputeZFunction(tmp, &z);
  for (int i = pattern.length() + 1; i < z.size(); ++i) {
    if (z[i] >= pattern.length()) {
      return true;
    }
  }
  return false;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  long t = clock();
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n, m;
    cin >> n;
    vi p(n);
    for (int i = 0; i < n; ++i) {
      cin >> p[i];
      --p[i];
    }
    string s;
    cin >> s;
    cin >> m;
    vector<string> cool(m);
    for (int i = 0; i < m; ++i) {
      cin >> cool[i];
    }
    vi totals(m, 0);
    vi substr(m, 0);
    /*double x = 1;
    for (int i = 1; i <= 100; ++i) {
      x *= i;
    }
    cerr << x << endl;*/
    /*double logf(n + 1);
    logf[1] = 0;
    for (int i = 2; i <= n; ++i) {
      logf[i] = logf[i - 1] + log(double(i));
    }*/
    vector<double> log_ways(n);
    set<int> was;
    was.insert(-1);
    vi seq;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (was.count(p[j]) && !was.count(j)) {
          seq.push_back(j);
          was.insert(j);
          break;
        }
      }
    }
    vvi children(n);
    for (int i = 0; i < n; ++i) {
      if (p[i] != -1) {
        children[p[i]].push_back(i);
      }
    }
    vi sz(n, 0);
    for (int i = n - 1; i >= 0; --i) {
      int a = seq[i];
      sz[a] = 1;
      for (int j = 0; j < children[a].size(); ++j) {
        int c = children[a][j];
        sz[a] += sz[c];
      }
    }
    int tries = 10000;
    for (int iter = 0; iter < tries; ++iter) {
      set<int> was;
      was.insert(-1);      
      string cur;
      set<int> cands;
      for (int i = 0; i < n; ++i) {
        if (p[i] == -1) {
          cands.insert(i);
        }
      }
      for (int i = 0; i < n; ++i) {
        vi cand(cands.begin(), cands.end());
        int total_size = 0;
        for (int j = 0; j < cand.size(); ++j) {
          total_size += sz[cand[j]];
        }
        int x = rand() % total_size;
        int sel = 0;
        int sum = 0;
        while (sum + sz[cand[sel]] <= x) {
          sum += sz[cand[sel]];
          ++sel;          
        }
        //seq.push_back(cand[sel]);
        cur += s[cand[sel]];
        for (int j = 0; j < children[cand[sel]].size(); ++j) {
          cands.insert(children[cand[sel]][j]);
        }
        cands.erase(cand[sel]);
        //was.insert(cand[sel]);
      }
      for (int i = 0; i < m; ++i) {
        totals[i]++;
        if (IsSubstring(cur, cool[i])) {
          ++substr[i];
        }
      }
    }
    /*int steps = 10000000;
    int first_take = 1000;
    int each = 1000;
    vvi children(n);
    for (int i = 0; i < n; ++i) {
      if (p[i] != -1) {
        children[p[i]].push_back(i);
      }
    }
    vi index(n);
    for (int i = 0; i < n; ++i) {
      index[seq[i]] = i;
    }
    for (int iter = 0; iter < steps; ++iter) {
      if (iter >= first_take && iter % each == 0) {
        string cur;
        for (int i = 0; i < seq.size(); ++i) {
          cur += s[seq[i]];
        }
        for (int i = 0; i < m; ++i) {
          totals[i]++;
          if (IsSubstring(cur, cool[i])) {
            substr[i]++;
          }
        }
      }
      vector<int> next_seq;
      int a = rand() % n;
      int b = rand() % n;
      if (a > b) {
        swap(a, b);
      }      
      bool good = true;
      if (p[seq[b]] != -1 && index[p[seq[b]]] >= a) {
        good = false;
      }
      if (good) {
        for (int i = 0; i < children[seq[a]].size(); ++i) {
          int other = children[seq[a]][i];
          if (index[other] <= b) {
            good = false;
            break;
          }
        }
      }
    }*/
    cout << "Case #" << (test_index + 1) << ":";
    cerr << "Case #" << (test_index + 1) << ":";
    for (int i = 0; i < m; ++i) {
      printf(" %.4lf", double(substr[i]) / double(totals[i]));
      fprintf(stderr, " %.4lf", double(substr[i]) / double(totals[i]));
    }
    cout << endl;
    cerr << endl;
    cerr << clock() - t << endl;
  }
  cerr << clock() - t << endl;
  return 0;
}
