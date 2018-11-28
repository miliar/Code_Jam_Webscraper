#include <iostream>
#include <cstdlib>
#include <cstddef>
#include <vector>

using namespace std;

size_t first_method(const vector<size_t> &v) {
  size_t n = 0;
  size_t prev = 0;
  for(auto &x: v) {
    if(x < prev)
      n += (prev - x);
    prev = x;
  }
  return n;
}

size_t second_method(const vector<size_t> &v) {
  size_t prev = 0;
  size_t max_eat = 0;
  for(auto &x: v) {
    if(x < prev)
      if (prev- x > max_eat)
        max_eat = prev - x;
    prev = x;
  }
  prev = 0;
  size_t n = 0;
  for(auto &x: v) {
    if(prev > 0)
      n += min(max_eat, prev);
    prev = x;
  }

  return n;
}

pair<size_t, size_t> process(const vector<size_t> &v) {
  return pair<size_t,size_t>(first_method(v), second_method(v));
}

int main(int argc, const char **argv)
{
  size_t t;
  cin >> t;
  for(size_t i = 0; i < t; ++i) {
    size_t n;
    cin >> n;
    vector<size_t> v;
    for(size_t j = 0; j < n; ++j) {
      size_t m;
      cin >> m;
      v.push_back(m);
    }
    auto res = process(v);
    cout << "Case #" << (i+1) << ": " << res.first << " " << res.second << endl;
  }
  return EXIT_SUCCESS;
}

