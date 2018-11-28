#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

typedef vector <   int  > vi;
typedef vector <   vi   > vvi;
typedef vector < double > vd;
typedef vector <   vd   > vvd;
typedef vector < string > vs;

#define LIM 100000000000000LL
//#define LIM 1000000LL
#define MAX 100
ll fs[MAX];
int ns;

bool isPalindrome (ll n) {
  ll num = n;
  ll rev = 0LL;

  while (num > 0) {
    rev *= 10;
    rev += num%10;
    num /= 10;
  }

  return n == rev;
}

void precompute() {
  ll lim = LIM;
  ll i = 1LL, is = 1LL; ns = 0;
  while (is < lim) {
    if (isPalindrome (is) && isPalindrome(i))
      fs[ns++] = is;
    i++; is = i*i;
  }
}

int gEq(ll v) {
  int i = 0;
  for (;i < ns && fs[i] < v; i++);
  return i;
}

int lEq(ll v) {
  int i = ns - 1;
  for (;i >= 0 && fs[i] > v; i--);
  return i;
}

int main () {

  precompute();
/*
  cout << ns << " squared fair Numbers until " << LIM << endl;
  for (int j = 0; j < ns; j++)
    cout << fs[j] << " " << (ll) sqrt(fs[j]) << endl;
*/
  int T; cin >> T;
  ll A, B;
  for (int t = 1; t <= T; t++) {
    cin >> A >> B;
    int pA = gEq(A);
    int pB = lEq(B);

    cout << "Case #" << t << ": " << pB - pA + 1 << endl;
  }

  return 0;
}
