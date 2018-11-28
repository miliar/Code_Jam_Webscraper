#include <iostream>
#include <vector>
#include <bitset>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>

using namespace std;

#define debug(x) cout << #x << ": " << x << endl;

template<typename T>
ostream& operator<<(ostream &ost, const vector<T> &v) {for(auto&& a : v) {ost << a << " ";} return ost;};

template<typename K, typename V>
ostream& operator<<(ostream &ost, const map<K,V> &v) {for(auto&& a : v) {ost << a.first << " => " << a.second << endl;} return ost;};

constexpr int N = 16;
constexpr int J = 50;

struct result {
  string coin;
  vector<int> div;
};

int getDiv(long long val) {
  for (int i = 2; i <= sqrt(val); ++i)
  {
    if (val % i == 0) return i;
  }

  return -1;
}

unordered_set<long long> primes() {
  long long max = pow(10,N);
  unordered_set<long long> res;
  vector<bool> t(max);
  for (int i = 2; i < max; ++i)
  {
    if (!t[i]) {
      res.insert(i);
      for (int j = i*i; j < max; j+=i) {
        t[j] = true;
      }
    }
  }

  return res;
}

void compute()
{
  int cnt = 0;
  int c = (1 << (N-1)) + 1;

  for (int i = 0; cnt < J && i < 1<< (N-1); ++i)
  {
    string s = "1" + std::bitset<N-2>(i).to_string() + "1";
    result res{s,{}};
    for (int i = 2; i <= 10; ++i)
    {
      long long conv = stoul(s,0,i);
      if (getDiv(conv) == -1)  break;
      res.div.push_back(getDiv(conv));
    }

    if (res.div.size() == 9)
    {
      cnt++;
      cout << res.coin << " " << res.div << endl;
    }
  }

}

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
  {
    cout << "Case #" << i << ": " << endl; compute();
  }
}
