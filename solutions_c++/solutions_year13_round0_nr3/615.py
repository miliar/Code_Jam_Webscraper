#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (cin >> _a , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

set<ll> fair;
map < ll, int > indices;

bool isPalindrome(ll n) {
  vector<int> digits;
  while(n > 0) {
    digits.push_back(n % 10);
    n /= 10;
  }
  int s = digits.size();
  for (int i = 0; 2 * i < s; i++) if (digits[i] != digits[s-1-i]) {
      return false;
    }
  return true;
}

void preprocess() {
  int count = 0;
  for (ll i = 1; i <= 1000*1000*10; i++) {
    if (isPalindrome(i) && isPalindrome(i*i)) {
      ll s = 1LL * i * i;
      fair.insert(s);
      indices[s] = count++;
    }
  }
}


void solveCase() {
  ll a, b; cin >> a >> b; cerr << "GOT " << a << ' ' << b << endl;
  set<ll>::iterator it;

  it = fair.lower_bound(a);
  int low = indices[*it];
  cerr << *it << ' ' << low << endl;
  it = fair.upper_bound(b);
  if (it == fair.end() || *it > b) {
    cerr << "BAD!" << *it << ' ' << b << ' ';
    it--;
    cerr << *it << endl;
  }
  int high = indices[*it];
  cerr << *it << ' ' << high << endl;
  printf("%d\n", high - low + 1);
}

int main() 
{
   preprocess();
  cerr << "done" << endl;
  int t = GETINT;
  for (int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    solveCase();
  }
  return 0;
}
