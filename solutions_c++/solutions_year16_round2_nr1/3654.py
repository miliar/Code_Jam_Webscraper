#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <string>
#include <bitset>

using namespace std;

#define debug(x) cout << #x << ": " << x << endl;
template <typename T>
ostream& operator<<(ostream& ost, const vector<T> &vec) {
  ost << "[";
  for (auto&& a : vec) cout << a << ", ";
  ost << "]";
  return ost;
};

template <typename K, typename V>
ostream& operator<<(ostream& ost, const map<K,V> &m) {
  ost << "{";
  for (auto&& a : m) cout << a.first << " => " << a.second << ", ";
  ost << "}";
  return ost;
};

map<int, string> numbers{
  {0,"ZERO"},
  {1, "ONE"},
  {2, "TWO"},
  {3, "THREE"},
  {4, "FOUR"},
  {5, "FIVE"},
  {6, "SIX"},
  {7, "SEVEN"},
  {8, "EIGHT"},
  {9, "NINE"}
};

bool mEmpty(const vector<int> m) {
  int cnt = 0;
  for (auto &c : m) cnt += c;
  return cnt==0;
}

bool contains(vector<int> m, int number) {
  vector<int> t(26,0);
  for(auto c : numbers.at(number)) {
    t.at(c-'A')++;
  }

  for (int i = 0 ; i < t.size(); ++i) {
    if (m.at(i) < t.at(i)) return false;
  }

  return true;
}

vector<int> r(vector<int> m, string s) {
  auto cp = m;
  for (auto c : s) {
    if (m.at(c-'A') == 0) {
      debug(m);
      debug(c);
    }
    cp.at(c-'A')--;
  }
  return cp;
}

vector<int> result;

void rec(vector<int> m, vector<int> res) {
  if (!result.empty()) return;
  if (mEmpty(m)) {
    result = res;
    return;
  }

  for (const auto& v : numbers) {
    if (contains(m, v.first)) {
      auto res_copy = res;
      res_copy.push_back(v.first);

      auto cp_m = m;
      rec(r(m, v.second), res_copy);
      m = cp_m;
    }
  }

}

void solve(string& input) {

  result = vector<int>();
  vector<int> m(26,0);
  for (auto &c : input) m[c - 'A']++;

  rec(m, vector<int>{});
  sort(result.begin(), result.end());
  for (auto c : result) cout << c;
}

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
  {
    string input;
    cin >> input;
    cout << "Case #"<<i<<": ";solve(input); cout << endl;
  }
}
