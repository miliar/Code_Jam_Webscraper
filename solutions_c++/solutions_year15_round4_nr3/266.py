#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <unordered_set>
#include <future>
using namespace std;

future<string> solve()
{
  int n; cin>>n;
  cin.ignore();
  vector<vector<int>> ls(n);
  map<string,int> dict;
  for (int i=0;i<n;i++) {
    string line; getline(cin, line);
    stringstream ss(line);
    for (string w; ss>>w;) {
      if (!dict.count(w))
        dict.insert(make_pair(w, dict.size()));
      ls[i].push_back(dict[w]);
    }
  }

  return async(std::launch::async, [n, ls]{

  set<int> e0, f0;
  e0.insert(ls[0].begin(), ls[0].end());
  f0.insert(ls[1].begin(), ls[1].end());
  int base = 0;
  for (auto &p: f0)
    base += e0.count(p);

  int ans = 999999;
  for (int b = 0; b < (1 << (n-2)); b++) {
    set<int> e, f;
    for (int i=2;i<n;i++){
      if (b&(1 << (i-2))) {
        e.insert(ls[i].begin(), ls[i].end());
      }
      else {
        f.insert(ls[i].begin(), ls[i].end());
      }
    }
    //e.insert(e0.begin(), e0.end());
    //f.insert(f0.begin(), f0.end());

    int cur = base;
    for (auto &p: f0) {
      cur += (1-e0.count(p))*e.count(p);
    }
    for (auto &p: f) {
      cur += (1-f0.count(p))*(e.count(p)|e0.count(p));
    }
    ans = min(ans, cur);
  }
  stringstream ss;
  ss << ans << endl;
  return ss.str();
  });
}

int main()
{
  int cases; cin>>cases;
  vector<future<string>> fs;
  for (int cn=1;cn<=cases;cn++){
    fs.push_back(solve());
  }

  for (int cn=1;cn<=cases;cn++){
    cout << "Case #" << cn << ": ";
    cout << fs[cn-1].get();
    cout << flush;
  }
  return 0;
}
