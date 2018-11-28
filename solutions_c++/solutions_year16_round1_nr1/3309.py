#include <iostream>
#include <cstdio>
#include <string>
#include <cassert>

#define NDEBUG

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

using namespace std;

const char INPUT[] = "HelloWorld.inp";
const char OUTPUT[] = "HelloWorld.out";

int compare (const string & str1, const string & str2) {
  //cerr << "\"" << str1 << "\"  \"" << str2 << "\"" << endl;
  for (int id = 0; id < MIN(str1.size(), str2.size()); ++ id) {
    if (str1[id] < str2[id]) {
      return -1;
    } else if (str1[id] > str2[id]) {
      return 1;
    }
  }
  if (str1.size() > str2.size()) {
    return 1;
  } else if (str1.size() < str2.size()) {
    return -1;
  } else {
    return 0;
  }
}

int main() {
  freopen(INPUT, "r", stdin);
  freopen(OUTPUT, "w", stdout);

  int numTest;
  cin >> numTest;

  for (int idTest = 0; idTest < numTest; ++ idTest) {
    string s;
    cin >> s;

    string result = "";

    for (int idS = 0; idS < s.size(); ++ idS) {
      char c = s[idS];
      string test1 = result;
      string test2 = result;
      test1 = test1.append(1,c);
      test2 = test2.insert(0,1,c);

      if (test1.compare(test2) > 0) {
        result = test1;
      } else {
        result = test2;
      }
    }

    cout << "Case #" << idTest + 1 << ": " << result << endl;
  }

  return 0;
}
