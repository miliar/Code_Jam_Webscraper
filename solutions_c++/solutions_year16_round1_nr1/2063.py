#include <iostream>
#include <string>

using namespace std;

string findLastWord(string &S) {
  int N = S.length();
  if (N <= 1) return S;  
  string newS; newS.reserve(N);
  int lastLetterIdx = -1;
  char lastLetter = ' ';
  for (int i = 0; i < N; ++i) {
    if (S[i] >= lastLetter) {
      lastLetterIdx = i;
      lastLetter = S[i];
    }
  }
  newS.push_back(lastLetter);
  string preS = S.substr(0, lastLetterIdx);
  newS.append(findLastWord(preS));
  newS.append(S.substr(lastLetterIdx + 1));
  return newS;
}

int main (int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    string S; cin >> S;
    cout << "Case #" << t << ": "
         << findLastWord(S)
         << '\n';
  }
  cout << flush;
  return 0;
}
