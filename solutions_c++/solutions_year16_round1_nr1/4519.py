#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<string> all;

void bar(string s, string c, int q) {
  string ccopy(c);
  reverse(c.begin(), c.end());
  c.push_back(s[q]);
  reverse(c.begin(), c.end());
  all.push_back(c);
  ccopy.push_back(s[q]);
  all.push_back(ccopy);
  if(q != s.size() -1) {
    bar(s, c, q+1);
    bar(s, ccopy, q+1);
  }
}

int main() {

  int kases;
  cin >> kases;
  for(int k = 0; k < kases; k++) {
    string s;
    cin >> s;

    bar(s, "", 0);
    sort(all.begin(), all.end());

    cout << "Case #" << k+1 << ": " << all.back() << endl;
    all.clear();

  }

  return 0;

}
