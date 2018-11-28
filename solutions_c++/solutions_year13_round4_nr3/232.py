/*
 * Code Jam Round 2 2013
 * File:   pCErdosSzekeres.cpp
 * Author: Andy Y.F. Huang
 * Created on June 1, 2013, 10:08 AM
 */

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

#ifdef AZN
#include "Azn.cpp"
#endif

using namespace std;

namespace pCErdosSzekeres {
int up[2222], down[2222];
int deg[2222];
vector<int> adj[2222]; //a < b
vector<int>::const_iterator it;
priority_queue<int, vector<int>, greater<int> > q;
int ans[2222];
//int temp[2222];
//int lis[2222], lds[2222];

void add(int a, int b) {
  //pln(a, b);
  adj[a].push_back(b);
  deg[b]++;
}

void solve(int test_num) {
  memset(deg, 0, sizeof (deg));
  int len;
  scanf("%d", &len);
  for (int i = 0; i < len; i++)
    cin >> up[i];
  for (int i = 0; i < len; i++)
    cin >> down[i];
  for (int i = 0; i < len; i++)
    adj[i].clear();
  for (int i = 0; i < len; i++) {
    for (int j = i + 1; j < len; j++) {
      if (up[i] >= up[j])
        add(j, i);
      if (down[i] <= down[j])
        add(i, j);
    }
    for (int j = i + 1; j < len; j++) {
      if (down[j] + 1 == down[i]) {
        add(j, i);
        break;
      }
    }
    for (int j = i - 1; j >= 0; j--) {
      if (up[j] + 1 == up[i]) {
        add(j, i);
        break;
      }
    }
  }
  printf("Case #%d:", test_num);
  for (int i = 0; i < len; i++) {
    if (deg[i] == 0)
      q.push(i);
  }
  //plnarr(deg, deg + len);
  for (int x = 1; x <= len; x++) {
    assert(!q.empty());
    int at = q.top();
    q.pop();
    //pln("at:", at);
    //plnarr(temp, temp + cnt);
    ans[at] = x;
    for (it = adj[at].begin(); it != adj[at].end(); ++it)
      if (--deg[*it] == 0)
        q.push(*it);
  }
  for (int i = 0; i < len; i++)
    printf(" %d", ans[i]);
  putchar('\n');
}

void solve() {
  #ifdef AZN
  freopen("inputC.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
  #endif
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  pCErdosSzekeres::solve();
  return 0;
}

