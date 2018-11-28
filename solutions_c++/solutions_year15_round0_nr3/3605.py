#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

bool isIJK(const string& ss, int L, int X);

bool isConvertable(const string& s, int L, int R, string c);

string reduce(string s);

map<string, string> table;

int main(int argc, char* argv[]) {

  if (argc != 2) {
    printf("Usage: %s input-file\n", argv[0]);
    return -1;
  }

  table["11"] = "1";
  table["i1"] = "i";
  table["j1"] = "j";
  table["k1"] = "k";

  table["1i"] = "i";
  table["ii"] = "-1";
  table["ji"] = "-k";
  table["ki"] = "j";

  table["1j"] = "j";
  table["ij"] = "k";
  table["jj"] = "-1";
  table["kj"] = "-i";

  table["1k"] = "k";
  table["ik"] = "-j";
  table["jk"] = "i";
  table["kk"] = "-1";

  // string str = "jikjijkijjkkkkkjijkjkjjkjjikjijkjkkjkjkkkkkkkkkkkkkkkkiiiiiiiiiiiiiiiiiijkjkjijkjikjikji";
  // printf("str = %s, reduced = %s\n", str.c_str(), reduce(str).c_str());

  ifstream fin(argv[1]);

  int nCases;
  fin >> nCases;

  for (int i=0; i<nCases; ++i) {

    // printf("\n\33[33m===== Case #%d =====\33[0m\n", i + 1);

    int L, X;
    fin >> L >> X;

    string ss;
    fin >> ss;

    bool result = isIJK(ss, L, X);
    printf("Case #%d: %s\n", i + 1, result ? "YES" : "NO");
  }

  return 0;
}

bool isIJK(const string& ss, int L, int X) {
  int count[3] = {0, 0, 0};

  for (int j=0; j<ss.size(); ++j)
    count[ss[j] - 'i'] |= 1;

  if (count[0] + count[1] + count[2] <= 1)
    return false;

  string s;
  while (X-- > 0) s += ss;

  // cout << "s = \"" << s << "\"" << endl;

  if (s.size() < 3)
    return false;

  string s1;

  for (int i=1; i<s.size(); ++i) {

    s1.push_back(s[i-1]);
    // printf("i = %d, s1 = %s\n", i, s1.c_str());
    s1 = reduce(s1);

    if (s1 != "i")
      continue;

    string s2;
    string s3 = s.substr(i);

    for (int j=i+1; j<s.size(); ++j) {

      s2.push_back(s[j-1]);
      s3 = "-" + string(1, s[j-1]) + s3;

      // printf("  j = %d, s1 = \"%s\", s2 = \"%s\", s3 = \"%s\"\n", j, s1.c_str(), s2.c_str(), s3.c_str());

      s2 = reduce(s2);
      s3 = reduce(s3);

      if (s2 != "j")
	continue;

      if (s3 != "k")
	continue;

      return true;

      // printf("s1 = %s, s2 = %s, s3 = %s, s1+s2+s3 = %s\n", s1.c_str(), s2.c_str(), s3.c_str(), (s1+s2+s3).c_str());
    }
  }

  return false;
}

bool isConvertable(const string& s, int L, int R, string c) {
  auto substring = s.substr(L, R-L);
  auto ss = reduce(substring);
  // cout << "substring = " << substring << ", ss = " << ss << ", c = " << c << endl;
  return ss == c;
}

string reduce(string s) {
  if (s.size() <= 1)
    return s;

  if (table.count(s) > 0)
    return table[s];

  string old_s = s;
  while (s.size() > 2) {
    string xx = s;
    s = reduce(s.substr(0, s.size() / 2)) + reduce(s.substr(s.size() / 2));

    bool positive = true;
    for (int i=0; i<s.size(); ++i) {
      if (s[i] == '-') {
	s.erase(i, 1);
	positive = !positive;
	--i;
      }
    }

    if (!positive)
      s = '-' + s;

    // printf("%s \33[33m\t=>\t\33[0m %s\n", xx.c_str(), s.c_str());
  }

  if (table.count(s) > 0)
    s = table[s];

  table[old_s] = s;

  return s;
}
