#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

int dist(string s1, string s2, string sp) {
  int result = 0;
  int shift1 = 0;
  int shift2 = 0;

  for (int i = 0; i < sp.size(); ++i) {
    int c1 = 0;
    int c2 = 0;
    while (s1[shift1] != sp[i]) {
      c1++; shift1++;
    }
    while (s2[shift2] != sp[i]) {
      c2++; shift2++;
    }
    result += abs(c1 - c2);
  }

  result += abs(((int)s1.size() - shift1) - ((int)s2.size()-shift2));

  //cout << s1 << " " << s2 << " " << sp << " " << result << endl;
  return result;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    int words;
    cin >> words;
    vector<string> w(words);
    for (int i = 0; i < words; ++i)
      cin >> w[i]; 

    bool impossible = false;
    string sf;

    for (int i = 0; i < words; ++i) {
      for (int k = 0; k < words; ++k) {
        
        string s1;
        string s2;
        for (int l = 0; l < w[i].size(); ++l) {
          if (s1[s1.size()-1] != w[i][l])
            s1 += w[i][l];
        }

        for (int l = 0; l < w[k].size(); ++l) {
          if (s2[s2.size()-1] != w[k][l])
            s2 += w[k][l];
        }

        if (s1 != s2) {
          impossible = true;
          break;
        }
        sf = s1;
      }
      if (impossible) break;
    }

    if (impossible) {
      cout << "Fegla Won" << endl;
      continue;
    }

    int distance = 10000000;

    {
      int thisd = 0;
      for (int i = 0; i < w.size(); ++i) {
        thisd += dist(w[i], sf, sf);
      }
      distance = min(thisd, distance);
    }

    for (int i = 0; i < w.size(); ++i) {
      int thisd = 0;
      for (int k = 0; k < words; ++k) {
        thisd += dist(w[i], w[k], sf);
      }
      distance = min(distance, thisd);
    }

    cout << distance << endl;

  }
}
