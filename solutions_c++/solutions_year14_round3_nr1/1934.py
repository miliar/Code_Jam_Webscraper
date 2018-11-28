#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <algorithm>
#include <functional>
#include <string.h>
#include <set>
#include <deque>
#include <map>
#include <cassert>
#include <math.h>
using namespace std;

struct Case_Data {
  int i;
  int N;
  vector<vector<int> > input;
  char input2[101][101];
  char chs[101];
  int num[101][101];
  int P, Q;
//  vector<vector<char> > output_s;
};

Case_Data get_case_data() {
  Case_Data cd;
  char skip;
  scanf("%d%c%d", &cd.P, &skip, &cd.Q);
  cerr << cd.P << " " << cd.Q << endl;
  return cd;
}

int gcd(int a, int b)
{
  int t;
  while (b)
  {
    a %= b;
    t = a, a = b, b = t;
  }
  return a;
}
int deal(Case_Data &cd) {
  int t = gcd(cd.P, cd.Q);
  cerr <<"gcd: " << t << endl;
  int p = cd.P / t; int q = cd.Q / t;

  int pow_q = 0;
  for (int i = 0; i < 40; i++) {
    int tmp = pow(2, i);
    cerr << tmp << " " << q << endl;
    if (tmp > q) {
      cout << "Case #" << cd.i << ": impossible" << endl;
      return 0;
    } else if (tmp == q) {
      pow_q = i;
      break;
    }
  }
  int pow_p = 0;
  for (int i = 0; i < 40; i++) {
    int tmp = pow(2, i);
    cerr << tmp << " " << q << endl;
    if (tmp > p) {
      pow_p = i - 1;
      break;
    }
    if (tmp == p) {
      pow_p = i;
      break;
    }
  }
  cout << "Case #" << cd.i << ": " << (pow_q - pow_p) << endl;
}
int main(int argc, char **argv) {
  int case_number; char skip;
  scanf ("%d%c", &case_number, &skip);
  cerr << "input case_number " << case_number << endl;
  for (int i = 1; i <= case_number; ++i) {
    Case_Data cd = get_case_data();
    cd.i = i;
    int ret = deal(cd);
  }
}
