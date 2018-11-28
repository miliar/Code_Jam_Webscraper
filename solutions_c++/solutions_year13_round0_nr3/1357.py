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

bool isPalindrome(long long a) {
  vector<int> digs;
  while (a) {
    digs.pb(a % 10);
    a /= 10;
  }
  bool is = true;
  int k = digs.sz;
  FOR (i, k >> 1)
    is &= digs[i] == digs[k - i - 1];
  return is;
}

vector<long long> fairNumbers;

int main(){
  freopen("Cl1.out","wt", stdout);
  freopen("Cl1.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  fairNumbers.clear();
  ffor (num, 1, 10000001)
    if (isPalindrome(num)) {
      long long a = 1LL * num * num;
      if (isPalindrome(a))
        fairNumbers.pb(a);
    }
  
  FOR (test, tests){
    long long a, b;
    cin >> a >> b;
    int cnt = 0;
    FOR (i, fairNumbers.sz)
      cnt += fairNumbers[i] >= a && fairNumbers[i] <= b;

    cout << "Case #" << (test + 1) << ": ";
    cout << cnt;
    cout << "\n";
  }
  return 0;
}
