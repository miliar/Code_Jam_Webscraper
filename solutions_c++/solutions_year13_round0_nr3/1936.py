#include<cstdio>
#include<cassert>

#include<vector>
#include<algorithm>
#include<iostream>
#include<string>

using namespace std;
int pals[40] ={0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,
111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};



int main(){
  assert(freopen("input.txt", "r", stdin));
  assert(freopen("output.txt", "w", stdout));

  int tests;
  cin >> tests;

  for(int i = 1; i <= tests; ++i){
    long long a, b;

    cin >> a >> b;
    int ans = 0;
    for(int j = 0; j < 40; ++j)
      if((long long) pals[j] * pals[j] >= a && (long long)pals[j] * pals[j] <= b)
        ++ans;

    cout << "Case #" << i << ": " << ans << "\n";
  }
  return 0;
}
