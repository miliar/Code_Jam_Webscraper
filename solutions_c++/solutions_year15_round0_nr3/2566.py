#include <stdlib.h>
#include <iostream>
#include <assert.h>
#include <vector>

using namespace std;

// 0: 1
// 1: i
// 2: j
// 3: k
const int prod[4][4] = {{0, 1, 2, 3},
                        {1, 0, 3, 2},
                        {2, 3, 0, 1},
                        {3, 2, 1, 0}};

// true: positive
// false: negative
const bool sign[4][4] = {{ true,  true,  true,  true},
                         { true, false,  true, false},
                         { true, false, false,  true},
                         { true,  true, false, false}};

bool solve(int L, int X, string S)
{
  vector<int> v;
  for (int x = 0; x < X; x++) {
    for (int i = 0; i < L; i++) {
      if (S[i] == 'i') {
        v.push_back(1);
      }
      else if (S[i] == 'j') {
        v.push_back(2);
      }
      else if (S[i] == 'k') {
        v.push_back(3);
      }
      else {
        assert(false);
      }
    }
  }

  // start with 1
  int p = 0;
  bool s = true;

  for (size_t i = 0; i < v.size(); i++) {
    int  np = prod[p][v[i]];
    bool ns = (s == sign[p][v[i]]);
    p = np;
    s = ns;
  }

  if (p != 0 || s != false) { // total product must be -1
    return false;
  }

  int index = v.size();
  // start with 1
  p = 0;
  s = true;

  for (size_t i = 0; i < v.size(); i++) {
    int  np = prod[p][v[i]];
    bool ns = (s == sign[p][v[i]]);
    p = np;
    s = ns;
    if (p == 1 && s == true) { // i
      index = i;
      break;
    }
  }

  if (index == v.size()) {
    return false;
  }

  int index2 = -1;
  // start with 1
  p = 0;
  s = true;

  for (int i = v.size() - 1; i >= 0; i--) {
    int  np = prod[v[i]][p];
    bool ns = (s == sign[v[i]][p]);
    p = np;
    s = ns;
    if (p == 3 && s == true) { // k
      index2 = i;
      break;
    }
  }

  if (index2 == -1) {
    return false;
  }

  if (index2 < index) {
    return false;
  }

  return true;
}

int main()
{
  int T;
  cin >> T;
  for (int count = 1; count <= T; count++) {
    int L, X;
    cin >> L >> X;
    string S;
    cin >> S;

    cout << "Case #" << count << ": " << (solve(L, X, S) ? "YES" : "NO") << "\n";
  }

  return 0;
}

