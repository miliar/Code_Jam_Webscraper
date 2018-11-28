// TEMPLATE {{{
#include <bits/stdc++.h>
using namespace std;
#ifndef LOCAL
#define OJ 1
#else
#define OJ 0
#endif
 
#define endl '\n'
#define TIMESTAMP merr << "Execution time: " << (double)clock()/CLOCKS_PER_SEC << " s.\n"
class C_ {}; template <typename T> C_& operator <<(C_& __m, const T& __s) { if (!OJ) cerr << "\E[91m" << __s << "\E[0m"; return __m; }
C_ merr;
 
struct __s { __s() { if (OJ) { ios_base::Init i; cin.sync_with_stdio(0); cin.tie(0); } } ~__s(){ TIMESTAMP; } } __S;
/// END OF TEMPLATE }}}

#include <tr1/unordered_set>

const long long P = 59;

long long hash(const string & s) {
  long long h = 0;
  long long p = 1;
  for (int i = 0; i < (int)s.size(); i++) {
    h += (s[i]-'a'+1)*p;
    p *= P;
  }
  return h;
}

vector<long long> split(const string & s) {
  istringstream iss(s);
  vector<string> result;
  copy(istream_iterator<string>(iss),
      istream_iterator<string>(),
      back_inserter(result));
  vector<long long> res;
  for (int i = 0; i < (int)result.size(); i++) {
    res.push_back(hash(result[i]));
  }
  return res;
}

int main(void) {
  int T;
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  cin >> T;
  for (int tt = 0; tt < T; tt++) {
    int n;
    string ss;
    tr1::unordered_set<long long> SE, SF;
    vector<long long> VE, VF;
    vector<long long> eng, fre;
    vector<long long> V[22];
    cin >> n;
    cin.get();
    getline(cin, ss);
    eng = split(ss);
    getline(cin, ss);
    int ans = 1000000000;
    fre = split(ss);
    for (int i = 0; i < n-2; i++) {
      getline(cin, ss);
      V[i] = split(ss);
    }
    for (int i = 0; i < (int)eng.size(); i++) {
      SE.insert(eng[i]);
    }
    for (int i = 0; i < (int)fre.size(); i++) {
      SF.insert(fre[i]);
    }
    for (tr1::unordered_set<long long>::const_iterator it = SE.begin(); it != SE.end(); ++it) {
      VE.push_back(*it);
    }
    for (tr1::unordered_set<long long>::const_iterator it = SF.begin(); it != SF.end(); ++it) {
      VF.push_back(*it);
    }
    n -= 2;
    for (int bit = 0; bit < (1<<n); bit++) {
      tr1::unordered_set<long long> SE2, SF2;
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < (int)V[i].size(); j++) {
          if (bit & (1<<i)) {
            SE2.insert(V[i][j]);
          } else {
            SF2.insert(V[i][j]);
          }
        }
      }
      int cnt = 0;
      bool ok = true;

      if (VE.size() + SE2.size() <= VF.size() + SF2.size()) {
        // for (set<string>::const_iterator it = SE.begin(); it != SE.end(); ++it) {
          // const string & s = *it;
          // if (SF.find(s) != SF.end() || SF2.find(s) != SF2.end()) cnt++;
        // }
        for (int i = 0; i < (int)VE.size(); i++) {
          const long long & s = VE[i];
          if (SF.find(s) != SF.end() || SF2.find(s) != SF2.end()) cnt++;
          if (cnt >= ans) { ok = false; break; }
        }
        if (cnt < ans) for (tr1::unordered_set<long long>::const_iterator it = SE2.begin(); it != SE2.end(); ++it) {
          const long long & s = *it;
          if (SE.find(s) != SE.end()) continue;
          if (SF.find(s) != SF.end() || SF2.find(s) != SF2.end()) cnt++;
          if (cnt >= ans) { ok = false; break; }
        }
      } else {
        // for (set<string>::const_iterator it = SF.begin(); it != SF.end(); ++it) {
          // const string & s = *it;
          // if (SE.find(s) != SE.end() || SE2.find(s) != SE2.end()) cnt++;
        // }
        for (int i = 0; i < (int)VF.size(); i++) {
          const long long & s = VF[i];
          // if (SF.find(s) != SF.end() || SF2.find(s) != SF2.end()) cnt++;
          if (SE.find(s) != SE.end() || SE2.find(s) != SE2.end()) cnt++;
          if (cnt >= ans) { ok = false; break; }
        }
        if (cnt < ans) for (tr1::unordered_set<long long>::const_iterator it = SF2.begin(); it != SF2.end(); ++it) {
          const long long & s = *it;
          if (SF.find(s) != SF.end()) continue;
          if (SE.find(s) != SE.end() || SE2.find(s) != SE2.end()) cnt++;
          if (cnt >= ans) { ok = false; break; }
        }
      }

      if (ok) ans = min(ans, cnt);
    }
    cout << "Case #" << tt+1 << ": " << ans << endl;
    merr << "Case #" << tt+1 << ": " << ans << endl;
  }
  return 0;
}
