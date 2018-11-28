#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

template<typename T> std::ostream& operator<<(std::ostream& str, const std::vector<T>& v) { str << "["; for(auto n : v) str << n << ", "; str << "]"; return str; }
template<typename K, typename V> std::ostream& operator<<(std::ostream& str, const std::unordered_map<K,V>& m) { str << "["; for(auto n : m) str << n.first << " => " << n.second <<  ", "; str << "]"; return str; }

#define debug(x) cout <<  #x  << ": " << x << endl


void solve1(vector<int> &shrooms)
{
  int r = 0;
  for (int i = 1; i < shrooms.size(); i++)
  {
    if (shrooms[i] - shrooms[i-1] < 0)
      r += shrooms[i-1] - shrooms[i];
  }
  cout << r;
}


void solve2(vector<int> &shrooms)
{
  double low = -1;
  double high = 10000;



  while (low + 0.0001 < high)
  {
    double mid = (low+high) /2;
    //cout << "trying: " << mid << endl;
    bool possible = true;
    for (int i = 1; i < shrooms.size() && possible; i++)
    {
      if (shrooms[i] < shrooms[i-1] - mid*10)
        possible = false;
    }
    if (possible)
    {
      high = mid;
      //cout << "POSSIBLE" << endl;
    }
    else
    {
      low = mid;
      //cout << "NOPE" << endl;
    }
  }
//  cout << "FOUND: " << high<< endl;
  int res = 0;

  for (int j = 0; j < shrooms.size()-1; j++)
  {
    res += min<double>(shrooms[j], 10*high);
    //cout << res << ", ";
  }
  //cout << endl;
  cout << res;
}



int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  int T;
  cin >> T;

  for (int i = 1; i <= T; i++)
  {

    int N;
    cin >> N;
    vector<int> shrooms;
    for (int j = 0; j < N;j++)
    {
      int temp;
      cin >> temp;
      shrooms.push_back(temp);
    }

    cout << "Case #" << i << ": ";
    solve1(shrooms);
    cout << " ";
    solve2(shrooms);
    cout << endl;
  }
}
