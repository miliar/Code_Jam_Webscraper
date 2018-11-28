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

void
Solve(ll N, int testCase) {
   if (N == 0) {
      cout << "Case #" << testCase << ": " << "INSOMNIA" << endl;
      return;
   }
   int table[11]; memset(table, 0, sizeof(table));
   ll seen = 0;
   ll last = 0;
   ll curr = N;
   while (seen < 10) {
      last = curr;
      ll tmp = curr;
      bool repeat = true;
      while (tmp) {
         int dig = tmp % 10; tmp /= 10;
         if (table[dig] == 0) {
            table[dig] = 1; seen++;
            repeat = false;
         }
      }
      curr += N;
   }
   cout << "Case #" << testCase << ": " << last << endl;
}

int
main() {
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int n = 0;
   cin >> n;
   for (int i = 0; i < n; i++) {
      int N = 0;
      cin >> N;
      Solve(N, i + 1);
   }
   return 0;
}