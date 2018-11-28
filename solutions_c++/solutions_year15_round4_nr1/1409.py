#include<iostream>
#include <assert.h>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define sss(n, size) fgets(n, size, stdin)
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define V(x) vector<x>

ll gcd(ll r0, ll r1)
{
    if(r0==0 || r1==0)
    return 1;

    if(r0<r1)
    return gcd(r1,r0);

    if(r0%r1==0)
    return r1;

    return gcd(r1,r0%r1);
}
ll findInverse(ll a, ll b)
{
    ll x[3];
    ll y[3];
    ll quotient  = a / b;
    ll remainder = a % b;
    x[0] = 0;
    y[0] = 1;
    x[1] = 1;
    y[1] = quotient * -1;

    ll i = 2;
    for (; (b % (a%b)) != 0; i++)
    {
        a = b;
        b = remainder;
        quotient = a / b;
        remainder = a % b;
        x[i % 3] = (quotient * -1 * x[(i - 1) % 3]) + x[(i - 2) % 3];
        y[i % 3] = (quotient * -1 * y[(i - 1) % 3]) + y[(i - 2) % 3];
    }
    //x[i — 1 % 3] is inverse of a
    //y[i — 1 % 3] is inverse of b
    return x[(i - 1) % 3];
}

int t,n,r,c;

enum D {
  N = 0,
  UP = 1,
  DOWN = -1,
  RIGHT = 2,
  LEFT = -2,
};

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/

struct data {
  int x, y;
  data() {}
  data(int x_, int y_) {
    x = x_;
    y = y_;
  }
};

char s[1000];
int a[100][100], v[100][100];
vector<data> q;

void dfs(int x, int y, int dir) {
  if (x < 0 || y < 0 || y >= c || x >= r) {
    int size = q.size();
    data temp = q[size-1];
    v[temp.x][temp.y] = 2;
    return;
  }
  if (v[x][y] > 0 && a[x][y] != 0) {
    return;
  }
  v[x][y] = 1;
  if (a[x][y] != N) {
    q.push_back(data(x,y));
  }
  int tdir = a[x][y];
  if (tdir == N) {
    tdir = dir;
  }
  if (tdir == N) {
    return;
  } else if (tdir == UP) {
    dfs(x-1, y, tdir);
  } else if (tdir == DOWN) {
    dfs(x+1, y, tdir);
  } else if (tdir == RIGHT) {
    dfs(x, y+1, tdir);
  } else {
    dfs(x, y-1, tdir);
  }
}

int check(int x, int y) {
  FOR(i, x+1, r) {
    if (a[i][y] != N) {
      return 1;
    }
  }
  REP(i, x) {
    if (a[i][y] != N) {
      return 1;
    }
  }
  REP(i, y) {
    if (a[x][i] != N) {
      return 1;
    }
  }
  FOR(i, y+1, c) {
    if (a[x][i] != N) {
      return 1;
    }
  }
  return 0;
}

int main() {

  si(t);
  REP(prob, t) {
    si(r);
    si(c);
    memset(v, 0, sizeof(v));
    REP(i, r) {
      ss(s);
      REP(j, c) {
        if (s[j] == '.') {
          a[i][j] = 0;
        } else if (s[j] == '^') {
          a[i][j] = 1;
        } else if (s[j] == 'v') {
          a[i][j] = -1;
        } else if (s[j] == '>') {
          a[i][j] = 2;
        } else {
          a[i][j] = -2;
        }
      }
    }
    REP(i, r) {
      REP(j, c) {
        q.clear();
        if (a[i][j] != 0) {
          dfs(i, j, N);
        }
      }
    }
    int flag = 0, ans = 0;
    REP(i, r) {
      REP(j, c) {
        if (v[i][j] == 2) {
          ans++;
          if (!check(i, j)) {
            flag = 1;
            break;
          }
        }
      }
    }
    if (flag) {
      printf("Case #%d: IMPOSSIBLE\n", prob+1);
    } else {
      printf("Case #%d: %d\n", prob+1, ans);
    }
  }

  //system("pause");
  return 0;
}
