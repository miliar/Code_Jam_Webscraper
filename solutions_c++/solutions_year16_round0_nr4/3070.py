#include <iostream>
#include <vector>
#include <bitset>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <iomanip>

using namespace std;

#define debug(x) cout << #x << ": " << x << endl;

template<typename T>
ostream& operator<<(ostream &ost, const vector<T> &v) {for(auto&& a : v) {ost << a << " ";} return ost;};

template<typename K, typename V>
ostream& operator<<(ostream &ost, const map<K,V> &v) {for(auto&& a : v) {ost << a.first << " => " << a.second << endl;} return ost;};

void compute(long long K, long long C, long long S)
{
  cout.setf(ios::fixed);
  for (unsigned long long i = 1; i <= S; ++i)
  {
    cout << i << " ";
  }
}

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
  {
    int k,c,s;
    cin >> k >> c >> s;
    cout << "Case #" << i << ": "; compute(k,c,s); cout << endl;
  }
}
