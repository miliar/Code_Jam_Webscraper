#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

long long A, B, K;

long long dp[2][2][2][32];

long long memo(bool sA, bool sB, bool sK, int bit) {
  if (bit < 0)
    return 1LL;
    
  long long &ret = dp[sA][sB][sK][bit];
  if (ret != -1)
    return ret;
  
  ret = 0LL;
  
  long long b = 1LL << bit;
  bool hA = (A & b) != 0;
  bool hB = (B & b) != 0;
  bool hK = (K & b) != 0;
  
  // 00
  ret += memo(sA || hA, sB || hB, sK || hK, bit - 1);
  // 01
  if (sB || hB)
    ret += memo(sA || hA, sB, sK || hK, bit - 1);
  // 10
  if (sA || hA)
    ret += memo(sA, sB || hB, sK || hK, bit - 1);
  // 11
  if ((sA || hA) && (sB || hB) && (sK || hK))
    ret += memo(sA, sB, sK, bit - 1);
  
  return ret;
}

int main(){
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cin >> A >> B >> K;
    A--;
    B--;
    K--;
    cout << "Case #" << (test + 1) << ": ";
    SET(dp, 255);
    cout << memo(0, 0, 0, 31);
    cout << "\n";
  }
  return 0;
}
