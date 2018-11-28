#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <tuple>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
  int T;
  cin >> T;
  string empty;
  getline(cin, empty);

  for (int testCase=0; testCase < T; ++testCase)
  {
    int solve = 0; 
    string str;
    getline(cin, str);

    string out;

    out.push_back(str[0]);

    for (int i = 1; i < str.size(); ++i)
      if (str[i] < out[0])
        out.push_back(str[i]);
      else
        out.insert(out.begin(), str[i]);

    cout << "Case #"<<testCase+1<<": ";

    cout << out << endl;
  }

  return 0;
}