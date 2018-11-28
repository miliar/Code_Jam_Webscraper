#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <cstring>
#include <stack>
#include <bitset>

using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int TS, N;;
    string S;
    scanf("%d",&TS);
    for (int ts = 1; ts <= TS; ts++) {
      cin >> N >> S;
      int ans = 0;
      for (int j = 0; j <= 1000; j++) {
        bool can = true;
        int ct = j;
        for (int i = 0; i < S.length(); i++) {
          if (S[i] != '0') {
            if (ct < i) {
              can = false;
              break;
            }
            ct += S[i] - '0';
          }
        }
        if (can) {
          ans = j;
          break;
        }
      }
      printf("Case #%d: %d\n",ts, ans);
    }
    return 0;
}
