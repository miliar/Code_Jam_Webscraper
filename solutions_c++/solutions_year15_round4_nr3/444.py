#include <bits/stdc++.h>
  
using namespace std;

template<class T> inline T sqr(const T& a) { return a * a; }
  
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
  
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 2100;

vector<string> Tokenize(const string &s) {
  vector<string> res;
  size_t after = 0;
  while (after != string::npos) {
    size_t next = s.find(' ', after);
    res.push_back(s.substr(after, next == string::npos ? next : (next - after)));
    //cout << "adding " << res.back() << endl;
    if (next != string::npos)
      ++next;
    after = next;
  }
  return res;
}

vector<string> saved;

vector<int> Convert(map<string, int> &dict, const vector<string> &ws) {
  vector<int> res;
  for (const string &s : ws) {
    if (dict.count(s) == 0) {
      dict.insert({s, (int) dict.size()});
      saved.push_back(s);
    }
    res.push_back(dict[s]);
  }
  return res;
}

bool eng0[N];
bool fre0[N];
bool eng[N];
bool fre[N];

void Solve() {
  int n;
  scanf("%d\n", &n);
  string s;
  map<string, int> dict;
  saved.clear();
  memset(eng0, 0, sizeof eng0);
  memset(fre0, 0, sizeof fre0);
  vector<vector<int> > sents;
  for (int i = 0; i < n; ++i) {
    getline(cin, s);
    vector<string> ws = Tokenize(s);
    vector<int> is = Convert(dict, ws);
    
    if (i == 0) {
      for (int w : is) {
        eng0[w] = true;
      }
    } else if (i == 1) {
      for (int w : is) {
        fre0[w] = true;
      }
    } else {
      sents.push_back(is);
    }
  }
  int d_size = int(dict.size());
  int m_size = d_size * int(sizeof(bool));
  int m = n - 2;
  int mend = 1 << m;
  int ans = d_size;
  for (int mask = 0; mask < mend; ++mask) {
    memcpy(eng, eng0, m_size);
    memcpy(fre, fre0, m_size);
    for (int j = 0; j < int(sents.size()); ++j) {
      const vector<int> &sent = sents[j];
      bool is_eng = (mask & (1 << j)) > 0;
      bool *dest = is_eng ? eng : fre;
      for (int i : sent)
        dest[i] = true;
    }
    int cur = 0;
    for (int i = 0; i < d_size; ++i) {
      if (eng[i] && fre[i]) {
        ++cur;
      }  
    }
#if 0
    if (cur == 2 && ans > cur) {
      for (int i = 0; i < d_size; ++i)
        if (eng[i] && fre[i])
          cout << saved[i] << " ";
      cout << " => " << cur << endl;
    }
#endif
    ans = min(ans, cur);
  }
  printf("%d\n", ans);
}

int main() {
  int tests;
  scanf("%d", &tests);
  for (int it = 1; it <= tests; ++it) {
    printf("Case #%d: ", it);
    Solve();
  }

  return 0;
}
