#include <iostream>
#include <set>
#include <vector>
using namespace std;
typedef long long ll;

bool is_palindrome(int n) {
  int original = n;
  int ans = 0;
  while (n) {
    ans *= 10;
    ans += n % 10;
    n /= 10;
  }
  return ans == original;
}

bool is_palindrome(ll n) {
  ll original = n;
  ll ans = 0;
  while (n) {
    ans *= 10;
    ans += n % 10;
    n /= 10;
  }
  return ans == original;
}

int main() {
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w", stdout);
    
  ll s = 1;
  ll ss = s * s;
  set<ll> squares;
  while (ss <= 100000000000000 && ss > 0) {
    squares.insert(ss);
    s++;
    ss = s * s;
  }
  
  vector<ll> fairs;
  for (ll n = 1; n < 10000000; n++) {
    if (is_palindrome(n)) {
      ll sq = n * n;
      if (is_palindrome(sq)) {
        if (squares.count(sq)) {
          fairs.push_back(sq);
        }
      }
    }
  }
//  cout << fairs.size() << endl;
//  for (int i = 0; i < fairs.size(); i++) {
//    cout << i << " " << fairs[i] << endl;
//  }
  
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int ans = 0;
    int A, B;
    scanf("%d %d", &A, &B);
    for (int i = 0; i < fairs.size(); i++) {
      if (fairs[i] >= (ll)A && fairs[i] <= (ll)B) {
        ans++;
      }
    }
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}