
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <fstream>
#include <thread>
#include <assert.h>
#include <sys/mman.h>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <sstream>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <iomanip>
#include <forward_list>

using namespace std;

void solve(int casenum) {
  printf("Case #%d: ", casenum);
  string s;
  cin >> s;
  unordered_map<char, int> m;
  for (char c : s) {
    m[c]++;
  }
  int counts[10] = {0};
  if (m['Z'] > 0) {
    int zcount = m['Z'];
    counts[0] += zcount;
    m['Z'] -= zcount;
    m['E'] -= zcount;
    m['R'] -= zcount;
    m['O'] -= zcount;
  }
  if (m['X'] > 0) {
    int xcount = m['X'];
    counts[6] += xcount;
    m['S'] -= xcount;
    m['I'] -= xcount;
    m['X'] -= xcount;
  }
  if (m['W'] > 0) {
    int xcount = m['W'];
    counts[2] += xcount;
    m['T'] -= xcount;
    m['W'] -= xcount;
    m['O'] -= xcount;
  }
  if (m['S'] > 0) {
    int xcount = m['S'];
    counts[7] += xcount;
    m['S'] -= xcount;
    m['E'] -= xcount;
    m['V'] -= xcount;
    m['E'] -= xcount;
    m['N'] -= xcount;
  }
  if (m['V'] > 0) {
    int xcount = m['V'];
    counts[5] += xcount;
    m['F'] -= xcount;
    m['I'] -= xcount;
    m['V'] -= xcount;
    m['E'] -= xcount;
  }
  if (m['G'] > 0) {
    int xcount = m['G'];
    counts[8] += xcount;
    m['E'] -= xcount;
    m['I'] -= xcount;
    m['G'] -= xcount;
    m['H'] -= xcount;
    m['T'] -= xcount;
  }
  if (m['I'] > 0) {
    int xcount = m['I'];
    counts[9] += xcount;
    m['N'] -= xcount;
    m['I'] -= xcount;
    m['N'] -= xcount;
    m['E'] -= xcount;
  }
  if (m['U'] > 0) {
    int xcount = m['U'];
    counts[4] += xcount;
    m['F'] -= xcount;
    m['O'] -= xcount;
    m['U'] -= xcount;
    m['R'] -= xcount;
  }
  if (m['R'] > 0) {
    int xcount = m['R'];
    counts[3] += xcount;
    m['T'] -= xcount;
    m['H'] -= xcount;
    m['R'] -= xcount;
    m['E'] -= xcount;
    m['E'] -= xcount;
  }
  counts[1] += m['O'];
  for (int i = 0; i < 10; ++i) {
    while (counts[i]-- > 0) {
      printf("%d", i);
    }
  }
  printf("\n");
}

int main(int argc, const char * argv[]) {
  freopen("file.txt","r",stdin);
  freopen("file.out","w",stdout);

  int t = 0;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; ++i) {
    solve(i);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
