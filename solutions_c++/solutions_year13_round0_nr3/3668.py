#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()
#define mp make_pair

using namespace std;
typedef long long ll;

vector<int> num;

void testCase()
{
  ll a, b;
  cin >> a >> b;
  printf("%d\n", (int)(upper_bound(all(num), b) - lower_bound(all(num), a)));
}

bool palindrome( ll a )
{
  ll x = 0;
  for (ll b = a; b; b /= 10)
    x = x * 10 + b % 10;
  return x == a;
}

int main() {
//  freopen("sample.in", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  for (ll a = 1; a <= 10000000; a++)
    if (palindrome(a) && palindrome(a * a))
      num.push_back(a * a);
//      cout << a << " " << a * a << endl;

  int n;
  cin >> n;
  for (int ti = 0; ti < n; ++ti) {
    printf("Case #%i: ", ti + 1);
    testCase();
  }

  return 0;
}
