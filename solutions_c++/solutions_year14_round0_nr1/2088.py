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

string FILENAME = "A-small-attempt1";

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
    vector<int> choices;
    int answer;
    scanf("%d", &answer);
    int a, b, c, d;
    for (int i = 0; i < answer - 1; i++) {
      scanf("%d %d %d %d", &a, &b, &c, &d);
    }
    scanf("%d %d %d %d", &a, &b, &c, &d);
    choices.push_back(a);
    choices.push_back(b);
    choices.push_back(c);
    choices.push_back(d);
    for (int i = 0; i < 4 - answer; i++) {
      scanf("%d %d %d %d", &a, &b, &c, &d);
    }
    scanf("%d", &answer);
    for (int i = 0; i < answer - 1; i++) {
      scanf("%d %d %d %d", &a, &b, &c, &d);
    }
    scanf("%d %d %d %d", &a, &b, &c, &d);
    vector<int> good;
    if (find(choices.begin(), choices.end(), a) != choices.end()) {
      good.push_back(a);
    }
    if (find(choices.begin(), choices.end(), b) != choices.end()) {
      good.push_back(b);
    }
    if (find(choices.begin(), choices.end(), c) != choices.end()) {
      good.push_back(c);
    }
    if (find(choices.begin(), choices.end(), d) != choices.end()) {
      good.push_back(d);
    }
    for (int i = 0; i < 4 - answer; i++) {
      scanf("%d %d %d %d", &a, &b, &c, &d);
    }
    if (good.size() == 1) {
      printf("%d\n", good[0]);
    } else if (good.size() == 0) {
      printf("Volunteer cheated!\n");
    } else {
      printf("Bad magician!\n");
    }
  }
  fflush(stdout);
}
