#include "cmath"
#include "cstdio"
#include "sstream"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

string digits[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
vector<vector<int>> by_char(26);
pair<char, int> single[] = { make_pair('Z', 0), make_pair('W', 2), make_pair('U', 4), make_pair('X', 6),
    make_pair('G', 8), make_pair('F', 5), make_pair('V', 7), make_pair('H', 3), make_pair('O', 1), make_pair('I', 9) };

string solve(string s)
{
  vector<int> nb_digits(10);
  vector<int> totalChars(26);
  for (auto c : s) {
    totalChars[(int)(c - 'A')]++;
  }
  for (auto p : single) {
    int n = p.second;
    int nb_found = totalChars[(int)(p.first - 'A')];
    nb_digits[n] = nb_found;
    for (auto c : digits[n]) {
      totalChars[(int)(c - 'A')] -= nb_found;
    }
  }
  ostringstream str;
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < nb_digits[i]; j++)
      str << (char)('0' + i);
  }
  return str.str();
}

int mainA() {
  for (int i = 0; i < 9; i++) {
    for (auto c : digits[i]) {
      int to_add = (int)(c - 'A');
      by_char[to_add].push_back(i);
    }
  }
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    fflush(stderr);
    char s[2001];
    scanf("%s", s);

    printf("Case #%d: %s\n", Ti, solve(s).c_str());
    fflush(stdout);
  }
  return 0;
}
