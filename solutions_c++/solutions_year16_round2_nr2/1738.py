#include <iostream>
#include <limits>
#include <bitset>
#include <algorithm>
#include <map>
#include <iomanip>

#include <boost/lexical_cast.hpp>

using namespace std;


const std::string VALS("0123456789");


void add_numbers(const string& s, vector<int>& P) {
  for (size_t i = 0; i < s.size(); ++i) {
    if (s[i] == '?') {
      for (auto c : VALS) {
        string s1(s);
        s1[i] = c;
        add_numbers(s1, P);
      }
      return;
    }
  }
  P.push_back(boost::lexical_cast<int>(s));
}

int main() {
  std::ios::sync_with_stdio(false);
  int T; cin >> T;

  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": ";
    string C, J;
    cin >> C >> J;

    int min_score = std::numeric_limits<int>::max();
    std::vector<std::pair<int, int> > min_scores;

    vector<int> possible_Cs;
    vector<int> possible_Js;

    add_numbers(C, possible_Cs);
    add_numbers(J, possible_Js);

    sort(possible_Cs.begin(), possible_Cs.end());
    sort(possible_Js.begin(), possible_Js.end());

    for (int c : possible_Cs) {
      for (int j : possible_Js) {
        auto diff = abs(j-c);
        // cerr << "(" << c << "," << j << ") = " << diff << "\n";
        if (diff < min_score) {
          min_score = diff;
          min_scores.clear();
          min_scores.push_back(make_pair(c, j));
        } else if ( diff == min_score) {
          min_scores.push_back(make_pair(c, j));
        }
      }
    }

    sort(min_scores.begin(), min_scores.end(), [](const pair<int, int>& a, const pair<int,int>& b) -> bool {
      if (a.first < b.first) {
        return true;
      } else if (a.first == b.first) {
        return (a.second <= b.second);
      } else {
        return false;
      }
    });
    cout << setfill('0');
    cout << setw(C.size()) << min_scores[0].first << ' ' << setw(J.size()) << min_scores[0].second << '\n';
  }
}
