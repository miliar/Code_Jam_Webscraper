#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <ctime>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define ALL(x) x.begin(), x.end()
#define F first
#define S second
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,-1,sizeof(x))
#define pw(x) (1ull<<(x))

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

const int maxn = (int)(1e7+10);

int z[maxn];
int col[maxn];
int n;

int num[20];
bool pal(ll a) {
  int c = 0;
  while (a>0) {
    num[c++] = a%10;
    a/=10;
  }
  bool ok = true;
  for (int i=0;i<c/2 && ok;i++) if (num[i]!=num[c-1-i]) ok = false;
  return ok;
}

void build() {
  for (int i=1;i<maxn;i++) {
    if (pal(i) && pal((ll)i*i)) z[i] = 1;
    col[i] = col[i-1]+z[i];
  }
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  build();
  int t; cin >> t;
  for (int i=0;i<t;i++) {
    ll a,b; cin >> a >> b;
    ll rgr = sqrt(a);
    if (rgr*rgr==a) rgr--;
    cout << "Case #" << i+1 << ": " << col[(ll)sqrt(b)]-col[rgr] << "\n";
  }
  return 0;
}
