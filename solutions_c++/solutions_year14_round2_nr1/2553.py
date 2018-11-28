#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct SequenceChar {
  char c;
  int num;
};

void createSequenceChar(string str, vector<SequenceChar> &seq) {
  char beforeChar = '\0';
  for (int i = 0; i < str.size(); i++) {
    if (beforeChar != str[i]) {
      SequenceChar s;
      beforeChar = s.c = str[i];
      s.num = 1;
      seq.push_back(s);
    }
    else {
      seq[seq.size() - 1].num++;
    }
  }
}

int main(void) {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N;
    vector<vector<SequenceChar>> S;
    cin >> N;
    for (int i = 0; i < N; i++) {
      vector<SequenceChar> seq;
      string str;
      cin >> str;
      createSequenceChar(str, seq);
      S.push_back(seq);
    }
    cout << "Case #" << t << ": ";
    int len = S[0].size();
    for (int i = 0; i < S.size(); i++) {
      if (len != S[i].size()) {
        goto CANNOT_CREATE;
      }
    }
    for (int i = 0; i < S[0].size(); i++) {
      char c = S[0][i].c;
      for (int j = 0; j < S.size(); j++) {
        if (c != S[j][i].c) {
          goto CANNOT_CREATE;
        }
      }
    }
    int ans = 0;
    for (int i = 0; i < S[0].size(); i++) {
      int m = 100;
      for (int j = 1; j <= 100; j++) {
        int sum = 0;
        for (int k = 0; k < S.size(); k++) {
          sum += abs(j - S[k][i].num);
        }
        m = min(m, sum);
      }
      ans += m;
    }
    cout << ans << endl;
    continue;
  CANNOT_CREATE:
    cout << "Fegla Won" << endl;
    continue;
  }
}