#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <iterator>
#define print_vector(a) cout << "{"; for (int i = 0; i < a.size(); i++) { if (i == a.size() - 1) {cout << a[i];} else { cout << a[i] << ",";}} cout << "}\n";
using namespace std;

string FILENAME = "D-large";

vector<int> read(string s){
  vector<int> ret;
  int n;
  istringstream sin(s);
  while(sin>>n)
    ret.push_back(n);
  return ret;
}

int main () {
  freopen((FILENAME + ".in").c_str(), "r", stdin);
  freopen((FILENAME + ".out").c_str(), "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  for (int case_id = 1; case_id <= testcases; case_id++) {
    int n;
    scanf("%d", &n);
    vector<double> naomi;
    vector<double> ken;
    for (int i = 0; i < n; ++i) {
      double b;
      scanf("%lf", &b);
      naomi.push_back(b);
    }
    for (int i = 0; i < n; ++i) {
      double b;
      scanf("%lf", &b);
      ken.push_back(b);
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    int war = 0;
    vector<bool> seen(n);
    fill(seen.begin(), seen.end(), 0);
    for (int i = 0; i < n; ++i) {
      bool found = false;
      for (int j = 0; j < n; ++j) {
        if (!seen[j] && ken[j] > naomi[i]) {
          found = true;
          seen[j] = true;
          break;
        }
      }
      if (!found) {
        war++;
      }
    }
    int deceit = 0;
    int naomi_index = 0;
    int ken_index = naomi.size() - 1;
    for (int i = 0; i < n; i++) {
      if (naomi[0] < ken[0]) { // can't win anything, sacrifice itself!
        ken.pop_back();
        naomi.erase(naomi.begin(), naomi.begin() + 1);
      } else {
        naomi.erase(naomi.begin(), naomi.begin() + 1);
        ken.erase(ken.begin(), ken.begin() + 1);
        deceit++;
      }
    }
    printf("Case #%d: ", case_id);
    printf("%d %d\n", deceit, war);
  }
  fflush(stdout);
}
