#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <string.h>
#include <utility>
#include <set>
#include <tuple>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <map>
#include <fstream>
using namespace std;

#define vi vector<int> 
#define pii pair<int, int>
#define mp make_pair
#define mt make_tuple
#define ll long long
#define INF 20000
#define all(a) a.begin(), a.end()
#define pb push_back
#define umap unordered_map

int
Solve(string&s, int pos, int state) {
   if (pos >= s.size()) return 0;
   int i = pos;
   int w = 0;
   if (s[i] == '-') {
      while (i < s.size() && s[i] == '-') i++;
      w = (state == 2) ? 2 : 1;
      state = 1;
   } else {
      while (i < s.size() && s[i] == '+') i++;
      w = 0;
      state = 2;
   }
   return Solve(s, i, state) + w;
}

int
main() {
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int n = 0;
   cin >> n;
   for (int i = 0; i < n; i++) {
      string s;
      cin >> s;
      int res = Solve(s, 0, 0);
      cout << "Case #" << i + 1 << ": " << res << endl;
   }
   return 0;
}