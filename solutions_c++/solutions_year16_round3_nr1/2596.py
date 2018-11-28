#include <cstdio>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <utility>
#include <functional>
using namespace std;

//for(int i = 0; i < N; ++i) {
//
//}

int main(int argc, char* argv[]) {
  freopen("A-large(1).in", "r", stdin);
  freopen("out.txt", "w", stdout);
  int T,N;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #"<<t<<": ";
    cin >> N;
    int tmp = N;
    vector<pair<int, char>> p;
    char ch = 'A';
    for(int i = 0; i <= 26; ++i)
      p.push_back(make_pair(0, ch++));
    for (int i = 0; i < N; ++i)
      cin >> p[i].first;
    p.erase(remove_if(p.begin(), p.end(), [](pair<int, char> pr){return pr.first == 0;}), p.end());
    int total = 0;
    for_each(p.begin(), p.end(), [&](pair<int, char>& pa){total += pa.first;});
    sort(p.begin(), p.end(), greater<pair<int, char>>());
    while(p.front().first > 0) {
      if(total == 3) {
        cout << p.front().second << " ";
        --p.front().first;
        --total;
        sort(p.begin(), p.end(), greater<pair<int, char>>());
        continue;
      }
      cout << p.front().second;
      --p.front().first;
      --total;
      if((p.size() > 1) && (p[1].first > 0) &&  (p.front().first <= (total-1) / 2)) {
        --p[1].first;
        cout << p[1].second;
        --total;
      }
      if(total > 0)
        cout << " ";
      sort(p.begin(), p.end(), greater<pair<int, char>>());
    }
    
    cout << endl;
  }
  return 0;
}