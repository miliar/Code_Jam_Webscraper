#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> doit(const vector<pair<long long, long long> >& v) {
  bool zero = false;
  for (long long i = 0; i < v.size(); i++) if (v[i].first == 0) zero = true;
  if (!zero) return vector<long long>();

  if (v.size() == 1 && v[0].first == 0 && v[0].second == 2) {
    return vector<long long>(1, 0);
  }
  if (v.size() == 2 && v[0].second == 1 && v[1].second == 1) {
    if (v[0].first == 0) return vector<long long>(1, v[1].first);
    if (v[1].first == 0) return vector<long long>(1, v[0].first);
    return vector<long long>();
  }

  for (long long i = v.size()-1; i > 0; i--) {
    long long cand = v[0].first-v[i].first;
//cout << "Trying " << cand << endl;
    vector<pair<long long, long long> > v2 = v;
    bool fail = false;
    for (long long j = 0; j < v2.size(); j++) if (v2[j].second > 0) {
      long long p = lower_bound(v2.begin(), v2.end(),
          make_pair(v2[j].first - cand, -1LL)) - v2.begin();
      if (p == v2.size() || v2[p].first != v2[j].first - cand ||
          v2[p].second < v2[j].second) {
        fail = true;
        break;
      }
      v2[p].second -= v2[j].second;
    }
    if (fail) continue;
    vector<pair<long long, long long> > v3;
    for (long long j = 0; j < v2.size(); j++) if (v2[j].second > 0) {
      v3.push_back(v2[j]);
      v3.back().first -= cand;
    }
    vector<long long> ret = doit(v3);
    if (ret.size()) {
      ret.insert(ret.begin(), cand);
      return ret;
    }
  }

  {
//cout << "Trying 0" << endl;
    bool fail = false;
    for (long long i = 0; i < v.size(); i++) {
      if (v[i].second % 2) {
        fail = true;
        break;
      }
    }
    if (!fail) {
      vector<pair<long long, long long> > v2 = v;
      for (long long i = 0; i < v2.size(); i++) v2[i].second /= 2;
      vector<long long> ret = doit(v2);
      if (ret.size()) {
        ret.insert(ret.begin(), 0);
        return ret;
      }
    }
  }

  for (long long i = 1; i < v.size(); i++) {
    long long cand = v[i].first-v[0].first;
//cout << "Trying " << cand << endl;
    vector<pair<long long, long long> > v2 = v;
    bool fail = false;
    for (long long j = 0; j < v2.size(); j++) if (v2[j].second > 0) {
      long long p = lower_bound(v2.begin(), v2.end(),
          make_pair(v2[j].first + cand, -1LL)) - v2.begin();
      if (p == v2.size() || v2[p].first != v2[j].first + cand ||
          v2[p].second < v2[j].second) {
        fail = true;
        break;
      }
      v2[p].second -= v2[j].second;
    }
    if (fail) continue;
    vector<pair<long long, long long> > v3;
    for (long long j = 0; j < v2.size(); j++) if (v2[j].second > 0) {
      v3.push_back(v2[j]);
    }
    vector<long long> ret = doit(v3);
    if (ret.size()) {
      ret.insert(ret.begin(), cand);
      return ret;
    }
  }

  return vector<long long>();
}

int main() {
  long long T, P, prob=1;
  for (cin >> T; T--;) {
    cin >> P;
    vector<pair<long long, long long> > v(P);
    for (int i = 0; i < P; i++) cin >> v[i].first;
    for (int i = 0; i < P; i++) cin >> v[i].second;
    vector<long long> ret = doit(v);
    cout << "Case #" << prob++ << ":";
    for (int i = 0; i < ret.size(); i++) cout << ' ' << ret[i];
    cout << endl;
  }
}
