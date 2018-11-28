#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;


string
getResStr(const string& str) {
   string ret;

   ret += str[0];
   char c = ret[0];
   for (unsigned n = 1; n < str.size(); ++n) {
      if (str[n] != c) {
         c = str[n];
         ret += c;
      }
   }

   return ret;
}

int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   for (unsigned t = 0; t < T; ++t) {
      int result = 0;

      unsigned N = 0;
      cin >> N;

      vector<string> strs(N);
      vector<int> minCnt;
      vector<int> maxCnt;
      string resStr;
      int resSize = 0;
      for (unsigned n=0; n < N; ++n) {
         cin >> strs[n];
         if (n == 0) {
            resStr = getResStr(strs[n]);
            resSize = resStr.size();
            minCnt.resize(resSize, 200);
            maxCnt.resize(resSize, 0);
         }
         if (resStr != getResStr(strs[n])) {
            result = -1;
            break;
         } else {
            unsigned j = 0;
            vector<int> cnt(resSize, 0);
            char c = strs[n][j];
            cnt[j] = 1;
            for (unsigned i = 1; i < strs[n].size(); ++i) {
               if (strs[n][i] == c) {
                  ++cnt[j];
               } else {
                  c = strs[n][i];
                  ++j;
                  ++cnt[j];
               }
            }
            for (unsigned i = 0; i < resSize; ++i) {
               if (cnt[i] < minCnt[i]) minCnt[i] = cnt[i];
               if (cnt[i] > maxCnt[i]) maxCnt[i] = cnt[i];
            }
         }
      }

      cout << "Case #" << t + 1 << ": ";
      if (result >= 0) {
         for (unsigned i=0; i<resSize; ++i) {
            result += maxCnt[i] - minCnt[i];
         }
         cout << result;
      } else {
         cout << "Fegla Won";
      }
      cout << endl;
   }

   return 0;
}

