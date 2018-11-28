#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

int main()
{
  int T;
  int Smax;
  vector<int> S;

  cin >> T;

  for (int i = 0; i < T; i++) {
    string str;
    cin >> Smax;
    cin >> str;
    //    printf("%d %s\n", Smax, str.c_str());

    int level = 0;
    int f_num = 0;

    S = vector<int>(Smax+1);
    for (int j = 0; j < Smax+1; j++) {
      S[j] = str[j] - '0';
      //      printf("[%d]= %d, ", j, S[j]);
    }
    //    printf("\n");

    for (int j = 0; j < Smax+1; j++) {
      if (j <= level) {
        level += S[j];
      } else {
        f_num += j - level;
        level += j - level + S[j];
      }
    }
    printf("Case #%d: %d\n", i+1, f_num);
  }
}
