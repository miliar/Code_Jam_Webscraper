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
#define GETINT (scanf("%d" , &_a) , _a)
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
typedef set < PII > :: iterator IT;

void insert(PII pair, ll num, map< PII, ll >& p, set < PII >& travels) {
  if (p.find(pair) != p.end()) p[pair] = p[pair] + num;
  else p[pair] = num;
  travels.insert(pair);
}

ll calc(ll N, set < PII >& travels, map < PII, ll >& p) {
  ll sum = 0;
  for (IT it = travels.begin(); it != travels.end(); it++) {
    PII p1 = *it;
    ll count = p[p1];
    ll n = p1.second - p1.first;
    sum += (n * N - n * (n - 1) / 2) * count;
  }

  return sum;
}

void solveCase() {
  ll N = GETINT;
  int M = GETINT;

  map < PII, ll > p;
  set < PII > travels;
  FOR(i, M) {
    ll o = GETINT;
    ll e = GETINT;
    ll num = GETINT;
    PII pair = PII(o, e);
    insert(pair, num, p, travels);
  }
  //  cerr << "orig:" << endl;
  ll orig = calc(N, travels, p);

  for (IT it = travels.begin(); it != travels.end(); it++) {
    PII p1 = *it;
    for (IT jt = travels.begin(); jt != travels.end(); jt++) {
      PII p2 = *jt;
      if ((p1.first < p2.first) &&
          (p2.first <= p1.second) &&
          (p2.second > p1.second)) {
        ll c1 = p[p1];
        ll c2 = p[p2];
        ll c = min(c1, c2);
        if (c > 0) {
          //          cerr << p1.first << ' ' << p1.second << ' ' << p2.first << ' ' << p2.second << ' ' << c << endl;
          PII q1 = PII(p1.first, p2.second);
          PII q2 = PII(p2.first, p1.second);
          insert(q1, c, p, travels);
          insert(q2, c, p, travels);
          p[p1] = p[p1] - c;
          p[p2] = p[p2] - c;
        }
      }
    }
  }

  ll sum = calc(N, travels, p);
  cout << orig - sum << endl;
}

int main() 
{
  int t = GETINT;
  for (int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    //    cerr << endl;
    solveCase();
  }
  return 0;
}
