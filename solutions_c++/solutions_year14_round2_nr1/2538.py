#include <iostream>
#include <algorithm>
#include <array>
#include <climits>
#include <cmath>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

typedef long long          ll;
typedef unsigned int       uint;
typedef unsigned long long ull;

using namespace std;

ostream& operator<<(ostream &s, vector<string> v)
{
  int cnt = v.size();
  s << "[ ";
  for (int i=0; i<cnt; i++) {
	if (i > 0) s << ", ";
	s << '"' << v[i] << '"';
  }
  return s << " ]  // " << cnt << " item" << (cnt >= 2 ? "s" : "");
}

template <typename T> ostream& operator<<(ostream &s, vector<T> v)
{
  int cnt = v.size();
  s << "[ ";
  for (int i=0; i<cnt; i++) {
	if (i > 0) s << ", ";
	s << v[i];
  }
  return s << " ]  // " << cnt << " item" << (cnt >= 2 ? "s" : "");
}

template <typename T> ostream& operator<<(ostream &s, list<T> ls)
{
  int cnt = 0;
  s << "( ";
  for (auto it=ls.begin(); it!=ls.end(); it++) {
	if (it != it.begin()) s << ", ";
	s << *it;
	cnt++;
  }
  return s << " )  // " << cnt << " item" << (cnt >= 2 ? "s" : "");
}

template <typename T> ostream& operator<<(ostream &s, deque<T> st)
{
  int cnt = st.size();
  s << "[ ";
  for (auto it=st.begin(); it!=st.end(); it++) {
	if (it != st.begin()) s << ", ";
	s << *it;
  }
  return s << " ]  // " << cnt << " item" << (cnt >= 2 ? "s" : "");
}

template <typename T1, typename T2> ostream& operator<<(ostream &s, map<T1,T2> m)
{
  int cnt = m.size();
  s << "{ ";
  for (auto it=m.begin(); it!=m.end(); it++) {
	if (it != m.begin()) s << ", ";
	s << it->first << " => " << it->second;
  }
  return s << " }  // " << cnt << " item" << (cnt >= 2 ? "s" : "");
}

template <typename T> ostream& operator<<(ostream &s, set<T> st)
{
  int cnt = st.size();
  s << "[ ";
  for (auto it=st.begin(); it!=st.end(); it++) {
	if (it != st.begin()) s << ", ";
	s << *it;
  }
  return s << " ]  // " << cnt << " item" << (cnt >= 2 ? "s" : "");
}

template <typename T1, typename T2> ostream& operator<<(ostream &s, pair<T1,T2> p)
{
  return s << "(" << p.first << "," << p.second << ")";
}


int N;
vector<string> s;

string Solve(int x) {
  cin >> N;
  s.resize(N);
  for (int i = 0; i < N; i++) {
    cin >> s[i];
    s[i] += '!';
  }
  vector<string> s2(s);
  for (int i = 0; i < N; i++) {
    string t = s2[i];
    string u = "";
    for (int j = 0; j < (int)t.size() - 1; j++) {
      if (t[j] != t[j + 1]) {
        u += t[j];
      }
    }
    s2[i] = u;
  }
  for (int i = 1; i < N; i++) {
    if (s2[0] != s2[i]) {
      return "Fegla Won";
    }
  }
  int ans = 0;
  vector<int> index(N, 0);
  for (int j = 0; j < (int)s2[0].size(); j++) {
    vector<int> count(N, 0);
    for (int i = 0; i < N; i++) {
      while (index[i] + 1 < (int)s[i].size() && s[i][index[i]] == s[i][index[i] + 1]) {
        count[i]++;
        index[i]++;
      }
      index[i]++;
    }
    int average = round(accumulate(count.begin(), count.end(), 0) / N);
    for (int i = 0; i < N; i++) {
      ans += abs(count[i] - average);
    }
  }
  return to_string(ans);
}

int main() {
  int T;
  cin >> T;
  for (int x = 0; x < T; x++) {
    cout << "Case #" << (x + 1) << ": " << Solve(x + 1) << endl;
  }
}
