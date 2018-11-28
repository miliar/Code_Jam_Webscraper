#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define TAM       1001
bool isP[TAM];
vector<int> P;
ll num[TAM], numBase;

int n;

void init ( int base ) {
  numBase = base;
  for ( int p : P )
    num[p] = 0;
}

void add ( int d ) {
  for ( int p : P )
    num[p] = ( num[p] * numBase + ll(d) ) % ll(p);
}

int getDiv ( ) {
  for ( int p : P )
    if ( num[p] == 0 )
      return p;
  return 0;
}

int divs[11];

bool check ( int m ) {
  for ( int b = 2; b <= 10; ++b ) {
    init(b);
    add(1);
    for ( int i = 0; i< n; ++i )
      add((m>>i)&1);
    add(1);
    if ( !( divs[b] = getDiv() ) )
      return 0;
  }
  return 1;
}

unsigned int g_seed = 1000000021;
const unsigned int FASTRAND_MAX = 0x7FFF;
inline int fastrand() {
  g_seed = (214013*g_seed+2531011);
  return (g_seed>>16)&0x7FFF;

}

int main ( )
{
  memset ( isP, true, sizeof(isP) );
  isP[0] = isP[1] = false;
  for ( int i = 2; i*i < TAM; ++i )
    if ( isP[i] )
      for ( int j = i*i; j < TAM; j += i )
        isP[j] = false;
  for ( int i = 2; i < TAM; ++i )
    if ( isP[i] )
      P.push_back(i);

  cout << "Case #1:\n";
  int k;
  cin >> n >> n >> k;
  n -= 2;
  set<int> seen;
  while ( seen.size() < k ) {
    int m = fastrand()%(1<<n);
    if ( check(m) ) {
      if ( seen.count(m) ) continue;
      seen.insert(m);
      string s ( n+2, '1' );
      for ( int i = 0; i < n; ++i )
        if ( !( (m>>i)&1 ) )
          s[i+1] = '0';
      cout << s;
      for ( int i = 2; i <= 10; ++i )
        cout << ' ' << divs[i];
      cout << endl;
    }
  }
  return 0;
}
