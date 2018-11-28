#include <algorithm>
#include <iterator>
#include <iostream>
#include <numeric>
#include <utility>
#include <string>
#include <vector>
#include <set>

using namespace std;

std::string solve(const vector<int>& v)
{
  int n = v.size();
  //int sum = accumulate(v.begin(), v.end(), 0);
  std::set<pair<int, int> > pq;

  for(int i = 0; i < n; i++)
    pq.insert(make_pair(v[i], i));

  std::vector<std::string> out;

  int target = pq.begin()->first;

  while(pq.rbegin()->first != target) {
    auto first_max = pq.rbegin();
    pair<int, int> new_elem = make_pair(first_max->first - 1, first_max->second);
    pq.erase(*first_max);
    out.push_back(std::string(1, char(new_elem.second + 'A')));
    pq.insert(new_elem);
  }

  if(pq.size() % 2 == 1) {
    auto _max = pq.rbegin();
    for(int i = 0; i < _max->first; i++)
      out.push_back(std::string(1, char(_max->second + 'A')));
    pq.erase(*_max);
  }

  vector<pair<int, int> > lin;
  copy(pq.begin(), pq.end(), std::back_inserter(lin));
  for(size_t i = 0; i < lin.size(); i += 2) {
    for(int j = 0; j < lin[i].first; j++) {
      out.push_back(std::string(1, char(lin[i].second + 'A')));
      out.back() += char(lin[i + 1].second + 'A');
    }
  }

  std::string ans;
  for(size_t i = 0; i < out.size(); i++) {
    ans += out[i];
    if(i+1 != out.size())
      ans += ' ';
  }

  return ans;
}

int main()
{
  int tests;
  cin >> tests;

  int n;

  for(int t = 1; t <= tests; t++) {
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++)
      cin >> v[i];

    cout << "Case #" << t << ": " << solve(v) << endl;
  }


	return 0;
}
