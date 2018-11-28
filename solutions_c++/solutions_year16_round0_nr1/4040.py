#include<bits/stdc++.h>
using namespace std;
typedef long long int64;

struct CountingSheep
{
  CountingSheep()
  {
    int64 N;
    cin >> N;
    if(N == 0) { 
      cout << "INSOMNIA" << endl;
      return;
    }
    int bit = 0;
    for(int i = 1; true; i++) {
      stringstream sss; sss << N * i;
      string S = sss.str();
      for(int j = 0; j < S.size(); j++) {
        bit |= 1 << (S[j] - '0');
      }
      if(bit == (1 << 10) - 1) {
        cout << N * i << endl;
        return;
      }
    }
  }
};


int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    new CountingSheep();
  }
  return(0);
}
