#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;



inline char getWinner(const char a, const char b) {
  if (a == 'P') {
    if (b == 'R')
      return a;
    else
      return b;
  } else if (a == 'R') {
    if (b == 'S')
      return a;
    else
      return b;
  } else if (a == 'S') {
    if (b == 'P')
      return a;
    else
      return b;
  }
  return '\0';
}

bool isTie(const string &perm) {
  if (int(perm.length()) == 1)
    return false;
  string newPerm;
  for (int i = 0; i < int(perm.length()); i += 2) {
    if (perm[i] == perm[i + 1])
      return true;
    newPerm.push_back(getWinner(perm[i], perm[i + 1]));
  }
  return isTie(newPerm);
}

int main() {
  ifstream in("input.txt");
  ofstream out("output.txt");
  int testCount;
  in >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    int N, P, R, S;
    in >> N >> R >> P >> S;
    string perm = "";
    for (; P > 0; --P)
      perm += "P";
    for (; R > 0; --R)
      perm += "R";
    for (; S > 0; --S)
      perm += "S";
    do {
      if (!isTie(perm))
        break;
    } while (next_permutation(perm.begin(), perm.end()));
    out << "Case #" << test << ": " << (isTie(perm) ? "IMPOSSIBLE" : perm) << "\n";
  }
  in.close();
  out.close();
  return 0;
}
