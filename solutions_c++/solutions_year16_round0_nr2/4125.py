#include<bits/stdc++.h>
using namespace std;
typedef long long int64;

struct RevengeofthePancakes
{
  RevengeofthePancakes()
  {
    string S;
    cin >> S;
    S += "+";

    int black = count(S.begin(), S.end(), '-');
    int ret = 0;
    while(black > 0) {
      int ptr = 0;
      if(S[0] == '+') {
        while(S[ptr] == '+') {
          S[ptr++] = '-';
          ++black;
        }
      } else {
        while(S[ptr] == '-') {
          S[ptr++] = '+';
          --black;
        }
      }
      ++ret;
    }

    cout << ret << endl;
  }
};


int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    new RevengeofthePancakes();
  }
  return(0);
}
