/*
** main.cpp for codeJam in /home/salete_s/rendu/codeJam
**
** Made by sebperso
** Login   <salete_s@epitech.net>
**
** Started on  Sat Apr 30 17:51:16 2016 sebperso
*/

#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <fstream>
#include <istream>
#include <stdint.h>
#include <unistd.h>

using namespace std;

std::vector<char>compute(std::vector<pair<int, char> >s)
{
  std::vector<char> result;
  int it;
  int it2;

  while (!s.empty()) {
    it = distance(begin(s), max_element(begin(s), end(s)));

    s[it].first -= 1;

    it2 = distance(begin(s), max_element(begin(s), end(s)));

    if (s[it2].first == s[it].first + 1) {
      if (!(s[it2].first == 1 && s.size() % 2)) {
        s[it2].first -= 1;
        result.push_back(s[it2].second);

        if (s[it2].first == 0) {
          s.erase(begin(s) + it2);
        }
      }
    }

    result.push_back(s[it].second);

    if (s[it].first == 0) {
      s.erase(begin(s) + it);
    }

    result.push_back(' ');
  }

  return result;
}

int main()
{
  int t;
  int party;
  int sen;

  vector<pair<int, char> > senator;
  cin >> t;
  std::string tmp;
  std::vector<char> v;

  for (int i = 1; i <= t; ++i) {
    cin >> party; // read n and then m.
    char c = 'A';

    for (int i = 0; i < party; i++) {
      cin >> sen;
      senator.push_back({sen, c + i});
    }

    v = compute(senator);
    cout << "Case #" << i << ": ";

    for (auto const& it : v) {
      std::cout << it;
    }
    std::cout << std::endl;
    senator.clear();
  }
  return 0;
}
