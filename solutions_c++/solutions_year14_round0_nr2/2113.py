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

string FILENAME = "B-large";

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
    printf("Case #%d: ", case_id);
    fflush(stdout);
    double c, f, x;
    scanf("%lf %lf %lf", &c, &f, &x);
    double best = x / 2;
    double last = x / 2;
    for (int i = 1; i < 120001; i = i + 10000) {
      double rate = 2;
      double t = 0;
      for (int j = 0; j < i; j++) {
        t += (c / rate);
        if (t > best) {
          break;
        }
        //printf("%lf\n", t);
        rate += f;
      }
      t = t + (x / rate); 
      if (t < best) {
        best = t;
      } else {
        // i'm bad
        for (int j = max(i - 10000, 0); j < max(10000,i); ++j) {
          rate = 2;
          t = 0;
          for (int k = 0; k < j; k++) {
            t += c / rate;
            rate += f;
          }
          t = t + x / rate;
          best = min(t, best);
        }
        // i'm, really really bad
        for (int j = max(i - 20000, 0); j < max(10000,i-10000); ++j) {
          rate = 2;
          t = 0;
          for (int k = 0; k < j; k++) {
            t += c / rate;
            rate += f;
          }
          t = t + x / rate;
          best = min(t, best);
        }
        break;
      }
    }
    printf("%.7lf\n", best);
  }
  fflush(stdout);
}
