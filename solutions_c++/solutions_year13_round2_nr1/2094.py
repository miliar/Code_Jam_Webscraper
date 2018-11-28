#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <utility>

using namespace std;

typedef vector<int> VI;
typedef pair<int,int> PII;

VI motes;


int costs_to_eat(int a, int start, int end) {
    //   cout << "costs_to_eat(" << a << ", " << start << ", " << end << ")" << endl;
    if(start >= motes.size() || start >= end) {return 0;}
    if(a > motes[start]) {
        return costs_to_eat(a + motes[start], start + 1, end);
    } else {
        return 1 + min(a > 1 ? costs_to_eat(2 * a - 1, start, end) : 1000000000, costs_to_eat(a, start, end - 1));
    }
}

int main(int argc, char* argv[]) {
    motes = VI();
  if(argc != 2) {
    cout << "please pass exactly one argument" << endl;
    exit(1);
  }
  ifstream input;
  input.open(argv[1]);
  int t(0);
  input >> t;
  for(int i(0); i != t; ++i) {
      cout << "Case #" << i+1 << ": ";
      int a(0);
      int n(0);
      input >> a >> n;
      motes.clear();
      for(int j(0); j != n; ++j) {
          int temp(0);
          input >> temp;
          motes.push_back(temp);
      }
      sort(motes.begin(), motes.end());
      cout << costs_to_eat(a, 0, n) << endl;
  }

  input.close();
  return 0;
}
